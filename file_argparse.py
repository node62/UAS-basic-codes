import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=0, help='select video-stream port number')
parser.add_argument('--save', type=str, choices=['yes', 'no'],default="no", help='to save the video-stream')
args = parser.parse_args()
# print(f"port is {args.port} and save is {args.save}")