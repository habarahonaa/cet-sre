from controller import controller
import schedule
import sys
import time

if __name__ == "__main__":
    # Runs the controller function every sunday at 10:00
    schedule.every().sunday.at("10:00").do(controller)
    while True:
        schedule.run_pending()
        time.sleep(1)
        sys.stdout.flush()