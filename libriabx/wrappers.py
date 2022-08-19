from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .libri_light.eval_ABX import main as run_abx

ABXFileTypes = Enum('ABXFileTypes',
                    '.pt .npy .txt .wav .flac .mp3')
ABXMode = Enum('ABXMode', 'all within across')

ABXDistanceMode = Enum('ABXDistanceMode',
                       'euclidian cosine kl kl_symmetric')


@dataclass
class AbxArguments:
    """ List of arguments to provide to abx in phonetic_eval.abx"""
    # path to input data
    path_data: str
    # path to item file
    path_item_file: str
    # Path to a CPC checkpoint
    path_checkpoint: Optional[str] = None
    # size of a single feature
    feature_size: Optional[float] = float(0.1)
    # Use the GPU to compute distances
    cuda: bool = True
    # extension (of input files ?)
    file_extension: ABXFileTypes = '.txt'
    # Choose the mode of the ABX score to compute
    mode: ABXMode = 'all'
    # Choose the kind of distance to use to compute
    distance_mode: ABXDistanceMode = 'cosine'
    # Max size of a group while computing the ABX score
    max_size_group: int = 10
    # When computing the ABX across score, maximum
    # number of speaker X to sample per couple A,B.
    max_x_across: int = 5
    # location to output the results
    out: Optional[str] = None


def abx(args: AbxArguments):
    return run_abx(arg_obj=args)
