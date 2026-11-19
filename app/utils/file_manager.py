import os

class ReportWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()



import os

class ReportWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        folder = os.path.dirname(self.filename)

        if folder:
            os.makedirs(folder, exist_ok=True)

        self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        return False
