import cv2
import numpy as np

image = cv2.imread('images/bunchofshapes.jpg')
cv2.imshow('0 - Original Image', image)
cv2.waitKey(0)

blank_image = np.zeros((image.shape[0], image.shape[1], 3))

orginal_image = image

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 200)
cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print ("Number of contours found = ", len(contours))

cv2.drawContours(blank_image, contours, -1, (0,255,0), 3)
cv2.imshow('2 - All Contours over blank image', blank_image)
cv2.waitKey(0)

cv2.drawContours(image, contours, -1, (0,255,0), 3)
cv2.imshow('3 - All Contours', image)
cv2.waitKey(0)

cv2.destroyAllWindows()


def get_contour_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

image = cv2.imread('images/bunchofshapes.jpg')
orginal_image = image

print ("Contor Areas before sorting, ") 
print (get_contour_areas(contours))

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print ("Contor Areas after sorting", )
print (get_contour_areas(sorted_contours))

for c in sorted_contours:
    cv2.drawContours(orginal_image, [c], -1, (255,0,0), 3)
    cv2.waitKey(0)
    cv2.imshow('Contours by area', orginal_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

def x_cord_contour(contours):
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return (int(M['m10']/M['m00']))
    else:
        pass

    
def label_contour_center(image, c):
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
 
    cv2.circle(image,(cx,cy), 10, (0,0,255), -1)
    return image

image = cv2.imread('images/bunchofshapes.jpg')
orginal_image = image.copy()

for (i, c) in enumerate(contours):
    orig = label_contour_center(image, c)
 
cv2.imshow("4 - Contour Centers ", image)
cv2.waitKey(0)

contours_left_to_right = sorted(contours, key = x_cord_contour, reverse = False)

for (i,c)  in enumerate(contours_left_to_right):
    cv2.drawContours(orginal_image, [c], -1, (0,0,255), 3)  
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(orginal_image, str(i+1), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('5 - Left to Right Contour', orginal_image)
    cv2.waitKey(0)
    (x, y, w, h) = cv2.boundingRect(c)  

    cropped_contour = orginal_image[y:y + h, x:x + w]
    image_name = "output_shape_number_" + str(i+1) + ".jpg"
    print (image_name)
    cv2.imwrite(image_name, cropped_contour)
    
cv2.destroyAllWindows()