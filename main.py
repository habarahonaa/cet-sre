import schedule
import sys
import time
from controller import controller

if __name__ == "__main__":
    schedule.every().sunday.at("10:00").do(controller)
    while True:
        schedule.run_pending()
        time.sleep(1)
        sys.stdout.flush()