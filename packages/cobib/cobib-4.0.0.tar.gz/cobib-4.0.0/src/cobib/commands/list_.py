r"""coBib's List command.

This command simply lists the entries in the database:
```
cobib list
```
By default, it lists them in the order in which they appear in the database. However, the order as
well as selection of entries to be listed can be manipulated via additional arguments as explained
below.

### Basic Options

It provides some very basic output manipulation options.

You can reverse the output:
```
cobib list --reverse
```
You can sort the list according to a database field:
```
cobib list --sort year
```
(In the TUI, this is available via the `s` key, by default.)


### Filters

However, the arguably most useful feature of this command are the *filters*.

These are a set of keyword arguments which are registered at runtime depending on the fields which
appear in your database.
To give an example, you can find the following filters in the output of `cobib list --help`:
```
++author AUTHOR
--author AUTHOR
++year YEAR
--year YEAR
```
As you can see, each field is used twice: once with a `++` and once with a `--` prefix.
These allow you to specify positive and negative matches, respectively.
For example:
```
cobib list ++year 2020
```
will list *only* entries whose `year` contains `2020`.
On the contrary:
```
cobib list --year 2020
```
will print all those entries whose `year` does *not* contain `2020`.

You can combine multiple filters to narrow your selection down further.
For example:
```
cobib list ++year 2020 ++author Rossmannek
```
will list entries whose `year` contains `2020` *and* whose `author` field contains `Rossmannek`.

Note, that by default you can use the `f` key in the TUI to add filters to the displayed list of
entries.

There are some aspects to take note of here:
1. By default, multiple filters are combined with logical `AND`s. You can specify `--or` to
   overwrite this to logical `OR`s. This will apply to all filters of the specified command.
2. All entries are treated as `str`. Thus, `++year 20` will match anything *containing* `20`.

As of version v3.2.0, the filter arguments are evaluated as regex patterns allowing you to do things
like the following:
```
cobib list ++label "\D+_\d+"
```
This will list all entries whose labels are formatted as `"<non-digit characters>_<digits>"`.

As of version v4.0.0, you can provide the `--ignore-case` (or `-i`) argument to perform the filter
matching case-**in**sensitive.
```
cobib list --ignore-case ++author rossmannek
```
This will still match entries where `Rossmannek` is contained in the author field.
You can even enable this behavior by default using the
`cobib.config.config.ListCommandConfig.ignore_case` setting.

.. note::
   For more information on the filtering mechanisms see also `cobib.database.Entry.matches`.
"""

from __future__ import annotations

import argparse
import logging
from collections import defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple, Type

from rich.console import Console, ConsoleRenderable
from rich.prompt import PromptBase
from rich.table import Table
from rich.text import Text
from textual.app import App
from textual.widgets import DataTable
from typing_extensions import override

from cobib.config import Event, config
from cobib.database import Database, Entry

from .base_command import ArgumentParser, Command

LOGGER = logging.getLogger(__name__)


class ListCommand(Command):
    """The List Command.

    This command can parse the following arguments:

        * `-s`, `--sort`: you can specify an arbitrary `cobib.database.Entry.data` field name which
          should be used for sorting the listed entries. This will automatically include a column
          for this field in the output table.
        * `-r`, `--reverse`: if specified, the entries will be listed in reverse order. This is
          especially useful in the TUI (where it is enabled by default) because it puts the last
          added entries at the top of the window. When using the command-line interface it is
          disabled by default, because this puts the last added entries at the bottom, just above
          the new command-line prompt.
        * `-i`, `--ignore-case`: if specified, the entry matching will be case **in**sensitive. You
          can enable this setting permanently via the
          `cobib.config.config.ListCommandConfig.ignore_case` setting.
        * `-x`, `--or`: if specified, multiple filters will be combined with logical OR rather than
          the default logical AND.
        * in addition to the options above, [Filter keyword arguments](#filters) are registered at
          runtime based on the fields available in the database. Please refer that section or the
          output of `cobib list --help` for more information.
    """

    name = "list"

    @override
    def __init__(
        self,
        *args: str,
        console: Console | App[None] | None = None,
        prompt: Type[PromptBase[str]] | None = None,
    ) -> None:
        super().__init__(*args, console=console, prompt=prompt)

        self.entries: List[Entry] = []
        """A list of entries, filtered and sorted according to the provided command arguments."""

        self.columns: List[str] = []
        """A list of (key) columns to be included when rendering the results."""

    @override
    @classmethod
    def init_argparser(cls) -> None:
        parser = ArgumentParser(
            prog="list", description="List subcommand parser.", prefix_chars="+-"
        )
        parser.add_argument("-s", "--sort", help="specify column along which to sort the list")
        parser.add_argument(
            "-r", "--reverse", action="store_true", help="reverses the listing order"
        )
        parser.add_argument(
            "-i", "--ignore-case", action="store_true", help="ignore case for entry matching"
        )
        parser.add_argument(
            "-x",
            "--or",
            dest="OR",
            action="store_true",
            help="concatenate filters with OR instead of AND",
        )
        unique_keys: Set[str] = {"label"}
        LOGGER.debug("Gathering possible filter arguments.")
        for entry in Database().values():
            unique_keys.update(entry.data.keys())
        for key in sorted(unique_keys):
            parser.add_argument(
                "++" + key, type=str, action="append", help="include elements with matching " + key
            )
            parser.add_argument(
                "--" + key, type=str, action="append", help="exclude elements with matching " + key
            )

        cls.argparser = parser

    @override
    @classmethod
    def _parse_args(cls, args: tuple[str, ...]) -> argparse.Namespace:
        args = tuple(arg for arg in args if arg != "--")

        return super()._parse_args(args)

    @override
    def execute(self) -> None:
        LOGGER.debug("Starting List command.")

        Event.PreListCommand.fire(self)

        filtered_entries, filtered_keys = self.filter_entries()

        self.entries = self._sort_entries(filtered_entries, self.largs.sort, self.largs.reverse)

        # construct list of columns to be displayed
        self.columns = config.commands.list_.default_columns
        # display the column along which was sorted
        if self.largs.sort and self.largs.sort not in self.columns:
            self.columns.append(self.largs.sort)
        # also display the keys which were used to filter
        self.columns.extend(col for col in filtered_keys if col not in self.columns)

        Event.PostListCommand.fire(self)

    def filter_entries(self) -> Tuple[List[Entry], Set[str]]:
        """The filtering method.

        This method implements the actual filtering routine. Based on the arguments provided to this
        command, this method will iterate the database and return those entries which match the
        specified filter.

        Returns:
            A pair indicating the matching entries. The first object is the list of matching entries
            (which is also exposed via `entries`). The second object is the set of keys which were
            filtered on. This can be used (for example) to include these keys during the result
            rendering.
        """
        LOGGER.debug("Constructing filter.")

        filtered_keys: Set[str] = set()
        _filter: Dict[Tuple[str, bool], List[Any]] = defaultdict(list)

        for key, val in self.largs.__dict__.items():
            if key in ["OR", "sort", "reverse", "ignore_case"] or val is None:
                # ignore special arguments
                continue

            # track the keys being filtered to display these columns later
            filtered_keys.add(key)

            if not isinstance(val, list):
                val = [val]
            # iterate values to be filtered by
            for i in val:
                for idx, obj in enumerate(self.args):
                    if i == obj:
                        # once we find the current value in the CLI argument list we can determine
                        # whether this filter is INclusive (`++`) or EXclusive (`--`)
                        index: Tuple[str, bool] = (key, self.args[idx - 1][0] == "+")
                        _filter[index].append(i)
                        break

        LOGGER.debug("Final filter configuration: %s", dict(_filter))

        if self.largs.OR:
            LOGGER.debug("Filters are combined with logical ORs!")

        ignore_case = config.commands.list_.ignore_case or self.largs.ignore_case

        for key, entry in Database().items():
            if entry.matches(_filter, self.largs.OR, ignore_case):
                LOGGER.debug('Entry "%s" matches the filter.', key)
                self.entries.append(entry)

        return self.entries, filtered_keys

    @staticmethod
    def _sort_entries(
        entries: List[Entry], sort: Optional[str] = None, reverse: bool = False
    ) -> List[Entry]:
        """The sorting method.

        This method sorts the provided entries according to the requested key and order.

        Args:
            entries: the list of entries to be sorted.
            sort: the optional key by which to sort.
            reverse: whether or not to sort in reverse order.

        Returns:
            The sorted list of entries.
        """
        if sort is None:
            if reverse:
                return entries[::-1]
            return entries

        sorted_entries: List[Entry] = sorted(
            entries, reverse=reverse, key=lambda entry: entry.stringify().get(str(sort), "")
        )

        return sorted_entries

    @override
    def render_porcelain(self) -> List[str]:
        output: List[str] = []

        output.append("::".join(self.columns))

        for entry in self.entries:
            stringified: Dict[str, str] = entry.stringify()

            output.append("::".join(stringified.get(col, "") for col in self.columns))

        return output

    @override
    def render_rich(self) -> ConsoleRenderable:
        rich_table = Table()

        for col in self.columns:
            rich_table.add_column(col)

        for entry in self.entries:
            stringified: Dict[str, str] = entry.stringify()

            rich_table.add_row(*(stringified.get(col, "") for col in self.columns))

        return rich_table

    @override
    def render_textual(self) -> DataTable[Text]:
        textual_table: DataTable[Text] = DataTable(id="cobib")
        textual_table.cursor_type = "row"
        textual_table.fixed_columns += 1
        textual_table.zebra_stripes = True
        # TODO: figure out why the following is necessary since the following commit:
        # https://github.com/Textualize/textual/commit/a4252a5760539177f6db8231d4229e8eada923e7
        textual_table.styles.height = "1fr"

        for col in self.columns:
            textual_table.add_column(col, width=None)

        for entry in self.entries:
            stringified: Dict[str, str] = entry.stringify()

            textual_table.add_row(*(Text(stringified.get(col, "")) for col in self.columns))

        return textual_table
