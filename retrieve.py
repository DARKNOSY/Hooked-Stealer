import base64
import requests

r = requests.get('https://raw.githubusercontent.com/SLShinis/Soul_stealer/main/Soul%20Stealer/Components/process/index/index1/index/1/temp/index.pyw')

if r.status_code == 200:
    rw = r.text
else:
    raise Exception(f"Failed to retrieve script. Status code: {r.status_code}")

c2_ = None
for line in rw.splitlines():
    if 'C2 =' in line:
        _string = line.split("base64.b64decode('")[1].split("').decode()")[0]
        c2_ = base64.b64decode(_string).decode()
        break

print(f"Hook > {c2_}")
