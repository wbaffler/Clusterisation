
from urllib.request import urlopen
import numpy as np
from error_codes import Error_codes as code
class File_parser:
    def __init__(self, url_path ):
        self.error = code.ok
        try:
            self.url = urlopen(url_path)
            print("URL Opened")
        except Exception:
            self.error = code.url_error

    def parse(self):
        matrix = []
        self.int_matrix = []
        try:
            data = self.url.readlines()
            
            my_list = []
            for line in data:
                if not line.strip():
                    continue
                my_list.append(line.lstrip().split())

            print("1")
            arr = np.array(my_list)
            self.int_matrix = arr.astype(np.int32)

            '''for line in data:
                    matrix.append([float(x) for x in line.split()])

            for line in data:
                if line.strip():
                    self.int_matrix = np.array(matrix, int)
'''
            print(len(self.int_matrix))
        except Exception:
            self.error = code.read_error

    
    def get_matrix(self):
        return self.int_matrix

    def get_error_code(self):
        return self.error

