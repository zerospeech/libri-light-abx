from importlib.metadata import version, PackageNotFoundError
from .wrappers import AbxArguments, abx_eval

try:
    __version__ = version("zerospeech-libriabx")
except PackageNotFoundError:
    # package is not installed
    __version__ = None
