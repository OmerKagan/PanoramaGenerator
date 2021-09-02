import cv2
import os

mainFolder = "Images"
subFolders = os.listdir(mainFolder)
print(subFolders)

for folder in subFolders:
    path = mainFolder + "/" + folder
    images = []
    myList = os.listdir(path)
    print(f'Total number of images detected in folder {folder}: {len(myList)}')
    for img in myList:
        curImg = cv2.imread(f'{path}/{img}')
        curImg = cv2.resize(curImg, (0, 0), None, 0.5, 0.5)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    #print(status) 0 for ok(if panorama generated) - 1 for not have enough keypoints in images(need more common points)
    if status == cv2.STITCHER_OK:
        print("Panorama Generated")
        cv2.imshow(folder, result)
        cv2.waitKey(1)
    else:
        print("Process unsuccessful: Panorama Generation")

cv2.waitKey(0)