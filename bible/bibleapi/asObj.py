class AsObj:
    def __init__(self, **entries):
        self.entries = entries
        self.__dict__.update(entries)

