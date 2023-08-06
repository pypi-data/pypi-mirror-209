config_folder = None


class TableImplementationError(NotImplementedError):
    pass


class TableAttachmentProtocol:
    def run(self, on, *args, **kwargs):
        raise TableImplementationError

    def __init__(self, *args, **kwargs):
        pass
        # self.output = {}
