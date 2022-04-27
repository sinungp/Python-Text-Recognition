import cv2
import pytesseract

url='http://192.168.0.110:8080/video'
cam = cv2.VideoCapture(url)


#Saat menggunakan Smartphone pakai Frame50
def rescale_frame(frame, percent=50):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

cv2.namedWindow("test")

img_counter = 0

#Jika menggunakan kamera USB
# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("test", frame)

#Jika menggunakan kamera url
while True:
    ret, frame = cam.read()
    frame50 = rescale_frame(frame, percent=50)
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame50)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        imgH, imgW,_ = frame.shape

        x1,y1,w1,h1=0,0,imgH,imgW

        imgchar = pytesseract.image_to_string(frame)

        imgboxes= pytesseract.image_to_boxes(frame)
        for boxes in imgboxes.splitlines():
            boxes=boxes.split(' ')
            x,y,w,h=int (boxes[1]),int (boxes[2]),int (boxes[3]),int (boxes[4])
            cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,0,255),3)
        
        cv2.putText(frame,imgchar,(x1+int(w1/50),y1+int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        font=cv2.FONT_HERSHEY_SIMPLEX

        img_name = "/home/it_gogo/belajar/Serius/Scan-code/Hasil Foto Objek/opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        print("Hasil Pembacaan Adalah")
        print(imgchar)

cam.release()
cv2.destroyAllWindows()