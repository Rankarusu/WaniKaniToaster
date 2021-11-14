import requests
from win10toast_persist import ToastNotifier
import schedule
import time
import os

TOKEN = "YOUR_V2_TOKEN_HERE"
url = "https://api.wanikani.com/v2/assignments?immediately_available_for_review"
header = {'Authorization': 'Bearer ' + TOKEN}

toaster = ToastNotifier()
dirname = os.path.dirname(__file__)
iconpath = os.path.join(dirname, "wanikani.ico")


def notify():
    response = requests.get(url, headers=header)
    jresponse = response.json()
    pendingreviews = jresponse["total_count"]
    text = f"{pendingreviews} reviews available!"
    if int(pendingreviews) > 0:
        toaster.show_toast("WaniKani", text, icon_path=iconpath, duration=None)


schedule.every().hour.at(":01").do(notify)

while True:
    schedule.run_pending()
    time.sleep(1)
