import cv2
import numpy as np
img_gray = cv2.imread('lenna.jpg', 0)
cv2.imshow('lenna', img_gray)
key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()

def medianBlur(img, kernel, padding_way):
    size = img.shape
    h, w = size[0], size[1]
    m, n = kernel.shape
    padding_size = m-1  #I supposed m = n and are odds

    if padding_way == 'REPLICA':
        img_padded = np.pad(img, padding_size, 'edge')
    elif padding_way == 'ZERO':
        img_padded = np.pad(img, padding_size, 'constant')

    print(img_padded)

    img_median_blur = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            img_median_blur[i][j] = np.median(img_padded[i:i+m, j:j+n].flatten())
    return img_median_blur

kernel = np.ones((3, 3))

test_img1 = medianBlur(img_gray, kernel, 'REPLICA')
cv2.imwrite('Median_Blur_REPLICA.jpg', test_img1)

test_img2 = medianBlur(img_gray, kernel, 'ZERO')
cv2.imwrite('Median_Blur_ZERO.jpg', test_img2)