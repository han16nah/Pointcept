"""
Hessigheim3D Dataset

Author: Hannah Weiser (h.weiser@uni-heidelberg.de)
"""

from pathlib import Path
from collections.abc import Sequence
from .defaults import DefaultDataset
from .builder import DATASETS


@DATASETS.register_module()
class Hessigheim3DDataset(DefaultDataset):
    def get_data_list(self):
        # data is located in a folder specifying the tiling structure
        if isinstance(self.split, str):
            data_list = list(Path(self.data_root).rglob(f"{self.split}/*/*"))
        elif isinstance(self.split, Sequence):
            data_list = []
            for split in self.split:
                data_list += Path(self.data_root).rglob(f"{split}/*/*")
        else:
            raise NotImplementedError
        print(data_list)
        return data_list
    
    def get_data_name(self, idx):
        # data_list contains all individual file paths - we want the folder name
        area_name = Path(self.data_list[idx % len(self.data_list)]).name
        return f"{area_name}"
