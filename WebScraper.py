from urllib.request import urlopen
from WordleMarathon import WordleMarathon


class WebScraper():
    def __init__(self, url = None):
        if url:
            self.url = url
        else:    
            self.url = "https://www.mit.edu/~ecprice/wordlist.10000"
    
    def Read(self):
        page = urlopen(self.url)
        html_bytes = page.read()
        self.html = html_bytes.decode("utf-8")
#        print(html)
 
    def to_list(self):
       list_of_words = self.html.split()
       valids = [word for word in list_of_words if len(word) == 5]
       #print (valids)
       return valids



def TestWebScraper():
    ws = WebScraper()
    ws.Read()
    list_of_words = ws.to_list()

    wm = WordleMarathon 
    wm.Play (list_of_words)




TestWebScraper()