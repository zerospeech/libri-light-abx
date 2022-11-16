from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, List

from vdataset import mount, unmount

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
    # boolean flag setting the path_data as a mounted dataset
    _is_mounted: bool = False

    @classmethod
    def load_from_file_list(cls, file_list: List[Path], **kwargs):
        """ Create a mounted folder containing all the files as symlinks """
        data_loc = mount(file_list)
        if data_loc:
            return cls(path_data=str(data_loc), **kwargs)

        raise SystemError('Could not create temp folder')

    def clear_mounts(self):
        """ Clean mounted folder """
        if self._is_mounted:
            unmount(self.path_data)


def abx_eval(args: AbxArguments):
    """ Run abx evaluation """
    results = run_abx(arg_obj=args)
    args.clear_mounts()
    return results
