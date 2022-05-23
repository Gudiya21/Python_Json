import json
a=[['neelam','programer','24','2400'],['komal','trainer','24','20000'],['anuradha','HR','25','40000'],['Abhishek','manager','29','63000']]
list=['Name','Designation','Age','Salary']
dic={}
c=1
for i in a:
    dic2={}
    c1=0
    for j in i:
        dic2[list[c1]]=j
        c1+=1
    dic["emp"+str(c)]=dic2
    c+=1
print(dic)








    


