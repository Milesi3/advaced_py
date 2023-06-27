# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle

csv_file_path = 'output.csv'

with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    csv_data = list(reader)

pickle_line = pickle.dumps(csv_data)
print(pickle_line)
