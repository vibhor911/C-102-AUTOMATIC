
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    # initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
        print("Snapshot taken")
        videoCaptureObject.released()
        cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token='sl.A8H8P_lKvFb6m5upz4Ok7dMHrVoCR-4K-yhIXeY85F2apzldnS_ZmNrXvmiRxfKUsQKop-iBAG4pq4CwGnHVdb-HRUbWY7QmomnKO6_TIuk2KzNSc77xF5CX7ItS9cViLE5MMplCGXgC'
    file = image_name
    file_from = file
    file_to ="newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >=3):
            name = take_snapshot()
            upload_file(name)

main()