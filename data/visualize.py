import cv2
import pickle

pkl_file = 'pointlines/00030043.pkl'
image_file = '/home/toby/Documents/berkeley/vision/wireframe/data/v1.1/train/00030043.jpg' 

img = cv2.imread(image_file)

with open(pkl_file, 'rb') as f:
    x = pickle.load(f)
    lines = x['lines']
    points = x['points']
    for idx, (i, j) in enumerate(lines, start=0):
        x1, y1 = points[i]
        x2, y2 = points[j]
        cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), [0, 255, 0], 2, cv2.LINE_8)
    
    cv2.imshow("PIC", img)
    cv2.waitKey(0)
