mods = ['cv2', 'qrcode', 'pyperclip']
for mod in mods:
    exec('import ' + mod)

def makeImg(val, imgName):
    img = qrcode.make(val)
    img.save(imgName)
def decImg(imgName):
    d = cv2.QRCodeDetector()
    val, points, straight_qrcode = d.detectAndDecode(cv2.imread(imgName))
    return val
def saveToPy(imgName, scriptName):
    #write to pyscript
    img = decImg(imgName)
    with open(scriptName, "w") as text_file:
        text_file.write("{}".format(img))
def codeToString():
    lines = pyperclip.paste()
    return lines
def runQR(imgName):
    img = decImg(imgName)
    exec(img)