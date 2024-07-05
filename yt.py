import pytube
site=input("LINK HERE")
yt=pytube.YouTube(site)
print(yt.title)
print(yt.length)
print(yt.views)
yt.streams.first().download()
yt.streams.first().download()
print('DOWNLOAD',site)