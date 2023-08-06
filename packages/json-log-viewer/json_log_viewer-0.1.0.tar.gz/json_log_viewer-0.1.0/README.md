# JSON Log Viewer

A simple tool to extra JSON logs from files, merge them, and display them in an
easy-to-read format.

## Installation

```commandline
pip install XXX
```

## Usage

```commandline
jlv <FILE1> <FILE2>
```

## File Format

The script expects a file containing JSON objects, any other content will be ignored.

Each JSON object must contain the following fields:
- `level` a log level, any of `DEBUG`, `INFO`, `WARN` or `ERROR`
- `message` the log message
- `timestamp` the logs time stamp

Any additional fields are displayed as part of the log.
