import schedule
import time
from file_organizer import organize_files
import logging

# Set up logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def job():
    logging.info("Running file organization...")
    organize_files()
    logging.info("File organization completed.")

# Schedule the job to run every Sunday at 1:00 AM
schedule.every().sunday.at("01:00").do(job)

if __name__ == "__main__":
    logging.info("Scheduler started.")
    while True:
        schedule.run_pending()
        time.sleep(1)
