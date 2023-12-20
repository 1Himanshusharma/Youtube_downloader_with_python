<h1> How to download youtube videos with python </h1>


if you want to craete youtube downloader with python follow these steps <br>
setp 1. first install pytube using pip install pytube in your terminal<br>
step 2. import pytube <br>
step 3. copy the url of video and store into a variable (ex. url).<br>
step 4. create object yt = YouTube(url)<br>
step 5. selecting the video resolution <br>
     video = yt.streams.get_higest_resolution()<br>

step 6. set the path where do you want to save that video<br>
  out_dir = "your path"<br>

step 7. setting up the name of the video<br>
     file_name - yt.title+".mp4"<br>

step 8. downloading of the video<br>
     video.download(out_dir,file_name)<br>

step 9. printing out success messages<br>
