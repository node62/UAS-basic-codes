import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=0, help='select video-stream port number')
parser.add_argument('--save', type=str, choices=['yes', 'no'],default="no", help='to save the video-stream')
args = parser.parse_args()

cap = cv2.VideoCapture(args.port)
output_folder = "frames"
i = 1
while True :
        if not os.path.exists(output_folder+f'_{i}'):
            output_folder = output_folder+f'_{i}'
            os.makedirs(output_folder)
            break
        else :
            i += 1
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_no = 1
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imwrite(f"{output_folder}/frame_{frame_no}.jpg", frame)
    frame_no += 1

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()