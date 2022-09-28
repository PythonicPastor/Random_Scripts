import cv2
imgName = 'PyQR.png'
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread(imgName))
exec(val)
saveToPy(imgName, 'PyQR.py')

strVal = codeToString()
print(strVal)
