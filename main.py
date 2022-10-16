import playsound            #pip install playsound; https://www.delftstack.com/de/howto/python/python-play-mp3/
import time


try:

    #playsound.playsound('music.mp3')

    print("Shutdown PC in:")


    count = 0

    while count < 13:
        time.sleep(1)
        print(13 - count)
        count = count + 1


except Exception as err:
    print(err)




