import sys
from json import loads, JSONDecodeError
from pathlib import Path
from typing import Iterator


def extract_from_file(path: Path) -> list[dict]:
    with path.open("r") as f:
        return extract(f)


def extract(lines: Iterator[str]) -> list[dict]:
    extracted_json = []

    json_blob = ""
    reading_json = False
    for line in lines:
        sline = line.strip()
        if not reading_json and sline.startswith("{"):
            reading_json = True
            json_blob = sline
            if sline.endswith("}"):
                try:
                    json = loads(json_blob)
                except JSONDecodeError:
                    pass
                else:
                    reading_json = False
                    extracted_json.append(json)
        elif reading_json and (sline.startswith("}") or sline.endswith("}")):
            json_blob += sline
            try:
                json = loads(json_blob)
            except JSONDecodeError:
                pass
            else:
                reading_json = False
                extracted_json.append(json)
        elif reading_json:
            json_blob += sline
        else:
            pass
    if reading_json and json_blob:
        print(f"Unconsumed JSON: {json_blob}", file=sys.stderr)
        raise RuntimeError("Failed to parse all JSON")
    return extracted_json
