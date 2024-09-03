import requests
from bs4 import BeautifulSoup
import pandas as pd 
#single song webscrapping

url="https://www.tamil2lyrics.com/lyrics/aagaya-suriyanai-song-lyrics/"
response=requests.get(url)
soup = BeautifulSoup (response.text,'html.parser')
#print(soup.prettify)
#print(soup)
listings=soup.find('div',id="Tamil",class_="tabcontent")
contents=listings .find_all('p')
#print(len(contents))
#print(contents)

my_result = []
for content in contents:
    a=content.text
    my_result.append (
        {a}
            )
    print(my_result)

df= pd.DataFrame(my_result)
print(df)
df.to_csv("tamilsong.csv",index=False)
