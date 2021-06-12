import numpy as np  # module import
import pandas as pd
import requests
import datetime as dt
import copy
import matplotlib.pyplot as plt

a = pd.read_csv('/content/drive/MyDrive/봄철/2018-03.csv', encoding='cp949')
b = pd.read_csv('/content/drive/MyDrive/봄철/2018-04.csv', encoding='cp949')
c = pd.read_csv('/content/drive/MyDrive/봄철/2018-05.csv', encoding='cp949')
d = pd.read_csv('/content/drive/MyDrive/봄철/2019-03.csv', encoding='cp949')
e = pd.read_csv('/content/drive/MyDrive/봄철/2019-04.csv', encoding='cp949')
f = pd.read_csv('/content/drive/MyDrive/봄철/2019-05.csv', encoding='cp949')
g = pd.read_csv('/content/drive/MyDrive/봄철/2020-03.csv', encoding='cp949')
h = pd.read_csv('/content/drive/MyDrive/봄철/2020-04.csv', encoding='cp949')
i = pd.read_csv('/content/drive/MyDrive/봄철/2020-05.csv', encoding='cp949')

l = pd.concat([a,b,c,d,e,f,g,h,i])

l = l.drop(['시도','측정소코드','날짜'], axis=1)

gu = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']

for i in range(25) :
  l[l['측정소명']==gu[i]].to_csv(gu[i]+'.csv')
