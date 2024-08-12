import base64
import json
import requests
import os

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

if not "api/webhooks" in c2_:
    print(f"\nInvalid Link.")
try:
    r = requests.get(c2_)
except (
    requests.exceptions.MissingSchema,
    requests.exceptions.InvalidSchema,
    requests.exceptions.ConnectionError,
):
    print(f"\nInvalid Webhook.")
try:
    j = None
    j = r.json()["name"]
except (KeyError, json.decoder.JSONDecodeError):
    print(f"\nInvalid Webhook.")
if j == None:
    print(f"\nInvalid Webhook.")
else:
    print(f"Valid webhook! ({j})"\n)

os.system("pause")
