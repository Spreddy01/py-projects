#youtube videos download in highest quality
from pytube import YouTube
link = input("Enter the link of the video: ")
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ", yt.length)
print("Rating: ", yt.rating)
ys = yt.streams.get_highest_resolution()
ys.download()
print("Download completed")
