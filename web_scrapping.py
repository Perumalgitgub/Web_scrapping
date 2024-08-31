import requests
from bs4 import BeautifulSoup
import pandas as pd 


# Making a GET request
url='https://www.noolulagam.com/'
r = requests.get(url)
soup = BeautifulSoup (r .text,'html.parser')
#print(soup.prettify)
check=soup .find_all(class_="single-item") 
#print(len(check))
#print(check)
#checks=check[0]
#print(checks)
book=[]
for checks in check:
    book_name=(checks.find("h5").find("font",class_="title").text)
    book_price=(checks.find("h5").find("font",class_="price").text)
    book.append(
        {"book name":book_name,"book price: ": book_price}
        )
    print(book)
df= pd.DataFrame(book)
print(df)
#df.to_csv("books_name.csv",index=False)