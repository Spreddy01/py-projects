import requests
import bs4
result=requests.get("URL of the page")
so=bs4.BeautifulSoup(result.text,'lxml')
so.select('.ImageThumbnail__overlay')
image_link=requests.get("LINK from the inspect in browser")
print(image_link.content)
f=open('Directory you want to download')
print(f.write(image_link.content))
f.close

