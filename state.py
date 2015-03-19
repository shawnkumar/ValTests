class State(object):

    numrows = 0

    def __init__(self, statefile, rows=None):
        self.statefile = statefile
        if rows!=None:
            self.toFile(rows)

    def toFile(self, rows):
        for idx, row in enumerate(rows):
            rowstring = row.toString()
            if idx != 0:
                rowstring = '\n' + rowstring
            with open(self.statefile, 'a') as f:
                f.write(rowstring)
                self.numrows=self.numrows+1

    def add_row(self, row):
        with open(self.statefile, 'a') as f:
            f.write('\n' + row.toString())
            self.numrows = self.numrows + 1

    def get_file(self):
        return self.statefile

    def get_num_rows(self):
        return self.numrows