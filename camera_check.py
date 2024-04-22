from file_argparse import args
import cv2

port = args.port 
video = cv2.VideoCapture(port)

if (video.isOpened() == False):
	print("Error reading video file")
else :
	print("Camera Connected Succesfully on port : ",port)