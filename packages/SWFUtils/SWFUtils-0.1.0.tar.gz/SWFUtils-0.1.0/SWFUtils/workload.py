import pandas as pd

class Workload:
    """
    A class to represent a workload of jobs.

    Attributes
    ----------
    meta : dict
        A dictionary containing specific metadata about the workload.
    jobs : pandas.DataFrame
        A DataFrame containing the job data.
    """

    def __init__(self):
        """
        Initializes a new Workload object.
        """
        self.meta = {}
        self.jobs = pd.DataFrame()

    def populate(self, metadata, jobs):
        """
        Populates the Workload object with data.

        Parameters
        ----------
        metadata : dict
            A dictionary containing specific metadata about the workload.
        jobs : pandas.DataFrame
            A DataFrame containing the job data.
        
        Raises
        ------
        ValueError
            If the Workload object is not empty.
        """
        if bool(self.meta) or not self.jobs.empty:
            raise ValueError("Cannot populate non-empty Workload instance.")
        else:
            self.meta = metadata
            self.jobs = jobs