import requests
import json

url = 'https://iot-backend-iihizzkyh-nat-siriruangbuns-projects.vercel.app/data/Food?amount=1000000'

try:

    response = requests.post(url)

    response.raise_for_status()

except requests.exceptions.HTTPError as err:
    print(f"เกิดข้อผิดพลาดในการเรียก API: HTTP Error - {err}")
except requests.exceptions.RequestException as err:
    print(f"เกิดข้อผิดพลาดในการเรียก API: Error - {err}")