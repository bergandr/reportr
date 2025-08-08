import os
from zipfile import ZipFile


zip_path_shared = "/Users/andrewberger/cs361-samples/report_zips"


def zip_all(directory, zip_name):
    zip_dest = os.path.join(zip_path_shared, zip_name)
    print(zip_dest)
    files = os.listdir(directory)
    with ZipFile(zip_dest, 'w') as myzip:
        for file in files:
            filepath = os.path.join(directory, file)
            myzip.write(filepath)
