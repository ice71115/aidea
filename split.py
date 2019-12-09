import os
dirpath=r"./darknet-master/JPEGImages"

data=["C:/Users/dcn_dp01/GitHub/darknet-master/JPEGImages/"+i+"\n" for i in os.listdir(dirpath)]
train=[data[i] for i in range(len(data)) if i<2200]
test=[data[i] for i in range(len(data)) if i>=2200]
print(len(train),len(test))
f=open('./train.txt','w')
f.writelines(train)
f=open('./test.txt','w')
f.writelines(test)
