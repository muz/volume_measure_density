# Produce a single JSON file of both supplied, and derived VMD values for

import json

derived_powders = []
with open('../derived_vmd.json') as json_file:
    derived = json.load(json_file)

    for powder in derived.keys():
        derived_powders.append(
            {
                "vmd": derived[powder]['avg'],
                "powder": powder,
                "_ref": "derived_dippers"
            }
        )

with open('../supplied_vmd.json') as json_file:
    supplied = json.load(json_file)

    with open("../vmd.json", "w") as vmd_json:
        json.dump(supplied + derived_powders, vmd_json, indent=4)