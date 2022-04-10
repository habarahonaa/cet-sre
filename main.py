from controller import controller
import schedule
import sys
import time

def main():
    # Run the controller
    controller()
    sys.exit(0)

if __name__ == "__main__":
    main()

'''
if __name__ == "__main__":
    # Runs the controller function every hour
    schedule.every().sunday.at("8:00").do(controller.controller)
    while True:
        schedule.run_pending()
        time.sleep(1)
'''