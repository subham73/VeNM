import cv2
import os
import re


def process_name(video_path):
    name = video_path.split('\\')[-1].split(".")[0].title()
    name = re.sub("[^A-Za-z0-9]","",name)
    name = name.replace(" ", "")
    # return name

def extract_frame(video_path, gap):
    target_folder_path = '../data/frames'
    name = process_name(video_path)
    target_folder_path = os.path.join(target_folder_path, name)
    create_dir(target_folder_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True:
        ret, frame = cap.read()
        
        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{target_folder_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{target_folder_path}/{idx}.png", frame)
        
        # idx +=1

        # if idx == 1000:
        #     break
    
    return target_folder_path

def main:
    

if __name__ == "__main__":
    link1 = r'D:\Venm\data\video\1 minute funny videos.mp4'
    link2 = r'D:\Venm\data\video\10 Principles of Economics.mp4'
    path = extract_frame(link2,2)




def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")