# from file_argparse import args
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=0, help='select video-stream port number')
parser.add_argument('--save', type=str, choices=['yes', 'no'],default="no", help='to save the video-stream')
args = parser.parse_args()

port = args.port 
video = cv2.VideoCapture(port)

if (video.isOpened() == False):
	print("Error reading video file")
else :
	print("Camera Connected Succesfully on port : ",port)