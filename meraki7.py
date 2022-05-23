f=open("bio.txt","w")
f.write("Name Abhishek\nDesignation CEO of navgurukul\nGender male\nAge 29")
f.close()

import json
file=open("bio.txt","r")
d={}
for k in file.readlines():
    str=""
    count=0
    for i in k:
        if i==" ":
            d[str]=k[count+1:len(k)-1]
            break
        else:
            str+=i
            count+=1
print(d)



