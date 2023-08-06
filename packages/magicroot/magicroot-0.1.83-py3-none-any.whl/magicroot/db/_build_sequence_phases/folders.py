from ...attach import attachment
from ..utils import config_folder


@attachment
class FoldersStorage:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config_folder
