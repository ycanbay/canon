import numpy as np
import csv
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import anonymizer as mn

with open("diabetic.csv") as f:
    mylist = []
    for row in csv.reader(f, delimiter=","):
        i=0
        for x in row:
            if x*1 != x:
                print( "warning")
            x=int(x)
            row[i]=x
            i=i+1
        mylist.append(row)


y = MinMaxScaler(copy=True, feature_range=(0, 1)).fit(mylist)
y = y.transform(mylist)
XList = y.tolist()

for k in [5,10,20,30,40,50,60,70]:
    result = mn.get_result(XList, k)
    print((k,result[0], result[1], result[2]))




