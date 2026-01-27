import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/mike/Imagens"
destination_dir = "/home/mike/Backups"

def cpy_folder_to_dir(src, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(src, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}!")

schedule.every().day.at("18:00").do(lambda: cpy_folder_to_dir(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)