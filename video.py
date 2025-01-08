from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path

def getDuration(path):
    dur = 0
    try:
        clip = VideoFileClip(path)
        dur = int(clip.duration)
    except:
        print("File Error ============================")
        print(path)
        print("File Error ============================")
    finally:
        return dur

def processDuration(dur):
    hrs, mins, secs = dur//60//60, dur//60%60, dur%60
    hrs = "0"+str(hrs) if(hrs<10) else str(hrs)
    mins = "0"+str(mins) if(mins<10) else str(mins)
    secs = "0"+str(secs) if(secs<10) else str(secs)

    print("Length of the video: "+ hrs +":"+ mins +":"+ secs)
    print("Full duration of the video: " + str(dur))



def getVideosLength():
    pathlist = Path(input("Enter the video filename (with extn.): ")).glob('**/*.mp4')

    print("Processing directories ............")

    duration = 0

    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        print(path_in_str)
        duration += getDuration(path_in_str)
        print("Current Duration is : ", duration)

    print("Directories processed :)")
    print("returning result ........")

    processDuration(duration)

getVideosLength()


# Todo : Add doc strings
# Todo : Sanitize input
# Todo : add try catch and error handling
# Todo : fix error (Exception ignored in: <function FFMPEG_AudioReader.__del__ at 0x081646A8>)