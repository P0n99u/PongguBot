from urllib.request import urlopen
from bs4 import BeautifulSoup

def GetEventBorad():
    MapleEvent="https://maplestory.nexon.com/News/Event/Ongoing/"
    html = urlopen(MapleEvent)
    bs4=BeautifulSoup(html,"html.parser")
    tagList=bs4.findAll('a')
    for tag in tagList:
        if "썬데이메이플" in tag:
            return MapleEvent+tag.get('href')[-3:]
    print("썬데이 공지가 안 올라왔거나 오류가 발생했습니다")
    return -1

def GetSundayInfo():
    SundayURL=GetEventBorad()
    if(SundayURL==-1):
        return "썬데이 공지가 아직 안올라왔습니다?"    
    html = urlopen(SundayURL)
    bs4=BeautifulSoup(html,'html.parser') 
    tagList=bs4.findAll('img')
    for tag in tagList:
        if tag.get('alt') == "썬데이 메이플!" :
            return tag.get('src')

    print("오류가 발생했다")
    return "오류가 발생했습니다"
