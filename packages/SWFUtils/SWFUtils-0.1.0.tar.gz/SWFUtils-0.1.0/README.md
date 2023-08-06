# SWFUtils

> ⚠️ **Early Development Notice:** SWFUtils is currently in the early stages of development. Please be aware that significant changes may be made as development progresses. Feedback, suggestions, and contributions are very welcome during this time.

SWFUtils is a Python library for handling files in the [Standard Workload Format](https://www.cs.huji.ac.il/labs/parallel/workload/swf.html) (SWF). It provides utilities for reading, writing, and manipulating SWF files.

## Features

- Read SWF files into a convenient Python object.
- Write SWF data from Python objects to files.

## Usage

The following code snippet provides a quick guide on how to use `SWFUtils` to read, manipulate and write Standard Workload Format (SWF) files.

```python
import SWFUtils

# Create an instance of the Reader and read the file
reader = SWFUtils.Reader('path_to_your_input_file.swf')
input_workload = reader.read()

# The Workload object contains meta data and job data
metadata = input_workload.meta
jobs = input_workload.jobs

# Manipulate the data as needed...

# Create a new Workload instance for the output
output_workload = SWFUtils.Workload()
output_workload.populate(metadata, jobs)

# Create an instance of the Writer and write the data back to a file
writer = SWFUtils.Writer('path_to_your_output_file.swf', output_workload)
writer.write()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.