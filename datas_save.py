
import cv2
import os
import argparse

def videoRunner(path1,path2):
  print(path1,path2)
  frame_no = 1
  cap = cv2.VideoCapture(args.port)
  while True:
      ret, frame = cap.read()
      if not ret:
          print("Error: Failed to capture frame.")
          break
      if path1 != "alphanumeric/na" :
        cv2.imwrite(f"{path1}/frame_{frame_no}.jpg", frame)
      if path2 != "shapes/na" :
        cv2.imwrite(f"{path2}/frame_{frame_no}.jpg", frame)
      frame_no += 1
      if cv2.waitKey(1) & 0xFF == ord('a'):
          break
  cap.release()
  cv2.destroyAllWindows()

def saveDataset(alpha,shape):
  print("Hello")
  i = 1
  j = 1
  path1 = f"alphanumeric/{alpha}"
  path2 = f"shapes/{shape}"
  while True and path1 != "alphanumeric/na":
        if not os.path.exists(path1+f'_{i}'):
            path1 = path1+f'_{i}'

            os.makedirs(path1)
            break
        else :
            i += 1
  while True and path2 != "shapes/na":
        if not os.path.exists(path2+f'_{j}'):
            path2 = path2+f'_{i}'
            os.makedirs(path2)
            break
        else :
            j += 1
  print(path1,path2)
  videoRunner(path1,path2)
    

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--alphanum', type=str, default='na', help='select alphanumeric')
  parser.add_argument('--shape', type=str,default="na", help='select shape')
  parser.add_argument('--port', type=int, default=0, help='select video-stream port number')
  args = parser.parse_args()
  alpha = args.alphanum
  shape = args.shape
  saveDataset(alpha,shape)
