import os
from setuptools import setup

# data_files option in setuptools allows you to include data files outside of the package's directory structure
# the data file in a wheel distribution will be installed at {distribution}.data/data directory
data_files = []

for root, dirs, files in os.walk('configuration'):
    # (. [file paths under configuration directory])
    # wheel distribution include the data files under {distribution}.data directory
    # egg distribution include the configuration directory
    data_files.append((os.path.relpath(root, 'configuration'), [os.path.join(root, f) for f in files]))


setup(
    data_files=data_files
)

