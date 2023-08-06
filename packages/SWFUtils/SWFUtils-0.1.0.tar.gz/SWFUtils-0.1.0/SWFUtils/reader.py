import re
import pandas as pd
from .workload import Workload

class Reader:
    """
    A class to read SWF workload files.

    Attributes
    ----------
    filepath : str
        The path to the SWF workload file.

    Methods
    -------
    read():
        Reads the SWF workload file and returns a Workload object.
    """

    def __init__(self, filepath):
        """
        Parameters
        ----------
        filepath : str
            The path to the SWF workload file.
        """
        self.filepath = filepath

    def read(self):
        """
        Reads the SWF workload file and returns a Workload object.

        Returns
        -------
        Workload
            A Workload object containing the parsed data.
        """
        column_names = ["job_number", "submit_time", "wait_time", "run_time", "num_processors", 
                        "avg_cpu_time_used", "used_memory", "req_num_processors", "req_time", 
                        "req_memory", "status", "user_id", "group_id", "exec_number", 
                        "queue_number", "partition_number", "preceding_job_number", 
                        "think_time_from_preceding_job"]
        workload = Workload()
        workload.meta = self._parse_comments()
        workload.jobs = pd.read_csv(self.filepath, comment=';', delim_whitespace=True, 
                                    header=None, names=column_names)
        return workload

    def _parse_comments(self):
        """
        Parses the comments in the SWF workload file and returns a dictionary of metadata.

        Returns
        -------
        dict
            A dictionary containing the metadata parsed from the comments.
        """
        comments_data = {}

        # Define the patterns to look for
        patterns = {
            "UnixStartTime": re.compile(r"^;\s*UnixStartTime:\s*(\d+)\s*$"),
            "TimeZoneString": re.compile(r"^;\s*TimeZoneString:\s*([\w\/]+)\s*$"),
            "MaxJobs": re.compile(r"^;\s*MaxJobs:\s*(\d+)\s*$"),
            "MaxProcs": re.compile(r"^;\s*MaxProcs:\s*(\d+)\s*$"),
            "MaxNodes": re.compile(r"^;\s*MaxNodes:\s*(\d+)\s*$"),
        }

        # Map keys to their appropriate parser function
        parsers = {
            "UnixStartTime": int,
            "TimeZoneString": str,
            "MaxJobs": int,
            "MaxProcs": int,
            "MaxNodes": int,
        }

        with open(self.filepath, 'r') as f:
            for line in f:
                if line.startswith(';'):
                    for key, pattern in patterns.items():
                        match = pattern.match(line)
                        if match:
                            # Apply the appropriate parser function
                            comments_data[key] = parsers[key](match.group(1))
                else:
                    break

        return comments_data
