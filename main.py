
import playsound            #pip install playsound; https://www.delftstack.com/de/howto/python/python-play-mp3/
import time                 #https://docs.python.org/3/library/time.html
import os                   #https://rdrr.io/cran/installr/man/os.shutdown.html
import threading            #https://docs.python.org/3/library/threading.html



#https://stackoverflow.com/questions/47316266/can-i-display-image-in-full-screen-mode-with-pil
import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()



try:
    #PLAY Outrosoundtrack
    def music():
        playsound.playsound('music.mp3')


    #COUNT FROM 15 to 1, than shutdown the pc
    def consol_output():
        count = 0
        while count < 15:
            time.sleep(1)
            print(f'Shutdown PC in: {15 - count}')
            count = count + 1
        print('BYE BYE')
        threading.Thread(target=picture).start()
        threading.Thread(target=shutdown).start()

    #SHUTDOWN the pc function
    def picture():
        showPIL(Image.open("bluescreen.png"))

    def shutdown():
        time.sleep(10)
        os.system('shutdown /s /t 1')

    threading.Thread(target = music).start()
    threading.Thread(target =  consol_output).start()


except Exception as err:
    print(err)




