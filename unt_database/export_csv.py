import os

from unt_database.get_unt_data import create_csv

for file in os.listdir('database'):
    if file.endswith('.txt'):
        file_name = file.split('.')[0]
        create_csv(file_name)
