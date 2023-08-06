from datetime import datetime, timezone

from json_log_viewer.logs.log import JsonLog, LogLevel


def test_from_dict():
    log = JsonLog.fromDict(
        **dict(
            source="source",
            level="INFO",
            message="test message",
            timestamp="2023-05-20T17:28:25.038Z",
            value=1,
            other=2,
        )
    )
    assert log.source == "source"
    assert log.level == LogLevel.INFO
    assert log.message == "test message"
    assert log.timestamp == datetime(
        2023, 5, 20, 17, 28, 25, 38000, tzinfo=timezone.utc
    )
    assert log.extra == dict(value=1, other=2)
