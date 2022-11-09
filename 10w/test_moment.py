import cv2
import numpy as np

def cal_moment(img, i, j):
    M = 0
    for a in range(img.shape[0]):
        for b in range(img.shape[1]):
            M += (a)**j*(b)**i*img[a,b]
    return M    

img = cv2.imread("sourcefiles-git/10w/line1.png", cv2.IMREAD_GRAYSCALE)

if img is not None:
   
  print('img shape : ', img.shape)

  cv2.imshow("img", img)
  y, x = img.shape
  print('x={}, y={}'.format(x,y))
  y_u = int(y/3)

  img_seg1 = img[:y_u,:]
  img_seg2 = img[y_u:y_u*2,:]
  img_seg3 = img[y_u*2:y_u*3,:]    

  sum_val = 0

  M_seg1 = [cal_moment(img_seg1, 0, 0), cal_moment(img_seg1, 1, 0)/cal_moment(img_seg1, 0, 0)\
    , cal_moment(img_seg1, 0, 1)/cal_moment(img_seg1, 0, 0)]
  M_seg2 = [cal_moment(img_seg2, 0, 0), cal_moment(img_seg2, 1, 0)/cal_moment(img_seg2, 0, 0)\
    , cal_moment(img_seg2, 0, 1)/cal_moment(img_seg2, 0, 0)]
  M_seg3 = [cal_moment(img_seg3, 0, 0), cal_moment(img_seg3, 1, 0)/cal_moment(img_seg3, 0, 0)\
    , cal_moment(img_seg3, 0, 1)/cal_moment(img_seg3, 0, 0)]

  print('M_seg1', M_seg1)
  print('M_seg2', M_seg2)
  print('M_seg3', M_seg3)
  
  M_seg1 = np.array(M_seg1).astype(np.uint16)
  M_seg2 = np.array(M_seg2).astype(np.uint16)
  M_seg3 = np.array(M_seg3).astype(np.uint16)

  img_seg1_color = np.zeros([y_u, x, 3])
  img_seg1_color[:,:,0] = img_seg1
  img_seg1_color[:,:,1] = img_seg1
  img_seg1_color[:,:,2] = img_seg1    

  img_seg2_color = np.array(img_seg2)
  img_seg2_color = np.expand_dims(img_seg2_color, axis=2)
  img_seg2_color = np.tile(img_seg2_color, (1,1,3))

  img_seg3_color = np.array(img_seg3)
  img_seg3_color = np.expand_dims(img_seg3_color, axis=2)
  img_seg3_color = np.tile(img_seg3_color, (1,1,3))

  img_seg1_cc = cv2.cvtColor(img_seg1, cv2.COLOR_GRAY2BGR)
  print('img_seg1_cc', img_seg1_cc.shape)
  print(img_seg2.shape)
  print(img_seg2_color.shape)
  print(M_seg1[1],M_seg1[2])
  cv2.circle(img_seg1_color, (M_seg1[1],M_seg1[2]), 3, (0,0,255),-1)
  cv2.circle(img_seg2_color, (M_seg2[1],M_seg2[2]), 3, (0,0,255),-1)
  cv2.circle(img_seg3_color, (M_seg3[1],M_seg3[2]), 3, (0,0,255),-1)
  cv2.imshow("img_seg1_color", img_seg1_color)
  cv2.imshow("img_seg2_color", img_seg2_color)
  cv2.imshow("img_seg3_color", img_seg3_color)

  contours, _ = cv2.findContours(img_seg1, 1, cv2.CHAIN_APPROX_NONE)
  c = max(contours, key=cv2.contourArea)
  M = cv2.moments(c)
  cx = M['m10']/M['m00']
  cy = M['m01']/M['m00']
  print(cx, cy)

  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
    print("Image file not found")



