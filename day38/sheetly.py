from const import SHEETLY_KEY, SHEETLY_URL_POST, EXERCISE, DURATION, CALORIES
from data_requests import post_request_data
from datetime import datetime

header = {"Authorization": f"Bearer {SHEETLY_KEY}"}
now = datetime.now()
date = now.strftime('%Y/%m/%d')
time = now.strftime('%H:%M:%S')


def post(workout):
    param = {
        "workout": {
            "date": f"{date}",
            "time": f"{time}",
            "exercise": f"{workout[EXERCISE]}",
            "duration": f'{workout[DURATION]}',
            'calories': f'{workout[CALORIES]}'
        }
    }
    return post_request_data(url=SHEETLY_URL_POST, json=param, headers=header)
