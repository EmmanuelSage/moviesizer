from moviepy.video.io.VideoFileClip import VideoFileClip
from pathlib import Path

def getDuration(path):
    """
    Get the duration of a video file in seconds.

    Parameters:
    path (str): The path to the video file.

    Returns:
    int: Duration of the video in seconds.
    """
    dur = 0
    try:
        clip = VideoFileClip(path)
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
    """
    Process and print the duration in hours, minutes, and seconds.

    Parameters:
    dur (int): Total duration in seconds.
    """
    hrs, mins, secs = dur // 60 // 60, dur // 60 % 60, dur % 60
    hrs = "0" + str(hrs) if (hrs < 10) else str(hrs)
    mins = "0" + str(mins) if (mins < 10) else str(mins)
    secs = "0" + str(secs) if (secs < 10) else str(secs)

    print("Total length of video files: " + hrs + ":" + mins + ":" + secs)
    print("Full duration in seconds: " + str(dur))

def getVideosLength():
    """
    Calculate the total duration of all MP4 videos in a given directory.
    """
    dir_path = input("Enter the directory containing video files: ")
    pathlist = Path(dir_path).glob('**/*.mp4')

    print("Processing directories ............")

    duration = 0

    for path in pathlist:
        path_in_str = str(path)
        print("Processing file:", path_in_str)
        duration += getDuration(path_in_str)
        print("Current total duration: ", duration, "seconds")

    print("Directories processed :)")
    print("Returning result ........")

    processDuration(duration)

getVideosLength()

# Todo : Add more specific error handling for different scenarios
# Todo : Enhance user input validation and sanitization
