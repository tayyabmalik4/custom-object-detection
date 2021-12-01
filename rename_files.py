import os
count =0
# path = 'D:\machine learning practice\Train Model\custom_data'
for i in os.listdir():
    os.rename(i,str(count)+'.'+i.split('.')[-1])
    count +=1