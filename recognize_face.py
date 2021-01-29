import cv2,time,datetime
import pandas as pd 


def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner.yml")
    face_data = cv2.CascadeClassifier("facedata.xml")
    # ============
    df = pd.read_csv("student_faces.csv")
    font  =cv2.FONT_HERSHEY_COMPLEX
    col_names = ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns=col_names)

    video_cap = cv2.VideoCapture(0)
    video_cap.set(3,640)
    video_cap.set(4,480)

    minW = 0.1 * video_cap.get(3)
    minH = 0.1 * video_cap.get(4)

    while True:
        _,img = video_cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_data.detectMultiScale(gray,1.5,5,minSize=(int(minW),int(minH)),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

            if conf < 100:
                data = df.loc[df['Id']== Id]['Name'].values
                detection_rate = " {}%".format(round(100-conf))
                data_id_str = str(Id)+"----"+data
            else:
                Id = 'unknown'
                data_id_str = str(Id)
                detection_rate = " {}%".format(round(100-conf))

            if (100-conf) > 60:
                time_data = time.time()
                date = datetime.datetime.fromtimestamp(time_data).strftime('%d-%m-%Y')
                timestamp = datetime.datetime.fromtimestamp(time_data).strftime('%H:%M:%S')
                data = str(data)[2:-2]
                attendance.loc[len(attendance)] = [Id,data,date,timestamp]
            data_id_str = str(data_id_str)[2:-2]
            if (100-conf) > 60:
                data_id_str = data_id_str + " [pass]"
                cv2.putText(img,str(data_id_str),(x+10,y-10),font,1,(255,0,0),2)
            else:
                cv2.putText(img,str(data_id_str),(x+10,y-10),font,1,(255,0,0),2)

            if (100-conf) > 60:
                cv2.putText(img,str(detection_rate),(x+10,y-10),font,1,(0,255,0),1)
            elif(100-conf) >50:
                cv2.putText(img,str(detection_rate),(x+10,y-10),font,1,(0,255,0),1)
            else:
                cv2.putText(img,str(detection_rate),(x+10,y-10),font,1,(0,255,0),1)

        attendance = attendance.drop_duplicates(subset=['Id'],keep='first')
        cv2.imshow('Hey Student ',img)  
        if (cv2.waitKey(1) == ord('q')):
            break
    time_data = time.time()
    date = datetime.datetime.fromtimestamp(time_data).strftime('%d-%m-%Y')
    timestamp = datetime.datetime.fromtimestamp(time_data).strftime('%H:%M:%S')
    Hour,Min,Sec = timestamp.split(":")
    filename = date+"_"+Hour+"_"+Min+"_"+Sec+".csv"
    attendance.to_csv(filename,index=False)
    print("thank you.....")
    video_cap.release()
    cv2.destroyAllWindows()




