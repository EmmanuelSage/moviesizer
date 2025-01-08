from moviepy.audio.io.AudioFileClip import AudioFileClip
from pathlib import Path

def getDuration(path):
    dur = 0
    try:
        clip = AudioFileClip(path)
        dur = int(clip.duration)
        clip.close()  # Close the clip to free resources
    except Exception as e:
        print("File Error ============================")
        print(path)
        print(f"Error: {e}")
        print("File Error ============================")
    finally:
        return dur

def processDuration(dur):
    hrs, mins, secs = dur // 60 // 60, dur // 60 % 60, dur % 60
    hrs = "0" + str(hrs) if (hrs < 10) else str(hrs)
    mins = "0" + str(mins) if (mins < 10) else str(mins)
    secs = "0" + str(secs) if (secs < 10) else str(secs)

    print("Total length of audio files: " + hrs + ":" + mins + ":" + secs)
    print("Full duration in seconds: " + str(dur))

def getAudiosLength():
    pathlist = Path(input("Enter the directory containing audio files: ")).glob('**/*.mp3')

    print("Processing directories ............")

    duration = 0

    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        print(path_in_str)
        duration += getDuration(path_in_str)
        print("Current total duration: ", duration, "seconds")

    print("Directories processed :)")
    print("Returning result ........")

    processDuration(duration)

getAudiosLength()

# Todo : Add doc strings
# Todo : Sanitize input
# Todo : add try catch and error handling
# Todo : fix error (Exception ignored in: <function FFMPEG_AudioReader.__del__ at 0x081646A8>)
