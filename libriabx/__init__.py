from importlib.metadata import version, PackageNotFoundError
from .wrappers import AbxArguments, run_abx

try:
    __version__ = version("zerospeech-benchmark")
except PackageNotFoundError:
    # package is not installed
    __version__ = None
