import os

import check_cam,capture_faces,train_faces,recognize_face,send_email



def titalBar():
    os.system('cls')
    print("**********************************************\n")
    print("*********Project tile here*******\n")
    print("**********************************************\n")

def mainmenu():
    # titalBar()
    print()
    print(5*"*","Welcome to Sytstem",5*"*")
    print("1) check cam")
    print("2) capture face")
    print("3) train data")
    print("4) mark attendace")
    print("5) email")

    while True:
        try:
            select_option = int(input("Enter your Choice: --> "))

            if select_option == 1:
                checkCam()
                break
            elif select_option == 2:
                captureface()
                break
            elif select_option == 3:
                trainImages()
                break
            elif select_option == 4:
                markAttendence()
                break
            elif select_option == 5:
                sendAttendence()
                break
            else:
                print("\nInvalid input Please enter 1-4")
                mainmenu()
        except ValueError:
            print("\ninvalid Choice")
    


def checkCam():
    check_cam.camera_check()
    mainmenu()

def captureface():
    capture_faces.takeImages()
    mainmenu()

def trainImages():
    train_faces.TrainImages()
    mainmenu()

def markAttendence():
    recognize_face.recognize_faces()
    mainmenu()

def sendAttendence():
    send_email.send_email()
    mainmenu()

mainmenu()
# virtualenv myenv
# pip install virtualenv
# myenv\Scripts\activate
# pip install cv2
# pip install pillow 
# pip install pandas
# pip install opencv-python
# pip install opencv-contrib-python
# python main.py