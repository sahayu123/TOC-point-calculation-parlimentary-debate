import requests
from bs4 import BeautifulSoup
class Calculate_Toc:
    def __init__(self,entries_url):
        print("Invite Link : ",entries_url)
        lnk=entries_url.split("/")
        #print(lnk)
        change=lnk[5].split(".")
        change[0]="fields"
        #print(change)
        lnk[5]=change[0]+"."+change[1]
        #print(lnk)
        link=""
        count=1
        for item in lnk:
            if count<len(lnk):
                #print(count,len(lnk))
                link=link+item+"/"
                count=count+1
            else:
                link=link+item
        print("Entries Link : ",link)
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('a')
            for p in paragraphs:
                txt=p.get_text(strip=True)
                if txt=="Novice Parli":
                    self.novice_url="https://tabroom.com"+p.get("href")
                    print("Novice Entries Link : ",self.novice_url)
                elif txt=="Open Parli":
                    self.open_url="https://tabroom.com"+p.get("href")
                    print("Open Entries Link : ", self.open_url)
                else:
                   continue
        else:
            print("Failed to retrieve the webpage")

        self.afs_place_points = {
        (10, 11): (17, 11, 7),   
        (12, 13): (18,12,8),   
        (14, 16): (19,14,9),   
        (17, 19): (20,14,10,6),  
        (20, 22): (21,15,11,7),  
        (23, 27): (22,16,12,8), 
        (28, 32): (23,17,13,9), 
        (33, 38): (24,18,14,10,6), 
        (39, 45): (25,19,15,11,7),  
        (46, 54): (26,20,16,12,8),  
        (55, 64): (27,21,17,13,9),  
        (65, 77): (28,22,18,14,10,6), 
        (78, 91): (29,23,19,15,11,7),  
        (92, 109): (30,24,20,16,12,8),  
        (110, 129): (31,25,21,17,13,9),   
        (130, 154): (32,26,22,18,14,10,6),
        (155, 183): (33,27,23,19,15,11,7),  
        (184, 218): (34,28,24,20,16,12,8),   
        (219): (35,29,25,21,17,13,9)        
    }
    def tabroom_get_entries(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('h5')
            entries_string=paragraphs[2].text.strip()
            amount_entries=entries_string[0:2]
            return amount_entries
        else:
            return "Failed to retrieve the webpage"
    def get_toc_points(self): 
        novice_entries=self.tabroom_get_entries(self.novice_url)
        print("Novice Entries : ", novice_entries)
        open_entries=self.tabroom_get_entries(self.open_url)
        print("Open Entries : ", open_entries)
        afs=(int(novice_entries)+int(open_entries))/3
        print("AFS "+str(afs))
        for point in self.afs_place_points.keys():
            try:
                if point[0] <= afs <= point[1]:
                    return self.afs_place_points[point]
                else:
                    continue 
            except:
                if point[0] <= afs :
                    return self.afs_place_points[point]
                else :
                    print("No data found")
                    break
url="https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=30494"
#Url for NPDL NATIONALS AND NOVICE NATIONALS
check=Calculate_Toc(url)
print(check.get_toc_points())






