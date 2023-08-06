# PySAST

[![python](https://img.shields.io/badge/python-3.8+-blue.svg?logo=python&labelColor=lightgrey)](https://www.python.org/downloads/)
![Status](https://img.shields.io:/static/v1?label=Status&message=Alpha-Release&color=lightgreen)
![Platform](https://img.shields.io:/static/v1?label=Platforms&message=All&color=yellowgreen)
![PyPi](https://img.shields.io:/static/v1?label=PyPi&message=1.1.3-alpha&color=lightblue)
![Codestyle](https://img.shields.io:/static/v1?label=Codestyle&message=black&color=black)

Welcome to `pysast` - a powerful Python package designed for scanning one or multiple files using customizable rules written
in JSON or YAML. This package allows you to automate the process of code analysis and identify potential issues or violations
based on your specified criteria.

By utilizing the rule-based system, you can define a set of rules that reflect your desired coding standards, best practices,
or specific requirements. The package then scans your files, identifies instances that violate the defined rules, and reports
them to help you maintain a high code quality.

You can install pysast using pip, the Python package installer. Simply run the following command:

## Installation

```shell
pip install pysast
```

Once installed, you're ready to start using pysast for your code analysis needs.

## Documentation

For more detailed information on using pysast, please refer to the [official documentation](https://matrixeditor.github.io/pysast/) on Github.

## Getting Started

Before you begin using `pysast`, it's recommended to familiarize yourself with the package's functionality and usage. The following steps will guide you through the essential setup and running your first code scan:

1. [Rule Definition](https://matrixeditor.github.io/pysast/intro/sast_rules.html): Learn how to define rules in JSON or YAML format to specify the analysis criteria for your codebase.
2. [Running Scans](https://matrixeditor.github.io/pysast/intro/sast_scans.html): Explore how to execute pysast to scan your files and generate detailed reports.
3. [Advanced Usage](https://matrixeditor.github.io/pysast/api/index.html): Dive deeper into the advanced features and options offered by pysast to enhance your code analysis capabilities.

By following these steps, you'll be equipped with the knowledge and tools to effectively utilize `pysast` in your projects.

## Optimization

Since version ``1.1.0`` this program introduces an optimization feature that significantly
improves its performance by leveraging threading. By utilizing the ``--threading`` option
on the command line, you can enable this optimization to take full advantage of your
system's resources.

## CLI Options

    usage: pysast.py [-h] [-r] [-j] [-v] [-s SAST_RULES] [-S SAST_DIRS] [-rS RECURSIVE_SAST_DIRS] [--disable-prefilter] [--enable-postfilter] [-M MAX_BYTES] [-T] [-e EXCLUDE_FILES] [--threading] [PATHS ...]

    Scan the given file with SAST scanner using all available rules.

    positional arguments:
    PATHS                 One or more files or directories to scan.

    options:
    -h, --help            show this help message and exit
    -r, --recursive       Scan target directories recursively
    -j, --json            Dump JSON output instead of pprint.
    -v, --verbose         Specifies the verbosity for the next scan. Use -vvv for more verbose output.
    -s SAST_RULES, --sast-rule SAST_RULES
                            File path(s) to SAST rules to import. (Use -S for directories)
    -S SAST_DIRS, --sast-dir SAST_DIRS
                            One or more directories that store SAST rules. (Use -rS for recursive search) The current directory is used if no rules are specified.
    -rS RECURSIVE_SAST_DIRS, --recursive-sast-dir RECURSIVE_SAST_DIRS
                            Load rules from target directories recursively
    --disable-prefilter   Disable prefiltering rules.
    --enable-postfilter   Enable postfiltering.
    -M MAX_BYTES, --max-bytes MAX_BYTES
                            Skip files exteeding a the amount of maximum bytes.
    -T, --disable-mime, -T, --disable-mime
                            Specifies whether the scanner should use the 'file' utility to retrieve the MIME-type of a file. (enabled as per default)
    -e EXCLUDE_FILES, --exclude-file EXCLUDE_FILES
                            Specifies exclusion files (use re: for regular expressions)
    --threading           Activates threading for file processing. (Can't be used on daemon processes)

## Contributing

We welcome contributions from the community! If you'd like to contribute to `pysast`, please refer to the contribution guidelines.

## Support

If you encounter any issues or have any questions or suggestions, please feel free to open an issue.

## License

This project is licensed under the GNU GPLv3.