import pyautogui
from win10toast import ToastNotifier
import time
time.sleep(5)
words=open('word.txt','r')
notify=ToastNotifier()
for i in range(6):
    word=words.readline()
    pyautogui.typewrite(word)
    pyautogui.press('enter')
notify.show_toast(
    title='Spam Complete',
    msg='The Script has been run Successfully',
    #icon_path='icon.png',
    duration=5
    )   
words.close()
print('Sussfully completed')