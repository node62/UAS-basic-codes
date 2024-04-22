import cv2
import os 

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
def save_video(output_folder,video_name,fps):

    j = 1
    while True :
            if not os.path.exists(f"{output_folder}/{video_name}_{j}.mp4"):
                video_name = video_name+f'_{j}'
                break
            else :
                j += 1
    out = cv2.VideoWriter(f"{output_folder}/{video_name}.mp4", fourcc, fps, (640, 480))  # Output file name, codec, FPS, frame size

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) ==ord("a"):
                break
        else:
            break
    out.release()


if __name__ =="__main__":
    output_folder = "output"
    video_name = "video"
    fps = 20
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    save_video(output_folder,video_name,fps)
cap.release()
cv2.destroyAllWindows()
