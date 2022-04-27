import cv2
import re
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
	
	rawCapture.truncate(0)  

	if key == ord("s"):
		text = pytesseract.image_to_string(image)
		text = text.replace(' ','')
		sn = text
		ka = text
		serialNumber = re.findall(r'[2-2][0-5][0-9][0-9]{5}\/[0-9]{4}', sn)
		kodeAktivasi = re.findall(r'[A-Z]{4}[0-9]{6}', ka)
		print(text)
		for sn in serialNumber:
			print(sn)
		for ka in kodeAktivasi:
			print(ka)
			
			
		report = open('hasil-scan.txt','a')
		report.write("<html>")
		report.write(sn + "\n")
		report.write(ka + "\n")
		report.write("</html>")
		report.close()
		cv2.imshow("Frame", image)
		cv2.waitKey(0)
		break

cv2.destroyAllWindows()