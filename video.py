from moviepy.video.io.VideoFileClip import VideoFileClip

print("Notice: Enter the address :")

clip = VideoFileClip(input("Enter the video filename (with extn.): "))
dur = int(clip.duration)
hrs, mins, secs = dur//60//60, dur//60%60, dur%60
hrs = "0"+str(hrs) if(hrs<10) else str(hrs)
mins = "0"+str(mins) if(mins<10) else str(mins)
secs = "0"+str(secs) if(secs<10) else str(secs)

print("Length of the video: "+ hrs +":"+ mins +":"+ secs)