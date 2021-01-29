import os,cv2,time
from PIL import Image
import numpy as np
from threading import Thread

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage,'uint8')
        Id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces,Ids

def counter_img(path):
    imgCounter = 1
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        print(str(imgCounter)+" Images Trained")
        time.sleep(0.005)
        imgCounter += 1

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    face_data = cv2.CascadeClassifier("facedata.xml")
    faces,Id = getImagesAndLabels("training_data")
    Thread(target=recognizer.train(faces,np.array(Id))).start()
    Thread(target=counter_img("training_data")).start()
    recognizer.save("Trainner.yml")
    print("Done")






