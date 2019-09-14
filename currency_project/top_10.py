import pandas as pd
import numpy as np
import convert 
import data_to_csv as dat
data=pd.read_csv(dat.dest_file,encoding='utf-8-sig',sep=';')
pd.set_option('display.max_columns', 9)
pd.set_option('display.width', 3000) 
usd_val=data['USD пок'].values.tolist()
eur_val=data['EUR пок'].values.tolist()
rub_val=data['RUB пок'].values.tolist()
curr_set=zip(usd_val,eur_val,rub_val)
result_set=[]
file_path=r'C:\Users\User\Desktop\currency_project\top_10.csv'
for e,u,r in curr_set:
    value=convert.func(e,u,r)
    result_set.append(value)
data.insert(len(data.columns), 'Получено', result_set, allow_duplicates = True)
data.sort_values(by='Получено',ascending=False,inplace=True)
#исключение дубликатов,поскольку большую ценность представляет не разнообразие филиалов одного банка,а вариация курсов в разных банках
data.drop_duplicates(subset=['Получено'],keep='first',inplace=True)
top_val=data[:10]
top_val.to_csv(file_path,encoding='cp1251',sep=';',float_format='%.3f',mode='w',header=True,index=False)
print("TOP 10 bank divisions for currency exchange performance:\n",top_val)