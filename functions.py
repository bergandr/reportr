import os
from zipfile import ZipFile


def zip_all(directory, zip_name):
    zip_name_extended = zip_name + ".zip"
    zip_dest = os.path.join(os.path.dirname(directory), zip_name_extended)
    files = os.listdir(directory)
    with ZipFile(zip_dest, 'w') as myzip:
        for file in files:
            filepath = os.path.join(directory, file)
            myzip.write(filepath, os.path.join(zip_name, file))

    return zip_dest