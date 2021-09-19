from pathlib import Path
import os

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest/path.relative_to(self.source)
        directory = os.mkdir(directory, parents=True, exist_ok=True)


    def build(self):
        self.dest = os.mkdir(dest, parents=True, exist_ok=True)


