import pandas as pd
import requests
import os
import io
import csv
import codecs

url='https://myfin.by/currency/minsk'
user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')
response = requests.get(url, headers={'User-Agent':user_agent}).content
data = pd.read_html(response)
dest_file=r'C:\Users\User\Desktop\currency_project\data_file.csv'
del data[0:2]
if os.path.exists(dest_file): 
    os.remove(dest_file)
    headers=['ОТДЕЛЕНИЕ','USD пок','USD прод','EUR пок','EUR прод','RUB пок','RUB прод']
    data_headers=pd.DataFrame(columns=headers)
    data_headers.to_csv(dest_file,encoding='utf-8-sig',sep=';',index=False)
with open(dest_file,'a') as file:
    for elem in data:
        elem.drop(elem.columns[[7,8]], axis=1,inplace=True)
        elem.drop_duplicates(subset=[elem.columns[0]],keep='first',inplace=True)
        divisions=elem.iloc[:,0]
        for el in divisions :
            new_val=elem.columns.values[0].replace("Отделения", " ")
            new_el=new_val+ " " + el
            divisions.replace(el,new_el,inplace=True)
        elem.to_csv(dest_file,encoding='utf-8-sig',sep=';',float_format='%.3f',mode='a',index=False,header=False)
print("Data saved to %s" % (dest_file))


    