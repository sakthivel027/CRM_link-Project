views.py files
Numpy
import numpy as np
bmi=np.array([21.34,22.34,32.56,1.45,26.87])
print(bmi)
print(type(bmi))
print(bmi<21)
print(bmi>21)
print(np.logical_and(bmi<21 ,bmi>21))
[21.34 22.34 32.56  1.45 26.87]
<class 'numpy.ndarray'>
[False False False  True False]
[ True  True  True False  True]
[False False False False False]
print(np.logical_and(brics['area']>4,brics['population']>200))
br    False
in     True
ru    False
ch     True
sa     True
Name: area, dtype: bool
print(brics[np.logical_and(brics['area']>4,brics['population']>200)])
         country    capital  area  population
in         india  new delhi   4.6         300
ch         china    beijing   5.6         500
sa  south africa   pretoria   8.4         399
for i in brics:
    print(i)
country
capital
area
population
for lab,row in brics.iterrows():
    print(lab)
    print(row)
    print()
br
country         brazil
capital       brazilia
area               7.5
population         200
Name: br, dtype: object

in
country           india
capital       new delhi
area                4.6
population          300
Name: in, dtype: object

ru
country       russia
capital       moscow
area             3.5
population       130
Name: ru, dtype: object

ch
country         china
capital       beijing
area              5.6
population        500
Name: ch, dtype: object

sa
country       south africa
capital           pretoria
area                   8.4
population             399
Name: sa, dtype: object

for lab,row in brics.iterrows():
    brics.loc[lab,"name_length"]=len(row['country'])
    print(brics)
    print()
         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12

         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12

         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12

         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12

         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12

brics['name_length']=brics['country'].apply(len)
print(brics)
         country    capital  area  population  name_length
br        brazil   brazilia   7.5         200            6
in         india  new delhi   4.6         300            5
ru        russia     moscow   3.5         130            6
ch         china    beijing   5.6         500            5
sa  south africa   pretoria   8.4         399           12
np.random.seed(123)
print(np.random.rand())
0.6964691855978616
np.random.seed(123)
print(np.random.rand())
0.6964691855978616
print(np.random.rand())
0.28613933495037946
print(np.random.random(size=4))
[0.7887235  0.28884082 0.84907152 0.42329787]
print(np.random.randint(0,2))
1
import pandas as pd
total=0
for chunk in pd.read_csv('http://0.0.0.0:8000/Desktop/planet.csv',chunksize=1000):
    total+=sum(chunk['a'])    
print(total)

