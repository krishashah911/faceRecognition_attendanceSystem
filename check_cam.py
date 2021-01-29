import cv2
def camera_check():
    
    video_cap = cv2.VideoCapture(0)
    while True:
        _, video_data = video_cap.read()
        cv2.imshow("Video",video_data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_cap.release()
    cv2.destroyAllWindows()