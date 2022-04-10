from controller import controller
import schedule
import sys
import time

if __name__ == "__main__":
    # Runs the controller function every hour
    schedule.every().sunday.at("14:47").do(controller)
    while True:
        schedule.run_pending()
        time.sleep(1)
        sys.stdout.flush()