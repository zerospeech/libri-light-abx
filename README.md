# LibriLight ABX

This is a wrapper module around the abx implementation found in [libri-light/eval](https://github.com/facebookresearch/libri-light/tree/main/eval).
This module only adds a wrapper function to directly call abx evaluation and a dataclass object annotating all arguments as well as a setup.py to allow installation
as a module.


## Installation

You can install this module from pip directly using the following command : `pip install zerospeech-libriabx`

Or you can install from source by cloning this repository and running : `pip install .`


## Usage

### From command line

A command line is created to allow running abx evaluations.

```
usage: libri-abx [-h] [--path_checkpoint PATH_CHECKPOINT] [--file_extension {.pt,.npy,.wav,.flac,.mp3}] [--feature_size FEATURE_SIZE] [--cuda] [--mode {all,within,across}]
                 [--distance_mode {euclidian,cosine,kl,kl_symmetric}] [--max_size_group MAX_SIZE_GROUP] [--max_x_across MAX_X_ACROSS] [--out OUT]
                 path_data path_item_file

ABX metric

positional arguments:
  path_data             Path to directory containing the data
  path_item_file        Path to the .item file

optional arguments:
  -h, --help            show this help message and exit
  --path_checkpoint PATH_CHECKPOINT
                        Path to a CPC checkpoint. If set, the apply the model to the input data to compute the features
  --file_extension {.pt,.npy,.wav,.flac,.mp3}
  --feature_size FEATURE_SIZE
                        Size (in s) of one feature
  --cuda                Use the GPU to compute distances
  --mode {all,within,across}
                        Choose the mode of the ABX score to compute
  --distance_mode {euclidian,cosine,kl,kl_symmetric}
                        Choose the kind of distance to use to compute the ABX score.
  --max_size_group MAX_SIZE_GROUP
                        Max size of a group while computing theABX score. A small value will make the code faster but less precise.
  --max_x_across MAX_X_ACROSS
                        When computing the ABX across score, maximumnumber of speaker X to sample per couple A,B. A small value will make the code faster but less precise.
  --out OUT             Path where the results should be saved

```

### From python API

To call the abx evaluation from python code you can use the following example :

```python 
from pathlib import Path
import libriabx

args = libriabx.AbxArguments(
    path_data=Path("/location/to/scores/")
    path_item_file=Path("/location/to/file.item")
    **other_options
)
result = libriabx.abx_eval(args)
```

For all possible options see the [AbxArguments class definition](libriabx/wrappers.py).

> Result is a dictionary containing Dict{mode -> score} where mode is defined as (across, within)


## Building & Upload

For security & compatibility reasons binary builds require a special environment to be build.
We need to use the manylinux docker container so that correct flags are used.

To do this run :

```shell
> docker pull quay.io/pypa/manylinux2014_x86_64
> docker run --rm -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 bash /io/build_wheel.sh
```

> To check for pyversions available `docker run --rm quay.io/pypa/manylinux2014_x86_64 ls /opt/python`

This allows to populate with compiled versions of libriabx for python3.8, python3.9, python3.10, python3.11 in the dist folder.
For more information see [ManyLinux Implementation](https://github.com/pypa/manylinux)

Once binaries have been build we can upload them to pypi using : `twine upload dist/*`