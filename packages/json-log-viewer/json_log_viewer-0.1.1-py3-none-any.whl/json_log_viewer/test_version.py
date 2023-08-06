from pathlib import Path
from tomllib import load

from json_log_viewer.__main__ import VERSION


def test_correct_version():
    pyproject = Path(__file__).parent.parent / "pyproject.toml"
    with pyproject.open("rb") as fp:
        pyproject = load(fp)
    assert pyproject["tool"]["poetry"]["version"] == VERSION
