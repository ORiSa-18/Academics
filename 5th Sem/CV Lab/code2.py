import cv2

#read and display the video
video = cv2.VideoCapture('./Videos/stalk.mp4')
while video.isOpened():
    ret,frame = video.read()
    if ret:
        cv2.imshow('video',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()

#convert frames of video to grayscale
while video.isOpened():
    ret,frame = video.read()
    if ret:
        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray_video',gray_scale)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
            break
video.release()
cv2.destroyAllWindows()

#check properties of video
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
num_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
print(f"Width: {width} \n Height: {height} \n FPS: {fps} \n Numbber of Frames: {num_frame}")


