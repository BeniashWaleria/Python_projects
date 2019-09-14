import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import top_10 as t
y=t.top_val['Получено'].values.astype(float)
x = np.arange(1,11,1) 
coordinates=pd.DataFrame({'x':x,'ОТДЕЛЕНИЯ':t.top_val['ОТДЕЛЕНИЕ'], 'y':y})
fig,chart=plt.subplots(figsize=(13,5),tight_layout =True)
chart.set_xticks(x)
chart.set_xlabel('BANKS',fontsize=20)
chart.set_ylabel('BYN',fontsize=14)
chart.xaxis.grid(True)
chart.yaxis.grid(True)
plt.plot(x,y, linestyle = 'solid',marker='o', color="#6c1888")
info="\n".join((coordinates['x'].astype(str)+''+coordinates['ОТДЕЛЕНИЯ']).values)
coordinates.apply(lambda x: chart.annotate(x['y'], (x['x'] , x['y']),fontsize=12), axis=1)
chart.tick_params(axis='both', labelsize=12)
plt.gcf().text(0, -0.43,info, fontsize=14)
plt.show()