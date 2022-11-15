# hv-get-power

A python package to allow querying IPMITool for information. Currently only allowing collection of power data.

# Installation

Must have Python3 and pip installed and updated. 
To install the Python package, clone the repository and run:

`pip install /path/to/repo/`

# Usage

```
from ipmitool.functions import *
res = get_current_power(csv=True) # produces a csv string
```