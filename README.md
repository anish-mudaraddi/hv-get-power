# IRISCAST Tools

A python package which contains tools for collecting energy usage and CPU usage information - by querying IPMITool and others. 

# Installation

Must have Python3 and pip installed and updated. 
To install the Python package, clone the repository and run:

`pip install /path/to/repo/`

# Usage

```
from iriscasttool.functions import *
res = get_iriscast_stats(csv=True, poll_period_seconds=60, include_header=False) # produces a csv string

```
