#!/usr/bin/python3
import requests

for year in range(2020,2022):
    for month in range(1,13):
        for day in range(1, 32):
            filename = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}-upload.pdf"
            with requests.session() as r:
                pdf = requests.get(f"http://10.10.10.248/documents/{filename}")
                if pdf.status_code == 200:
                    print(f"Found a file {filename}")
                    with open(filename, "wb") as file:
                        file.write(pdf.content)
