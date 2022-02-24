# Parse the CSV of dipper -> grain volumes to calculate derived VMD values.

import csv
import json

derived_vmd = {}

with open('../ref/Dippers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        derived_vmd[row['POWDER']] = {}
        average = 0

        for cc in list(row.keys())[1:]:
            vmd = float(cc) / float(row[cc])
            derived_vmd[row['POWDER']][cc] = vmd
            average += vmd
        
        derived_vmd[row['POWDER']]['avg'] = average / 16

with open("../derived_vmd.json", "w") as ref_json:
    json.dump(derived_vmd, ref_json, indent=4)