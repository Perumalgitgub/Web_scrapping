import requests
from bs4 import BeautifulSoup
Url= "https://www.panuval.com/enmakaje-10026709"
response=requests.get(Url)
soup = BeautifulSoup (response.text,'html.parser')
#print(soup.prettify)
#print(soup)
listings=soup.find_all(class_="tab-content")
print(len(listings))
print(listings)

'''
my_result = []
for listing in listings:
    name_list=listing.find('div',class_="name").text
    print(len (name_list))
    my_result.append(
        {"books name : ",name_list}
         )
    print(name_list)'''
    