# Copyright (C) 2023 MatrixEditor
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import annotations

__doc__ = """Simple and small python module to perform SAST scans."""
__version__ = "0.0.1"
__authors__ = "MatrixEditor"

import sys
import os
import re
import logging
import json
import yaml
import pathlib
import subprocess
import datetime
import importlib

from typing import Generator, Any

RESULT_KEY_META = "meta"
RESULT_KEY_FILES = "files"
RESULT_KEY_ABS_PATH = "abs_path"
RESULT_KEY_LINES = "lines"
RESULT_KEY_POSITIONS = "positions"
RESULT_KEY_MATCHES = "matches"
RESULT_KEY_RULE_ID = "rule-id"
ALL_RESULT_KEYS = [
    # Just put top level result keys here
    RESULT_KEY_META,
    RESULT_KEY_FILES,
    RESULT_KEY_RULE_ID,
]

DEFAULT_MAX_BYTES = 100 * 1024 * 1024  # 100 MB

DEFAULT_PATTERN_ENGINE = "re"

FILTER_FILE_EXT = "file_ext"
FILTER_FILE_NAME = "file_name"
FILTER_FULL_PATH = "full_path"
FILTER_MIME_TYPE = "mime_type"
VALID_FILTER_KEYS = [
    FILTER_FILE_EXT,
    FILTER_FILE_NAME,
    FILTER_FULL_PATH,
    FILTER_MIME_TYPE,
]

PYSAST_LOGGER = "pysast-logger"

logger = logging.getLogger(PYSAST_LOGGER)


def is_rule_file(file_path: str) -> bool:
    """Returns whether the file path looks like a supported rule definition."""
    if not file_path:
        return False

    for suffix in ("yml", "yaml", "json"):
        if file_path.lower().endswith(f".{suffix}"):
            return True

    return False


def get_mime_type(file_path: str) -> str | None:
    """Retrieve the MIME type of a file.

    :param file_path: The path to the file.
    :type file_path: str
    :rtype: str | None
    :return: The MIME type of the file, or None if it couldn't be determined.
    """
    try:
        with subprocess.Popen(
            f"file -b --mime-type {file_path}".split(" "),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ) as pipe:
            # Get the output from the 'file' command
            mime_type, _ = pipe.communicate()
            return mime_type.strip()
    except Exception:
        logger.debug("Could not find 'file' utility - MIME-Type will be ignored!")
        return None


def extract_filter_keys(filters: dict[str, str], is_meta=False) -> dict[str, str]:
    """Extracts valid filter keys from a dictionary of filters.

    This function iterates through the ``filters`` dictionary and selects only the
    keys that are considered valid filter keys based on a predefined list of valid
    keys (``VALID_FILTER_KEYS``). If ``is_meta`` is True, it treats ``filters`` as
    a nested dictionary and extracts the filter keys from the nested `"`filters`"`
    dictionary.

    :param filters: A dictionary of filters, where the keys are filter names and the
                    values are corresponding filter values
    :type filters: dict[str, str]
    :param is_meta: Flag indicating whether the ``filters`` dictionary should be treated
                    as a nested dictionary with a ``"filters"`` key., defaults to False
    :type is_meta: bool, optional
    :return: A dictionary containing only the valid filter keys and their corresponding
             values.
    :rtype: dict[str, str]
    """
    result = {}
    for key, value in (filters if not is_meta else filters.get("filters", {})).items():
        if key in VALID_FILTER_KEYS:
            result[key] = value
    return result


class FileFilter:
    """A utility class for filtering files based on specific criteria.

    The ``FileFilter`` class allows you to create filters for file matching. It supports
    basic string matching and regular expression matching. Filters can be inverted and
    combined to create complex filtering logic.

    Usage:
    ~~~~~~

    >>> f = FileFilter()
    >>> f.with_re()  # Enable regular expression matching
    >>> f = ~f  # Invert the filter
    >>> result = f.apply("jpg, png", "image.jpg")  # Apply the filter
    """

    def __init__(self) -> None:
        self._inverted = False
        self._use_re = False

    def reset(self):
        """Resets this filter."""
        self._inverted = False
        self._use_re = False

    def __invert__(self) -> "FileFilter":
        """Inverts the filter.

        This method flips the inversion flag of the filter. When applied, the filter will
        match files that would have been excluded and vice versa.

        :return: the instance itself
        :rtype: ``FileFilter``
        """
        self._inverted = not self._inverted
        return self

    def with_re(self) -> None:
        """Enable regular expression matching.

        This method enables regular expression matching when applying the filter. After
        calling this method, the :ref:`pysast.FileFilter.apply` method will use regular expressions
        to match files against the filter criteria.
        """
        self._use_re = True

    def apply(self, value: str, target: str) -> bool:
        """Apply the filter to a target value.

        This method applies the filter to the target value and determines whether it matches the filter criteria.


        :param value: The filter criteria. It can contain multiple values separated by commas.
        :type value: str
        :param target: The target value to match against the filter.
        :type target: str
        :return: True if the target value matches the filter criteria, False otherwise.
        :rtype: bool
        """
        matches = False
        for item in [x.strip() for x in value.strip().split(",")]:
            if self._use_re:
                matches = matches or re.search(item, target, re.IGNORECASE)
            else:
                matches = matches or item.lower() in target.lower()

        return (self._inverted and matches) or (not self._inverted and not matches)


class SupportsFilter:
    """A mixin class for supporting filtering based on predefined criteria.

    The ``SupportsFilter`` class provides a method for applying filters to a file
    based on various criteria such as file extension, file name, full path, and MIME
    type. It utilizes the :class:`FileFilter` class for applying individual filters.

    Usage:
    ~~~~~~

        >>> instance = SupportsFilter()
        >>> result = instance.apply_filters(
        ...     filters={"file_ext": "jpg", "file_name": "image", "mime_type": "image/jpeg"},
        ...     file_path="/path/to/image.jpg",
        ...     mime_type="image/jpeg"
        ... )

    You can also pass spacial directives to filter values:

    - ``!`` inverts the filter logic.
    - ``re:`` will treat the following string as a regular expression
    """

    def apply_filters(
        self, filters: dict[str, str], file_path: str, mime_type: str
    ) -> bool:
        """Apply filters to a file based on predefined criteria.

        This method iterates through the ``filters`` dictionary and applies the
        filters to the ``file_path`` and ``mime_type`` values. It uses the
        :class:`FileFilter` class to apply individual filters based on predefined
        criteria. If any filter fails, it returns False. If all filters pass, it
        returns True.

        :param filters: A dictionary of filters, where the keys are filter directives and the values
                are corresponding filter criteria.
        :type filters: dict[str, str]
        :param file_path: The path of the file to be filtered.
        :type file_path: str
        :param mime_type: The MIME type of the file.
        :type mime_type: str
        :return: True if the file passes all filters, False otherwise.
        :rtype: bool
        """
        file_filter = FileFilter()
        for key, value in filters.items():
            file_filter.reset()
            if value.startswith("!"):
                # Invert the filter logic
                file_filter = ~file_filter
                value = value[1:]

            if value.startswith("re:"):
                # Enable regular expression matching
                file_filter.with_re()
                value = value[3:]

            if key.lower() == FILTER_FILE_EXT:
                target = "" if "." not in file_path else file_path.split(".")[-1]
            elif key.lower() == FILTER_FILE_NAME:
                target = os.path.basename(file_path)  # Extract file name
            elif key.lower() == FILTER_FULL_PATH:
                target = file_path
            elif key.lower() == FILTER_MIME_TYPE:
                target = mime_type
            else:
                logger.warning("Invalid filter directive: %s", key)
                continue  # Skip invalid filter directives

            # Apply the filter and check if it fails
            if not file_filter.apply(value, target):
                return False
        return True


class SastPattern:
    """A class representing a static application security testing (SAST) pattern.

    The ``SastPattern`` class encapsulates a pattern used for SAST matching. It provides
    functionality to compile the pattern using a specified regular expression engine and
    supports different modes of pattern matching.

    .. note::
        All patterns will be converted to byte-patterns before compilation.

    Each pattern can use a different compile engine that produces a ``re.Pattern``. To
    specify a custom engine, use the ``"engine"`` directive in a pattern declaration within
    a rule:

    .. code-block:: json
        :linenos:

        "rule-id": {
            "pattern": {
                "text": "...",
                "engine": "mymodule"
            }
        }

    or with YAML:

    .. code-block:: yaml

        - rule-id: ...
          pattern:
            text: ...
            engine: mymodule

    To apply custom pattern matching you can specify whether the pattern is optional or the
    matching logic should be inverted. You can do that by adding the ``"mode"`` directive,
    which can take the following values:

    - ``and`` (*default*): The default setting implies that the pattern **must** be found in a file
    - ``or``: The pattern is optional and **may** occur in the scanned file
    - ``not``: The matching logic will be inverted so that the pattern **must not** be found

    .. hint::
        You can use multiple modes separated with a ``+``:

        .. code-block:: yaml

            - rule-id: sample-rule
              pattern:
                text: ...
                mode: not+and
    """

    text: str
    """The text pattern to be compiled. Defaults to None."""

    engine: str
    """The regular expression engine to be used for pattern compilation. Defaults to ``"re"``."""

    modes: list
    """Additional modes to be applied for pattern matching. Defaults to ``["and"]``."""

    re_pattern: re.Pattern

    def __init__(self, text=None, engine=None, mode=None, modes=None) -> None:
        self.text = text
        self.engine = engine or DEFAULT_PATTERN_ENGINE
        self.modes = []
        if mode:
            self.modes.append(mode)
        if modes and isinstance(modes, str):
            self.modes.extend(modes.split("+"))
        elif modes and isinstance(modes, list):
            self.modes.extend(modes)

        # "and" will be added by default
        if not self.modes or ("or" not in self.modes and "and" not in self.modes):
            self.modes.append("and")

        self.re_pattern = None
        # Check if 'and' mode is specified. The pattern must be found in a
        # file if "and" is specified.
        self.required = "and" in self.modes

        # Check if 'not' mode is specified - this will invert the logic
        # that will be applied at the end of a scan.
        self.inverted = "not" in self.modes
        self.compile()

    def compile(self):
        """Compile the pattern using the specified regular expression engine.

        This method compiles the pattern using the regular expression engine specified
        in ``self.engine``. It handles potential errors during module import and checks
        if the target module has the `compile()` function. By default, the built-in
        module ``re`` is used.
        """
        try:
            mod = importlib.import_module(self.engine)
        except Exception as err:
            # Use the default 're' module if import fails
            mod = re
            logger.warning("Could not import module: %s, %s", self.engine, str(err))

        # Check if the module has the 'compile()' function, otherwise
        # use the default module "re" again
        if not hasattr(mod, "compile"):
            mod = re
            logger.warning("Target module has not compile() function: %s", self.engine)

        # Compilation errors should be visible to the user
        self.re_pattern = mod.compile(self.text.encode(errors="replace"))


class SastRule(SupportsFilter):
    """A class to describe a single SAST rule.

    It extends the :class:`SupportsFilter` class. The purpose of this class is
    to encapsulate a rule with its associated content, filters, and patterns. It
    also provides methods to add patterns and reset its internal state.

    :param rule_id: The ID of the rule.
    :type rule_id: str
    :param rule_content: The content of the rule.
    :type rule_content: dict
    :ivar filters: A dictionary of filter directives
    :type filters: dict
    :ivar patterns: A list of SAST patterns.
    :type patterns: list[:class:`SastPatterns`]
    """

    def __init__(self, rule_id: str, rule_content: dict) -> None:
        self.rule_id = rule_id
        self.rule_content = rule_content
        self.filters = {}
        self.patterns = []

        # Filters are optional so we don't have to use them
        if "filter" in self.rule_content.get("meta", {}):
            self.filters = extract_filter_keys(self.rule_content["meta"], is_meta=True)

        # Patterns can be declared as pure string with default filter mode "and"
        # and can be defined in two ways:
        # 1. Single pattern: Use the "pattern" attribute to define a single pattern
        if "pattern" in self.rule_content:
            pattern = self.rule_content["pattern"]
            self.add_pattern(pattern)

        # 2. Pattern group: Use "patterns" with a list to store additional patterns.
        # Note that these patterns will be added two existing patterns.
        if "patterns" in self.rule_content:
            for pattern in self.rule_content["patterns"]:
                self.add_pattern(pattern)

        # :private: used within a file scan
        self._lines = []
        self._positions = []
        self._pattern_matches = []
        self._matches = []

    def __str__(self) -> str:
        """Returns a string representation of a SastRule object.

        :return: A string representation of this object.
        :rtype: str
        """
        return f"<SastRule id='{self.rule_id}'>"

    def add_pattern(self, pattern: str | dict[str, str]):
        """Adds a pattern to this rule.

        .. note::
            You can use either a regular expression string or a custom object that
            contains special attributes as defined in :class:`SastRule`.

        :param pattern: The pattern to add.
        :type pattern: dict[str, str] | str
        """
        if isinstance(pattern, str):
            self.patterns.append(SastPattern(text=pattern))
        else:
            self.patterns.append(SastPattern(**pattern))

    def reset(self) -> None:
        """Resets the internal state of the ``SastRule`` object."""
        self._lines.clear()
        self._positions.clear()
        self._pattern_matches.clear()
        self._matches.clear()

    @property
    def meta(self) -> dict[str, str | dict]:
        """Returns the meta information of this rule

        :return: meta information like severity or description
        :rtype: dict[str, str | dict]
        """
        return self.rule_content.get("meta", {})

    @property
    def must_not_patterns(self) -> list[SastPattern]:
        """Get a list of patterns that must not match for this rule.

        :return: A list of patterns that must not match for this rule.
        :rtype: list[SastPattern]
        """
        return list(
            filter(lambda x: "not" in x.modes and "or" not in x.modes, self.patterns)
        )

    @property
    def required_patterns(self) -> list[SastPattern]:
        """Get a list of patterns that are required to match for this rule.

        :return: A list of patterns that are required to match for this rule.
        :rtype: list[SastPattern]
        """
        return list(filter(lambda x: "and" in x.modes, self.patterns))

    def create_result(self, file_path: str) -> dict:
        """Create a result dictionary for the rule.

        If the rule does not have any matches (``self.has_match`` is False), an empty
        dictionary is returned. Otherwise, a dictionary is created with keys such as

            - ``RESULT_KEY_RULE_ID`` (``rule-id``),
            - ``RESULT_KEY_ABS_PATH`` (``abs_path``),
            - ``RESULT_KEY_LINES`` (``lines``),
            - ``RESULT_KEY_META`` (``meta``),
            - ``RESULT_KEY_POSITIONS`` (``positions``), and
            - ``RESULT_KEY_MATCHES`` (``matches``).

        The values are populated from the respective attributes and content of the
        `:class:`SastRule` object. The resulting dictionary represents the rule result.

        :param file_path: the file path that was scanned
        :type file_path: str
        :return: the result object
        :rtype: dict
        """
        if not self.has_match:
            return {}

        return {
            RESULT_KEY_RULE_ID: self.rule_id,
            RESULT_KEY_ABS_PATH: file_path,
            RESULT_KEY_LINES: self._lines,
            RESULT_KEY_META: self.rule_content.get("meta", {}),
            RESULT_KEY_POSITIONS: self._positions,
            RESULT_KEY_MATCHES: self._matches,
        }

    @property
    def has_match(self) -> bool:
        """Check if the rule has any matches.

        :return: True if the rule has matches, False otherwise.
        :rtype: bool
        """
        #  If a "must not" pattern has a match, it means the rule does not
        # have a match, and False is returned. ("must not" with "or" are optional)
        for pattern in self.must_not_patterns:
            if pattern in self._pattern_matches:
                return False

        # If any of the required patterns don't have a match, it also indicates
        # that the rule does not have a match, and False is returned.
        for pattern in self.required_patterns:
            if pattern not in self._pattern_matches:
                return False

        return len(self._pattern_matches) > 0

    def search(self, line: bytes, line_index: int, abs_offset: int):
        """Search for matches of the rule's patterns in a given line.

        Before searching for matches, the method checks if a transformation is
        specified in the rule's content using the ``"input"``. If the transformation
        is not ``"default"`` and the line object has an attribute with the same name
        as the transformation, the method applies the transformation to the line using
        the ``getattr`` function.

        The method then iterates through the patterns defined in the ``patterns`` list
        and performs a regular expression search using ``re.search``. If a match is
        found (result is not None), the method performs the following actions:

            - Appends the ``line_index`` to the ``_lines`` list to keep track of the line index associated with the match.
            - Calculates the start position of the match using ``.span()`` and appends the corresponding absolute offset to the ``_positions`` list.
            - If the pattern is not already present in the ``_pattern_matches`` list, it appends the pattern to keep track of which patterns have matches.
            - Appends the match to the ``_matches`` list as a decoded string

        .. note::
            It's important to note that this method modifies the internal state of the
            :class:`SastRule` object by appending information to the ``_lines``,
            ``_positions``, ``_pattern_matches``, and ``_matches`` lists.

        :param line: The line to search for matches (as bytes).
        :type line: bytes
        :param line_index: The index of the line.
        :type line_index: int
        :param abs_offset: The absolute offset of the line.
        :type abs_offset: int
        """
        transform = self.rule_content.get("input", "default")
        if transform != "default" and hasattr(line, transform):
            line = getattr(line, transform)()

        for pattern in self.patterns:
            result = re.search(pattern.re_pattern, line)

            if result:
                self._lines.append(line_index)
                start, _ = result.span()
                self._positions.append(abs_offset + (start or 1))
                if pattern not in self._pattern_matches:
                    self._pattern_matches.append(pattern)

                self._matches.append(result.group().decode(errors="replace"))


class SastContext:
    """Represents the context for performing a SAST scan on a given file.

    It manages a collection of :class:`SastRule` objects and provides methods
    to match the rules against file contents and generate results.

    :param sast_rules:  A list of SastRule objects representing the SAST rules
                            to be applied in the context. If not provided, an empty
                            list is assigned as the default value.
    :type sast_rules: list[SastRule]
    """

    def __init__(self, sast_rules: list[SastRule]) -> None:
        self.sast_rules = sast_rules or []

    def _pool_lines(self, fp) -> Generator[tuple[bytes, int, int], Any, None]:
        """
        A private method that pools lines from a file object and yields each line
        along with its line index and absolute offset.
        """
        line_index = 1
        abs_offset = 1
        for line in iter(lambda: fp.readline(), b""):
            yield line, line_index, abs_offset
            line_index += 1
            abs_offset += len(line)

    def match(self, file_path: str) -> list[dict]:
        """Matches the SAST rules against the contents of a file and returns the results.

        :param file_path: A string representing the path to the file to be analyzed.
        :type file_path: str
        :return: A list of dictionaries representing the results of rule matches.
        :rtype: list[dict]
        """
        result = []
        try:
            # Open the specified file in binary mode and handle any OSError. If
            # an error occurs, it will be logged with a warning message and
            # directly return an empty result list.
            fp = open(file_path, "rb")
        except OSError as err:
            logger.warning(
                "(%s) Could not open file %s due to error: %s",
                type(err).__name__,
                file_path,
                str(err),
            )
            return result

        for line, line_index, offset in self._pool_lines(fp):
            for rule in self.sast_rules:
                rule.search(line, line_index, offset)

        fp.close()
        for rule in self.sast_rules:
            rule_result = rule.create_result(file_path)
            if rule_result:
                result.append(rule_result)

        return result


class SastScanner(SupportsFilter):
    """
    A class representing a static application security scanner.

    :param rules_dir: Optional. Path to a directory containing SAST rule files.
    :type rules_dir: str
    :param rules_path: Optional. Path to a specific SAST rule file.
    :type rules_path: str
    :param rules: Optional. A list of SastRule objects to be loaded.
    :type rules: list[SastRule]
    :param recursive_dir: Optional. Specifies whether to recursively scan rule
                          files in a directory. Default is False.
    :type recursive_dir: bool
    :param disable_prefilter: Optional. Specifies whether to disable pre-filtering
                              of rules. Default is False.
    :type disable_prefilter: bool
    :param disable_postfilter: Optional. Specifies whether to disable post-filtering
                               of scan results. Default is True.
    :type disable_postfilter: bool
    :param max_bytes: Optional. Maximum number of bytes to read from a file during
                      scanning. Default is ``DEFAULT_MAX_BYTES``.
    :type max_bytes: int
    """

    def __init__(
        self,
        rules_dir: str = None,
        rules_path: str = None,
        rules: list[SastRule] = None,
        recursive_dir: bool = False,
        disable_prefilter: bool = False,
        disable_postfilter: bool = True,
        max_bytes=DEFAULT_MAX_BYTES,
    ) -> None:
        super().__init__()
        self._scan_results = []
        self._rules = []

        self.max_bytes = max_bytes
        self.disable_prefilter = disable_prefilter
        self.disable_postfilter = disable_postfilter

        if rules_dir is not None:
            self.load_rule_directory(rules_dir, recursive_dir)
        if rules_path is not None:
            self.load_rule_file(rules_path)
        if rules is not None:
            self.rules.extend(rules)

    def load_rule_directory(self, dir_path: str, recursive: bool) -> None:
        """Load SAST rule files from a directory.

        :param dir_path: Path to the directory containing the rule files.
        :type dir_path: str
        :param recursive: Specifies whether to recursively scan rule files in subdirectories.
        :type recursive: bool
        """
        for file in pathlib.Path(dir_path).glob("**/*.*" if recursive else "*.*"):
            if not is_rule_file(str(file)):
                continue

            self.rules.extend(load_sast_rules(file))

    def load_rule_file(self, file_path: str) -> None:
        """Load a specific SAST rule file.

        :param file_path: Path to the rule file.
        :type file_path: str
        """
        if is_rule_file(file_path):
            self.rules.extend(load_sast_rules(file_path))

    @property
    def rules(self) -> list[SastRule]:
        """Get the loaded SAST rules."""
        return self._rules

    @property
    def scan_results(self) -> list:
        """Get the scan results as a list."""
        return self._scan_results

    @scan_results.setter
    def scan_results(self, value):
        """Set the scan results.

        :param value: The scan results to be set.
        :type value: list
        """
        self._scan_results = value

    @property
    def has_matches(self) -> bool:
        """Check if there are any scan results.

        :return: True if there are scan results, False otherwise.
        :rtype: bool
        """
        return len(self._scan_results) != 0

    @property
    def json(self) -> str:
        """Get the scan results in JSON format.

        :return: A string representing the scan results in JSON format.
        """
        return json.dumps(self.scan_results)

    def get_context(self, file_path: str, mime_type: str) -> SastContext:
        """Get the :class:`SastContext` object for the specified file.

        :param file_path: Path to the file to be scanned.
        :type file_path: str
        :param mime_type: MIME type of the file.
        :type mime_type: str
        :return: the newly created context
        :rtype: :class:`SastContext`
        """
        filtered_sast_rules = []
        for rule in self.rules:
            if file_path and not self.disable_prefilter:
                if rule.apply_filters(rule.filters, file_path, mime_type):
                    filtered_sast_rules.append(rule)
                    rule.reset()
            else:
                # include all rules
                filtered_sast_rules.append(rule)
                rule.reset()

        return SastContext(filtered_sast_rules)

    def scan(self, file_path: str) -> bool:
        """Perform the scanning process on the specified file.

        :param file_path: the file to be scanned
        :type file_path: str
        :return: whether there are any scan results
        :rtype: bool
        """
        mime_type = get_mime_type(file_path)
        logger.debug(f"Got mime-type {mime_type} for {file_path}")

        if os.path.getsize(file_path) > self.max_bytes:
            logger.warning("File too large - skipping '%s'", file_path)
            return self.has_matches

        context = self.get_context(file_path, mime_type)
        start = datetime.datetime.now()
        results = context.match(file_path)
        end = datetime.datetime.now()
        logger.info(
            "Scanned file %s in %d ms",
            file_path,
            int((end - start).total_seconds() * 1000),
        )

        return self.filter_scan_results(file_path, mime_type, results)

    def filter_scan_results(
        self, file_path: str, mime_type: str, sast_matches: list
    ) -> bool:
        """Filter the scan results based on the specified file path, MIME type, and SAST matches.

        :param file_path: the scanned file path
        :type file_path: str
        :param mime_type: MIME type of the scanned file
        :type mime_type: str
        :param sast_matches: a list of matches
        :type sast_matches: list
        :return: True if there are scan results, False otherwise.
        :rtype: bool
        """
        self.scan_results = []

        if self.disable_postfilter:
            self.scan_results.extend(sast_matches)
        else:
            for result in sast_matches:
                if self.apply_filters(
                    extract_filter_keys(result["meta"], is_meta=True),
                    file_path,
                    mime_type,
                ):
                    self.scan_results.append(result)

        return self.has_matches


def load_sast_rules(file_path: str) -> list[SastRule]:
    """Loads SAST (Static Application Security Testing) rules from a file.

    The method takes a file path as input and returns a list of :class:`SastRule`
    objects. The file can be in either JSON or YAML format.

    Example:
    >>> rules = load_sast_rules("sast_rules.json")
    >>> for rule in rules:
    ...     print(rule.rule_id, rule.meta["severity"])
    example-rule INFO

    :param file_path: The path to the file containing the SAST rules.
    :type file_path: str
    :return: A list of :class:`SastRule` objects representing the loaded rules.
    :rtype: list[:class:`SastRule`]
    """
    path_obj = pathlib.Path(file_path)
    if not path_obj.exists():
        return []

    result = []
    if path_obj.name.endswith(".json"):
        with open(str(file_path), "rb") as docfp:
            document = json.load(docfp)
            for rule_id in document:
                result.append(SastRule(rule_id, document[rule_id]))

    elif path_obj.name.endswith((".yml", ".yaml")):
        with open(str(file_path), "rb") as docfp:
            document = yaml.load(docfp, yaml.SafeLoader)
            result = [SastRule(x.pop("rule-id"), x) for x in document]

    return result


def run(cmd: list[str] = None):
    """Runs a scan by using the incoming command line arguments.

    :param cmd: the command to execute, defaults to None
    :type cmd: str, optional
    """
    import argparse
    import pprint

    parser = argparse.ArgumentParser(
        description="Scan the given file with SAST scanner using all available rules."
    )
    parser.add_argument(
        "paths",
        metavar="PATHS",
        nargs="*",
        help="One or more files or directories to scan.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        required=False,
        default=False,
        action="store_true",
        help="Scan target directories recursively",
    )
    parser.add_argument(
        "-j",
        "--json",
        required=False,
        default=False,
        action="store_true",
        dest="dump_json",
        help="Dump JSON output instead of pprint.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Specifies the verbosity for the next scan. Use -vvv for more verbose output.",
    )
    parser.add_argument(
        "-s",
        "--sast-rule",
        required=False,
        default=[],
        action="append",
        dest="sast_rules",
        help="File path(s) to SAST rules to import. (Use -S for directories)",
    )
    parser.add_argument(
        "-S",
        "--sast-dir",
        required=False,
        default=[],
        action="append",
        dest="sast_dirs",
        help="One or more directories that store SAST rules. (Use -rS for recursive search)",
    )
    parser.add_argument(
        "-rS",
        "--recursive-sast-dir",
        required=False,
        default=False,
        action="store_true",
        dest="recursive_sast_dir",
        help="Load rules from target directories recursively",
    )
    parser.add_argument(
        "--disable-prefilter",
        dest="disable_prefilter",
        action="store_true",
        default=False,
        help="Disable prefiltering rules.",
    )
    parser.add_argument(
        "--enable-postfilter",
        dest="enable_postfilter",
        action="store_true",
        default=False,
        help="Enable postfiltering.",
    )
    parser.add_argument(
        "-M",
        "--max-bytes",
        default=DEFAULT_MAX_BYTES,
        type=int,
        help="Skip files exteeding a the amount of maximum bytes.",
    )

    args = parser.parse_args(cmd)

    # Setup logging
    log_levels = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
    }
    log_level = min(3, max(args.verbose, 0))
    logging.basicConfig(level=log_levels[log_level])

    if len(args.sast_rules) == 0 and len(args.sast_dirs) == 0:
        logger.error("Please specify at least one rule file or rule directory!")
        sys.exit(1)

    scanner = SastScanner(
        max_bytes=args.max_bytes,
        disable_postfilter=not args.enable_postfilter,
        disable_prefilter=args.disable_prefilter,
    )

    for file_path in args.sast_rules:
        scanner.load_rule_file(file_path)

    for dir_path in args.sast_dirs:
        scanner.load_rule_directory(dir_path, args.recursive_sast_dir)

    def pprint_match(match: dict, intent: str):
        print(intent, "+ match:%s (%s)"
            % (
                match[RESULT_KEY_RULE_ID],
                match[RESULT_KEY_META].get("severity", "None"),
            )
        )
        print(intent * 3, "Title:", match[RESULT_KEY_META].get("title", "No Title"))
        print(intent * 3, "Description", match[RESULT_KEY_META].get("description", "<>"))
        print(intent * 3, "Lines:", pprint.pformat(match[RESULT_KEY_LINES], compact=True))
        print(intent * 3,"Offsets:",pprint.pformat(match[RESULT_KEY_POSITIONS], compact=True))
        print(intent * 3, "Meta:", pprint.pformat(match[RESULT_KEY_META]), "\n")

    def scan_file(file_path: str) -> bool:
        try:
            if scanner.scan(file_path):
                if args.dump_json:
                    json.dump(
                        scanner.scan_results, sys.stdout, sort_keys=True, indent=4
                    )
                else:
                    print("+ file:", file_path)
                    for match in scanner.scan_results:
                        pprint_match(match, " ")
                return True

        except Exception as err:
            logger.exception("(%s) Scan failed for %s:", type(err).__name__, file_path)
            return False

    def scan_dir(dir_path: str) -> bool:
        for file_path in pathlib.Path(dir_path).iterdir():
            if file_path.is_dir() and args.recursive:
                scan_dir(str(file_path))
            else:
                scan_file(str(file_path))

    for path in args.paths:
        if os.path.isdir(path):
            scan_dir(path)
        else:
            if not scan_file(path):
                sys.exit(1)


if __name__ == "__main__":
    run()
