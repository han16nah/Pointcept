"""
Hessigheim3D Dataset

Author: Hannah Weiser (h.weiser@uni-heidelberg.de)
"""

from pathlib import Path
from .defaults import DefaultDataset
from .builder import DATASETS


@DATASETS.register_module()
class H3DDataset(DefaultDataset):
    def get_data_name(self, idx):
        # data_list contains all individual file paths - we want the folder name
        area_name = Path(self.data_list[idx]).name
        return f"{area_name}"
