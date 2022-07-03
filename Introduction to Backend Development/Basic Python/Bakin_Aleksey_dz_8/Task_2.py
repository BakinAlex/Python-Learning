import requests
import re

URL = "https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
rez = requests.get(URL)

with open("rez.txt", 'w+', encoding = 'utf-8') as file:
    file.write(rez.text)
with open("rez.txt", 'r', encoding = 'utf-8') as file:
    for i in file:
        rez = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[(.+\d{4}).*"([A-Z]{3}).*(/d.+?)\s.*\s(\d+)\s(\d+) ', i)
        if not rez:
            rez = re.findall(r'(^\w{4}:.+\:\w{4}).*\[(.+\d{4}).*"([A-Z]{3}).*(/d.+?)\s.*\s(\d+)\s(\d+)', i)
            if not rez:
                print("Не прошло фильтр", i)
        with open("rez_format.txt", "a", encoding = "utf-8") as rez_format:
            rez_format.write(f'{rez}\n')
    print("Конец поиска")
