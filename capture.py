import cv2

video = cv2.VideoCapture(0)
roll = '85'
frame_no = 0
print("Capturing ")
while True:
	
	_,frame = video.read()		#1st is the boolean, 2nd array of image

	cv2.imshow("Capturing",frame)
	key = cv2.waitKey(1)
	
	if frame_no == 200:
		break
		
	if frame_no % 10 == 8 or frame_no % 10 == 9:
		cv2.imwrite('dataset/' + roll + '/test_set/'+str(frame_no)+'.jpg', frame)
	else:
		cv2.imwrite('dataset/' + roll + '/training_set/'+str(frame_no)+'.jpg', frame)
	
	frame_no = frame_no + 1

print(frame_no)
video.release()
cv2.destroyAllWindows()