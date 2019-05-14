from zipfile import ZipFile
import shutil
import glob
import os
import datetime
import dropbox

def get_file_paths(directory_to_zip):
    file_paths = []
    for root, directories, files in os.walk(directory_to_zip):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

directory_to_zip = './stills/'
now = datetime.datetime.now()
file_paths = get_file_paths(directory_to_zip)

archive_name = 'Camera_Stills' + now.isoformat()
shutil.make_archive(archive_name, 'zip', directory_to_zip)
#with ZipFile(archive_name, 'w') as zip:
#    for file in file_paths:
#        zip.write(file)
print('All files zipped succesfully!')

f = open(archive_name + '.zip')
dbx = dropbox.Dropbox('itsEPUWg-uAAAAAAAAAADHkqCns1QzQ60mpfGQWrlpEDYoWD6P2gW3Qucm-BYtY8')
dbx.files_upload(f.read(), '/Camera_captures_' + str(now.hour) 
        + '_' +  str(now.minute) + '_' + str(now.second) + '.zip')
print("Archive uploaded succesfully!")
f.close()

mydir1 = "/home/pi/proj/stills/detectedMotionStills"
mydir2 = "/home/pi/proj/stills/timedStills"
filelist = glob.glob(os.path.join(mydir1, "*.jpg"))
for f in filelist:
        os.remove(f)

filelist = glob.glob(os.path.join(mydir2, "*.jpg"))
for f in filelist:
        os.remove(f)

os.remove(archive_name + '.zip')
