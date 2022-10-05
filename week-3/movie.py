import urllib.request as req
import bs4

def getData1(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    for title in titles:
        if title.a != None and "[好雷]" in title.a.string:
                with open("movie.txt", mode="a", encoding="utf-8") as file:
                    file.write(title.a.string+"\n")
                
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

def titleGood():
    pageURL="https://www.ptt.cc/bbs/movie/index.html"
    count=0
    while count<10:
        pageURL="https://www.ptt.cc"+getData1(pageURL)
        count+=1

def getData2(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    for title in titles:
        if title.a != None and "[普雷]" in title.a.string:
            with open("movie.txt", mode="a", encoding="utf-8") as file:
                file.write(title.a.string+"\n")
                
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

def titleNormal():
    pageURL="https://www.ptt.cc/bbs/movie/index.html"
    count=0
    while count<10:
        pageURL="https://www.ptt.cc"+getData2(pageURL)
        count+=1

def getData3(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")

    for title in titles:
        if title.a != None and "[負雷]" in title.a.string:
            with open("movie.txt", mode="a", encoding="utf-8") as file:
                file.write(title.a.string+"\n")
                
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"]

def titleBad():
    pageURL="https://www.ptt.cc/bbs/movie/index.html"
    count=0
    while count<10:
        pageURL="https://www.ptt.cc"+getData3(pageURL)
        count+=1

titleGood()
titleNormal()
titleBad()