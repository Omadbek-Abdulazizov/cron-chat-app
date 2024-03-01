from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .py_file import p

def start():
    now = datetime.now()
    scheduler = BackgroundScheduler()
    scheduler.add_job(p, 'interval', seconds=60)
    scheduler.start()