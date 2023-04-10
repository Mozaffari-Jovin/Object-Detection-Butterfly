import cv2
import numpy as np

img = cv2.imread("pic.jpeg") # load picture

# cv2.imshow("Image", img) # show the image
# cv2.waitKey(0) # wait for 0 second
# cv2.destroyAllWindows() # close all windowds
# print(img.shape) # (896, 1600, 3) 869 rows and 1600 columns

# template = img[626:685, 972:1030] # the area for the butterfly 
# cv2.imshow("Image", template) # show the image
# cv2.waitKey(0) # wait for 0 second
# cv2.destroyAllWindows() # close all windowds
# cv2.imwrite("template.jpeg", template) # save file

template = cv2.imread("template.jpeg")
# print(template.shape) # (59, 58, 3)

tmp_float = np.float32(template) # template is originally a uint8

# slide the template over the pic 
img_h, img_w = img.shape[:2] # img.shape is a tuple
tmp_h, tmp_w = template.shape[:2]

# print(img_h, img_w, tmp_h, tmp_w) # 896 1600 59 58

mat_sum_min = 3 * tmp_w * tmp_h * 255
for i in range(img_h-tmp_h): # rows
	for j in range(img_w-tmp_w): # columns
		little_window = img[i:i+tmp_h, j:j+tmp_w]

		wnd_float = np.float32(little_window) # little_window is originally a uint8
	# 	wnd_resize = cv2.resize(little_window, None, fx=3, fy=3) # to have a better display
	# 	cv2.imshow("Image", wnd_resize)
	# 	q = cv2.waitKey(1)

	# 	if q == ord('q'):
	# 		break
	# if q == ord('q'):
	# 	break

		mat_diff = tmp_float - wnd_float

		# mat_diff = template - little_window
		# print(mat_diff[0, 0], template[0, 0], little_window[0, 0])
		# print(mat_diff[0, 0], tmp_float[0, 0], wnd_float[0, 0])
		# quit()
		# mat_diff becomes zero when template is completely conincident with little_window
		mat_diff_abs = np.abs(tmp_float - wnd_float)
		mat_sum = mat_diff_abs.sum()
		# print(mat_sum)
		# quit()

		if mat_sum < mat_sum_min:
			mat_sum_min = mat_sum
			i_min = i
			j_min = j

# print(i_min, j_min)

cv2.rectangle(img, (j_min, i_min), (j_min+tmp_w, i_min+tmp_h), (255, 0, 0), 2)
cv2.imshow("Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()