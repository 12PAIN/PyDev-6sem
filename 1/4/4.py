import os
import zipfile
import datetime


def make_reserve_arc(source, dest):
    now = datetime.datetime.now()

    archive_name = f"{os.path.basename(source)}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.zip"

    with zipfile.ZipFile(os.path.join(dest, archive_name), "w") as zip_file:
        for root, dirs, files in os.walk(source):
            for file in files:
                zip_file.write(os.path.join(root, file))


source = input("Enter the path to the directory to archive: ")
dest = input("Enter the path to the directory to place the archive: ")
make_reserve_arc(source, dest)
