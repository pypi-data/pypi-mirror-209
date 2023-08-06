import os
import pytest
from SWFUtils.reader import Reader
from SWFUtils.writer import Writer
from SWFUtils.workload import Workload

@pytest.fixture
def output_file_path():
    return os.path.join(os.path.dirname(__file__), "data/test_output_workload.swf")

@pytest.fixture
def empty_workload():
    return Workload()

@pytest.fixture
def dummy_workload():
    input_file_path = os.path.join(os.path.dirname(__file__), "data/dummy_workload.swf")
    reader = Reader(input_file_path)
    workload = reader.read()
    return workload

@pytest.fixture
def writer(output_file_path, dummy_workload):
    return Writer(output_file_path, dummy_workload)

def test_writer_write(writer, dummy_workload, output_file_path):
    writer.write()

    # Read the output file and validate
    reader = Reader(output_file_path)
    output_workload = reader.read()

    # Ensure the metadata and jobs match
    assert output_workload.meta == dummy_workload.meta
    assert output_workload.jobs.equals(dummy_workload.jobs)

    # Clean up the test output file
    os.remove(output_file_path)

def test_writer_with_empty_workload(output_file_path, empty_workload):
    writer = Writer(output_file_path, empty_workload)

    with pytest.raises(ValueError):
        writer.write()
