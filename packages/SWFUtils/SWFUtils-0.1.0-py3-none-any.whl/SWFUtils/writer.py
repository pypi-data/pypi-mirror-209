class Writer:
    """
    A class for writing a Workload instance to a file.

    Parameters
    ----------
    filepath : str
        The path to the output file.
    workload : Workload
        The Workload instance to write.

    Attributes
    ----------
    filepath : str
        The path to the output file.
    workload : Workload
        The Workload instance to write.

    Methods
    -------
    write():
        Writes the Workload instance to the output file.
    """

    def __init__(self, filepath, workload):
        """
        Initializes a Writer instance.

        Parameters
        ----------
        filepath : str
            The path to the output file.
        workload : Workload
            The Workload instance to write.
        """
        self.filepath = filepath
        self.workload = workload

    def write(self):
        """
        Writes the Workload instance to the output file following the standard workload format.
        """
        if not bool(self.workload.meta) or self.workload.jobs.empty:
            raise ValueError("Cannot write empty Workload instance.")
        else:
            with open(self.filepath, 'w') as f:
                # Write metadata
                for key, value in self.workload.meta.items():
                    f.write(f"; {key}: {value}\n")
                
                # Write jobs
                self.workload.jobs.to_csv(f, sep=' ', index=False, header=False)
