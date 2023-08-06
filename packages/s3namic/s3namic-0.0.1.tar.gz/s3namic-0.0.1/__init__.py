from setuptools import setup
from _version import get_version

__docformat__ = 'restructuredtext'

_hard_dependencies=[
    'pandas', 
    'boto3', 
    'botocore',
    'pyarrow',
]

# _soft_dependencies=[
#     'pyarrow',
# ]

_missing_dependencies = []
for _dependency in _hard_dependencies:
    try:
        __import__(_dependency)
    except ImportError as _e:
        _missing_dependencies.append(f"{_dependency}: ({_e})")
        
if _missing_dependencies:
    raise ImportError(
        f"Required packages not installed. Please install the following packages:\n" + "\n".join(_missing_dependencies)
    )
    
v = get_version()
__version__ = v.get("closest-tag", v["version"])

del get_version, v

setup(
    name='s3namic',
    version=__version__,
    author='Joey Kim',
    author_email='hyoj0942@gmail.com',
    description='my project',
)

del _hard_dependencies, _dependency, _missing_dependencies

from api import (
    s3namic
)

__all__ = [
    "s3namic",
]

