class FileReader:

    def __init__(self, file_name):
        self.file_name = self.set_file_name(file_name)

    def set_file_name(self, file_name):
        """Validate file name."""
        try:
            open(file_name)
        except FileNotFoundError:
            print("Invalid quiz name")
            exit(1)

        return file_name

    def read_content(self):
        """Read a file's content."""
        return open(self.file_name)

    def parse_line(self, line):
        """Parse csv line into list"""
        return line.split(",")