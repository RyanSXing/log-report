import json
from pathlib import Path

REPORT = Path("/app/report.json")


def read_report():
    return json.loads(REPORT.read_text())


def test_report_is_expected_json_object():
    """Success criterion 1: the output is JSON with exactly the required keys."""
    report = read_report()
    assert type(report) is dict
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Success criterion 2: total_requests counts non-empty request lines."""
    assert read_report()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 3: unique_ips counts distinct client IP addresses."""
    assert read_report()["unique_ips"] == 3


def test_top_path():
    """Success criterion 4: top_path is the most frequently requested path."""
    assert read_report()["top_path"] == "/index.html"
