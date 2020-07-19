from plyer import notification
from time import sleep
import requests
from bs4 import BeautifulSoup



def notifime(title, message):
    notification.notify(
        title = title,
        message = message,
        #app_icon = "E://program//icon.ico",
        timeout = 15
    )
def  getData(url):
    try:   
        r = requests.get(url)
        return r.text
    except:
        print("No Internet Connection")


if __name__ == "__main__":
    while True:
        
        try:
        
            while True:
                myHtmlData = getData('https://www.mohfw.gov.in/')
                soup = BeautifulSoup(myHtmlData, 'html.parser')
                myDataStr = " "
                for tr in soup.find_all('tbody'):
                    myDataStr += tr.get_text()
                    myDataStr = myDataStr[3:]
                    itemList = myDataStr.split("\n\n\n")
                    states = ['Delhi', 'Maharashtra', 'Uttar Pradesh']
                for item in itemList[0:35]:
                    dataList =item.split('\n')
                    #print(dataList)
                    if dataList[1] in states:
                        nTitle = 'Cases of Covid-19'
                        nText = f" States: {dataList[1]}\n Confirmed Cases: {dataList[2]}\n Cured: {dataList[3]}\n Deaths: {dataList[4]}"
                        notifime(nTitle,nText)
                        sleep(10)
                sleep(1800)

        except:
            print("Make sure you are connected to internet")
            sleep(8)







