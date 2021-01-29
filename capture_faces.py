import cv2,os,csv

def takeImages():
    Id = input("Enter Your Id:===> ")
    name = input("Enter your Name:===> ")

    if (name.isalpha() and Id.isdigit()):
        video_cap = cv2.VideoCapture(0)
        face_data = cv2.CascadeClassifier("facedata.xml")
        sampleNumber = 0
        while(True):
            ret,img = video_cap.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_data.detectMultiScale(gray,1.5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(25, 25,227),2)
                sampleNumber = sampleNumber+1
                cv2.imwrite("training_data"+os.sep+name+"_"+Id+"_"+str(sampleNumber)+".jpg",gray[y:y+h,x:x+w])
                cv2.imshow('image',img)
            
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNumber > 100:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        res = "Images saves for Id "+Id+" Name: "+name
        row = [Id,name]
        with open("student_faces.csv",'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    else:
        if Id.isdigit():
            print("Please Enter Name in Alphabetic Only...")
        if name.isalpha():
            print("Please Enter Id in Numbers only...")



