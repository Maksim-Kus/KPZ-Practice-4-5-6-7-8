import csv
from collections import Counter
import requests

CSV_URL = "https://support.staffbase.com/hc/en-us/article_attachments/360009197031/username.csv"

def get_text_info(filepath):
    with open(filepath) as file_csv:
        header = next(file_csv)
        content = csv.reader(file_csv, delimiter=";")
        data = []
        for row in content:
            data.extend(row)
        print(dict(Counter(data)))

def download_csv(urlpath):
    with requests.Session() as s:
        download = s.get(urlpath)
        open('source_data/csv_file.csv', 'wb').write(download.content)
        print("Download completed!\n")

download_csv(CSV_URL)
get_text_info('source_data/csv_file.csv')
