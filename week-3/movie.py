import urllib.request as req
import bs4

goodTitles=[]
normalTitles=[]
badTitles=[]

def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    for title in titles:
        if title.a != None and "[好雷]" in title.a.string:
            goodTitles.append(title.a.string)
        elif title.a != None and "[普雷]" in title.a.string:
            normalTitles.append(title.a.string)
        elif title.a != None and "[負雷]" in title.a.string:
            badTitles.append(title.a.string)

    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

def title():
    pageURL="https://www.ptt.cc/bbs/movie/index.html"
    count=0
    while count<10:
        pageURL="https://www.ptt.cc"+getData(pageURL)
        count+=1

title()
with open("movie2.txt","a",encoding="utf-8") as file:
    for good in goodTitles:
        file.write(good+"\n")
    for normal in normalTitles:
        file.write(normal+"\n")
    for bad in badTitles:
        file.write(bad+"\n")
