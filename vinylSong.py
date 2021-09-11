import detectSong
import time

while True:
    songPlaying = detectSong.detectSongFun()
    # update the song playing on display
    time.sleep(30)
