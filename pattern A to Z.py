#%% A pattern
for i in range(6):
    for j in range(7):
        if ((j==2 or j==3 or j==4) and i==0) or (j==1 and i!=0) or (j==5 and i!=0)or (j!=0 and j!=6 and i==3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")    

    print()        

#%% E
for i in range(8):
    for j in range(7):
        if ((j!=0 or j!=5 or j!=6 ) and (i==0 and j!=0) or (i==3 and j!=0) or (i==6 and j!=0) or j==1) :
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()  

#%% F
for i in range(7):
    for j in range(7):
        if ((j!=0 or j!=5 or j!=6 ) and (i==0 and j!=0) or (i==3 and j!=0)  or j==1) :
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()    

#%% A

for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and (i!=0)) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")    

    print()     
#%% B


for i in range(5):
    for j in range(6):
        if (j==0) or ((i==0 or i==2 or i==4) and j<5) or ((i!=0 and i!=2 and i!=4) and (j==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()       

#%% C


for i in range(6):
    for j in range(6):
        if (i!=0 and i!=5 and j==0) or (i==0 and 0<j) or (i==5 and 0<j):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print() 
#%% D

for i in range(7):
    for j in range(7):
        if (j==0) or ((i==0  or i==6) and (j!=6)) or (j==6 and i!=0 and i!=6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   
#%% E

for i in range(7):
    for j in range(6):
        if (i==0 or i==3 or i==6) or j==0:
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()                                        
#%% F


for i in range(7):
    for j in range(6):
        if (i==0 or i==3 ) or j==0:
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()                

#%% G
for i in range(7):
    for j in range(7):
        if ((i==0 or i==6 ) and j!=0  and j!=6) or (j==0 and i!=0 and i!=6) or (j==6 and i<6 and i>3) or (i==4 and j>3):
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()                


#%% H


for i in range(7):
    for j in range(6):
        if (j==0 or j==5 or i==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()        

#%% I

for i in range(7):
    for j in range(7):
        if (j==3) or (i==0 and j<5 and j>1 ) or (i==6 and j<5 and j>1):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()  

#%% T

for i in range(6):
    for j in range(7):
        if (j==3) or i==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()                    

#%% J


for i in range(6):
    for j in range(8):
        if (i==0 and (j>0 and j<=5)) or (j==3 and(i!=5)) or (i==5 and(j<4 and j>0)) or (i==4 and j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% K


for i in range(7):
    for j  in range(8):
        if (j==0) or (i-j==3) or (j+i==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()       

  #%%      L

for i in range(6):
    for j in range(6):
        if (j==0) or (i==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            


#%% M

for i in range(7):
    for j in range(7):
        if j==0 or j==6 or (i==j and j<4) or (i+j==6 and i<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()         


#%% N


for i in range(7):
    for j in range(7):
        if j==0 or j==6 or (i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()       

#%% O


for i in range(7):
    for j in range(7):
        if ((j==0 or j==5) and i>1 and i<5) or ((i==0 or i==6) and j>1 and j<4)  or ((j==1 or j==4) and (i==1 or i==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()             

#%% O

for i in range(7):
    for j in range(6):
        if ((j==0 or j==5) and i!=0 and i!=6) or ((i==0 or i==6) and j!=0 and j!=5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

#%% P


for i in range(7):
    for j in range(6):
        if j==0 or (i==0 and j!=5 ) or (j==5 and i>0 and i<3) or(i==3 and j!=5):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% Q



for i in range(8):
    for j in range(6):
        if ((j==0 or j==5) and i!=0 and i!=6 and i!=7) or ((i==0 or i==6) and j!=0 and j!=5) or (i==7 and j==5) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

#%% R

for i in range(8):
    for j in range(6):
        if j==0 or (i==0 and j!=5 ) or (j==5 and i>0 and i<3) or(i==3 and j!=5)  or (i-j==3):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% S

for i in range(7):
    for j in range(6):
        if ((i==0 or i==3 or i==6) and (j!=0 and j!=5)) or (j==0 and 0<i<3) or (j==5 and 6>i>3):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   

#%% S

for i in range(7):
    for j in range(6):
        if (i==0 and j!=0) or (i==6 and j!=5) or (i==3 and j!=0 and j!=5) or (j==0 and 0<i<3) or (j==5 and 6>i>3):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()             

#%% T


for i in range(7):
    for j in range(7):
        if i==0 or j==3:    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  


#%% U


for i in range(7):
    for j in range(6):
        if ((j==0 or j==5) and (i!=6))or (i==6 and j!=0 and j!=5):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% V



for i in range(4):
    for j in range(7):
        if i==j or (i+j==6):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()      

#%% W


for i in range(7):
    for j in range(7):
        if j==0 or j==6 or ((j+i==6 or i==j) and i>2):
    
    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% X

for i in range(7):
    for j in range(7):
        if i==j or i+j==6:   
    
    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% Y


for i in range(7):
    for j in range(7):
        if (i==j and i<3) or (i+j==6 and i<3) or (j==3 and i>2):   
    
    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%%  Z


for i in range(7):
    for j in range(7):
        if i==0 or i==6 or i+j==6:   
    
    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  

#%% 1


for i in range(5):
    for j in range(3):
        if j==1 or i==4 or (i==1 and j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        

 #%%


for i in range(len("python")):
    

       print("python"[:i+1])
          
    