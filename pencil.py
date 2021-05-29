import cv2

img_rgb = cv2.imread("leo.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

img_gray_inv = 255 - img_gray
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
                            sigmaX=0, sigmaY=0)

def dodgeV2(image, mask):
  return (cv2.divide(image, 255-mask, scale=256))

def burnV2(image, mask):
  return (255 - cv2.divide(255-image, 255-mask, scale=256))

img_blend = dodgeV2(img_gray, img_blur)

cv2.imwrite('result.jpg',img_blend)




