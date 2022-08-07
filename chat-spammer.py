import pyautogui
import time
time.sleep(5)
words=open('word.txt','r')
for i in range(74):
    word=words.readline()
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    time.sleep(1)
words.close()
print('Sussfully completed')