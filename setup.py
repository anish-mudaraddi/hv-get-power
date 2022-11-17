from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'python package for querying IPMI tool'

LONG_DESCRIPTION = """Python package to query IPMITool to get power statistics"""

setup (
        name="iriscastipmi",
        version=VERSION,
        author="Anish Mudaraddi",
        author_email="<anish.mudaraddi@stfc.ac.uk>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        python_requires='>=3',
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['python']
)
