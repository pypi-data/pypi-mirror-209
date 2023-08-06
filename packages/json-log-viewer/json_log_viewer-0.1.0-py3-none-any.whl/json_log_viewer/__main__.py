"""JSON Log Viewer.

Usage:
  jlv <file>...

Options:
  -h --help   Show this screen.
  --version   Show version.

"""
from pathlib import Path

from docopt import docopt

from json_log_viewer.extractor.extract import extract_from_file
from json_log_viewer.logs.log import JsonLog
from json_log_viewer.logs.tree import TreeApp

VERSION = "0.1.0"


def main(files: list[str]):
    json_logs: list[JsonLog] = []
    for f in files:
        path = Path(f)
        raw_logs = extract_from_file(path)
        json_logs.extend(JsonLog.fromDict(source=path.name, **log) for log in raw_logs)

    app = TreeApp(sorted(json_logs))
    app.run()


def run():
    arguments = docopt(__doc__, version=f"jlv {VERSION}")
    main(arguments["<file>"])


if __name__ == "__main__":
    run()
