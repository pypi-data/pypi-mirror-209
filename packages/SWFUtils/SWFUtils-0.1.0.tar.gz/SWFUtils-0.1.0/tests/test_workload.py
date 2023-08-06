import pandas as pd
import pytest
from SWFUtils.workload import Workload

@pytest.fixture
def empty_workload():
    return Workload()

@pytest.fixture
def metadata():
    return {"MaxJobs": 3, "MaxProcs": 2, "MaxNodes": 2}

@pytest.fixture
def jobs():
    return pd.DataFrame({"job_number": [1, 2, 3], "submit_time": [0, 1, 2], "run_time": [10, 200, 30], "num_processors": [1, 2, 1]})

@pytest.fixture
def populated_workload(metadata, jobs):
    workload = Workload()
    workload.populate(metadata, jobs)
    return workload

def test_workload_init(empty_workload):
    assert empty_workload.meta == {}
    assert empty_workload.jobs.empty

def test_workload_populate(empty_workload, metadata, jobs):
    empty_workload.populate(metadata, jobs)
    assert empty_workload.meta == metadata
    assert empty_workload.jobs.equals(jobs)

def test_workload_populate_nonempty(populated_workload, metadata, jobs):
    with pytest.raises(ValueError):
        populated_workload.populate(metadata, jobs)