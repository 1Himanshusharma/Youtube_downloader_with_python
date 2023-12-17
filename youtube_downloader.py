from pytube import YouTube

#creating the youtube video URL
url = r"https://www.youtube.com/watch?v=tOo5Rn8dRaA"


#create a Youtube obeject with the url
yt = YouTube(url)

#selct the highest resolution video
video = yt.streams.get_highest_resolution()

#set the output dir
out_dir = r"C:\Users\himan\OneDrive - Lovely Professional University\Desktop"

filename = yt.title+".mp4"

#download the video
video.download(out_dir,filename)
print(f"Download complete: {filename}")