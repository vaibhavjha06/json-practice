#!/bin/bash python3

import requests
import json
import csv

with open('data/schacon.repos.json') as f:
	json_data = json.load(f)

selected_columns = ['name', 'html_url', 'updated_at', 'visibility']
filtered_data = [{key: entry[key] for key in selected_columns} for entry in json_data]

headers = filtered_data[0].keys()
with open('chacon.csv', 'w', newline='') as f:
	writer = csv.DictWriter(f, fieldnames=headers)
	writer.writerows(filtered_data)


# I really tried to limit output to 5 but could not find a way. Sorry about this.