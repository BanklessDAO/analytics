# simple helper script to convert csv column headers to entity class field names

import csv
import sys
import os

def field_name_format(header):
    return header.lower().replace(' ', '_')

def generate_entity_fields(column_headers):
    for header in column_headers:
        print(field_name_format(header))

# simply copy console output and put it into entity class
# add typing information for each field manually
if __name__ == '__main__':
    if len(sys.argv) == 2:
        cwd = os.getcwd()
        path = sys.argv[1]
        csvpath = os.path.join(cwd, path)

        with open(csvpath) as csvfile:
          reader = csv.reader(csvfile, delimiter=',')
          column_headers = reader.__next__()

        generate_entity_fields(column_headers)
    else:
        print('usage: python gen_fields_from_csv.py path_to_analytics.csv')

# todo: use this script combined with an array of type info
# to generate a complete entity class and input type