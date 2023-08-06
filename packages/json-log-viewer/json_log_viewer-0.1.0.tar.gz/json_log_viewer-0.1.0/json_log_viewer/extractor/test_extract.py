from json_log_viewer.extractor.extract import extract


def test_simple_single_line_json():
    json = extract(['{"test": 1}'])
    assert json == [dict(test=1)]


def test_simple_multiline_json():
    json = extract(["{", '  "test": 1', "}"])
    assert json == [dict(test=1)]


def test_nested_multiline_json():
    json = extract(["{", '  "l1": {', '    "l2": 1', "}", "}"])
    assert json == [dict(l1=dict(l2=1))]


def test_multiple_single_line_jsons():
    json = extract(['{"test": 1}', '{"test": 2}', '{"test": 3}'])
    assert json == [dict(test=1), dict(test=2), dict(test=3)]


def test_multiple_multiline_line_jsons():
    json = extract(
        ["{", '  "test": 1', "}", "{", '  "test": 2', "}", "{", '  "test": 3', "}"]
    )
    assert json == [dict(test=1), dict(test=2), dict(test=3)]


def test_simple_json_with_random_splits():
    json = extract(['{"', "te", 'st":', "1}"])
    assert json == [dict(test=1)]


def test_simple_single_line_json_with_ignorable_lines():
    json = extract(["ignore me", '{"test": 1}', "ignore me"])
    assert json == [dict(test=1)]
