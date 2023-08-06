import os
import pytest
from SWFUtils.reader import Reader

@pytest.fixture
def reader():
    test_file_path = os.path.join(os.path.dirname(__file__), "data/dummy_workload.swf")
    return Reader(test_file_path)

@pytest.fixture
def expected_meta():
    return {
        'UnixStartTime': 1609459200,
        'TimeZoneString': 'Europe/London',
        'MaxJobs': 15,
        'MaxProcs': 4,
        'MaxNodes': 4,
    }

def test_reader_init(reader):
    test_file_path = os.path.join(os.path.dirname(__file__), "data/dummy_workload.swf")
    assert reader.filepath == test_file_path

def test_reader_parse_comments(reader, expected_meta):
    comments = reader._parse_comments()
    assert comments == expected_meta

def test_reader_read(reader, expected_meta):
    workload = reader.read()
    assert workload.meta == expected_meta
    assert workload.jobs.shape == (expected_meta['MaxJobs'], 18)