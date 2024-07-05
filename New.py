from pytube import YouTube

url = "https://youtu.be/kca0cG9fiQw?si=wMbD3H5Qp9GSPr3G"

video = YouTube(url)

video.streams.first().download("C:\Users\selen\Downloads")