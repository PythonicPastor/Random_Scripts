import pyautogui as pg
import pyperclip as pclip
import time
print('click on text file')
time.sleep(10)
#file1 = open('text.txt', 'r')
#lines = file1.readlines()
lines = pclip.paste()

for line in lines:
    for char in range(len(line)):
        pg.write(line[char])
        time.sleep(0.005)
    #pg.press('Enter')
print('done')
