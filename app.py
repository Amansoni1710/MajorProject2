from dis import disco
import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


link= ['https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29','https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off','https://www.flipkart.com/search?q=phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
discounts = []
orignalPrices = []

# warranty = [] 
for p in range(len(link)):
    page = requests.get(link[p])
    soup = bs(page.content, 'html.parser')


    for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        discount = data.find('div', attrs={'class':'_3Ay6Sb'})
        orignalPrice = data.find('div', attrs={'class':'_3I9_wc _27UcVY'})
        if (names and price and rating and discount and orignalPrice):
            products.append(names.text) # Add product name to list
            prices.append(price.text) # Add price to list
            ratings.append(rating.text)   #Add rating specifications to list
            discounts.append(discount.text)
            orignalPrices.append(orignalPrice.text)

#printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
print(len(discount))

# # print(len(apps))
# # print(len(warranty))
# print(len(os))
# print(len(hd))

df = pd.DataFrame({"Product Name":products,"Rating":ratings,"Price":prices,"OrignalPrice":orignalPrices,"Discount":discounts})
print(df)
df_new = df[df['Product Name'] == 'APPLE iPhone 11 (White, 128 GB)']
print(df_new)
