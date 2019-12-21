l=["Mathematics","DCC","ECAD","NUMERICAL TECHNIQUES","ELECTRONIC NETWORKS","PYTHON PROGRAMMING","DCC LAB","ECAD LAB","PYTHON LAB"]
m=[3,3,3,2,3,3,1,1,1]
while(True):
    s=0
    for i in range(len(l)):
        u=int(input("Enter the pointer for %s"%(l[i])))
        s=s+u*m[i]
    print("Pointer is ",s/sum(m))
    
