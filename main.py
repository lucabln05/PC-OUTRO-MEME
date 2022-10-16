
import playsound            #pip install playsound; https://www.delftstack.com/de/howto/python/python-play-mp3/
import time                 #https://docs.python.org/3/library/time.html
import os                   #https://rdrr.io/cran/installr/man/os.shutdown.html
import threading            #https://docs.python.org/3/library/threading.html


try:

    print("Shutdown PC in:")

    #PLAY Outrosoundtrack
    def music():
        playsound.playsound('music.mp3')

    #COUNT FROM 15 to 1, than shutdown the pc
    def consol_output():
        count = 0
        while count < 15:
            time.sleep(1)
            print(15 - count)
            count = count + 1
        print('BYE BYE')
        shutdown()

    #SHUTDOWN the pc function
    def shutdown():
        os.shutdown(s=0, m=0, h=0)




    threading.Thread(target = music).start()
    threading.Thread(target =  consol_output).start()


except Exception as err:
    print(err)




