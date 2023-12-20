<h1> How to download youtube videos with python </h1>


if you want to craete youtube downloader with python follow these steps
setp 1. first install pytube using pip install pytube in your terminal
step 2. import pytube 
step 3. copy the url of video and store into a variable (ex. url).
step 4. create object yt = YouTube(url)
step 5. selecting the video resolution 
     video = yt.streams.get_higest_resolution()

step 6. set the path where do you want to save that video
  out_dir = "your path"

step 7. setting up the name of the video
     file_name - yt.title+".mp4"

step 8. downloading of the video
     video.download(out_dir,file_name)

step 9. printing out success messages
