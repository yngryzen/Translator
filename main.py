import requests
import time

translate = input("Enter text: ")

r = requests.post("https://api-free.deepl.com/v2/translate", headers={"Authorization": "DeepL-Auth-Key 7c188974-7146-4af3-aed2-ccb225f0cb49:fx"}, json={
    "text": [translate],
    "target_lang": "EN-GB"
}).json()

print(r["translations"][0]["text"])