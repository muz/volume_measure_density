# Quick and dirty script to parse those funny plaintext ref files and generate
# some standardised JSON I can actually work with...

import json
import re

vmd_info = []
refs = [
    '90058_2',
    '90058_i',
    '90058',
    'AP1074_ru',
    'AP1074'
]

for ref in refs:
    with open("../ref/%s.txt" % ref, 'r') as txt:
        for line in txt:
            line = line.strip()
            if re.match(r'^[A-Z]', line):
                manufacturer = line

            if re.match(r'^\.\d{4}', line):
                vmd, powder = line.split(" ", 1)
                vmd_info.append({
                    'vmd': float("0%s" % vmd),
                    'powder': powder,
                    'manufacturer': manufacturer,
                    '_ref': ref
                })

with open("../supplied_vmd.json", "w") as ref_json:
    json.dump(vmd_info, ref_json, indent=4)