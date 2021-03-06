import pandas as pd
from addfriends import Addfriend


class Readfile:
    file = pd.read_excel("tt.xlsx", dtype=str)
    lines = file.shape[0]

    def get_line_content(self, line):
        tt = self.file["TT号"][line]
        print(tt)
        return tt
