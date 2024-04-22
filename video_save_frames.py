import cv2
import os

def save_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)

    i = 1
    while True :
        if not os.path.exists(output_folder+f'_{i}'):
            output_folder = output_folder+f'_{i}'
            os.makedirs(output_folder)
            break
        else :
            i += 1

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    for frame_number in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        frame_filename = f"{output_folder}/frame_{frame_number}.png"
        cv2.imwrite(frame_filename, frame)
    
    cap.release()

if __name__ == "__main__":

    video_path = "output/video_1.mp4"
    output_folder = "frames"
    save_frames(video_path, output_folder)
