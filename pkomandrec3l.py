import pdb

print('Введите натуральное число')
chi1=input()
chi=int(chi1)
print('Введите несчастливое  число')
ne1=input()
ne=int(ne1)
i=0
slog3=[]
aa=0
ss=0
slog11=[]
slog22=[]
print('chi=',chi)
def recur(chi):
   global aa
   global i
   global ss
   global slog11
   global slog22
   slog1=0
   slog2=0
   dd=0
   ff=0
   
   
   #pdb.set_trace()
   global slog3           
   
   if chi%2==0:
     slog1=chi/2
     ss=ss+1
     print('ss nach=',ss)
     slog2=slog1
     slog11.append(slog1)
     slog22.append(slog2)
     #print('slog1,slog2 cht=',slog1,slog1)
     if ne==3:
        
        if slog1==6: 
          slog3.append('4')
          slog3.append('2')
          slog3.append('4')
          slog3.append('2')
          if ss==1: i=1
        
        elif slog1==5:
          #slog3.append('5')
          #slog3.append('5')
          print('ss=',ss)
         
          while ss!=0:
             slog3.append('5')
             slog3.append('5')
             ss=ss-1
          i=1
          aa=aa+1
        elif slog1==7:
          print("ss KKONEX=",ss)
         
          slog3.append('5')
          slog3.append('2')
          slog3.append('5')
          slog3.append('2')
          i=1
       
        elif slog1==8:
       
          print('ss kon=',ss)
          slog3.append('4')
          slog3.append('4')
          if ss==1: i=1
          aa=aa+1
        elif slog1==9:
          slog3.append('5')
          slog3.append('4')
          if ss==1: i=1
          aa=aa+1
        elif slog1==4:
          print('slog11=',slog11)
          print('slog22=',slog22)
          print('ss kkon=',ss)
          dd=ss-1
          ff=2**dd
          while ff!=0:
             slog3.append('4')
             ff=ff-1
        
            
          #if ss==1: i=1
          i=1
          
       
          
        elif slog1!=5 and slog1!=6 and slog1!=3 and slog1!=2 and slog1!=7: recur(slog1)
        elif slog1==2:
          
           aa=aa+1
           print('slog1=',slog1)
           slog3.append(slog1)
           print('aa=',aa)
                   
     if ne==2:
        if slog1==5:
          slog3.append('5')
          slog3.append('5')
          aa=aa+1
          i=1
          
        if slog1==4:
          dd=ss-1
          ff=2**dd
          while ff!=0:
            slog3.append('4')
            ff=ff-1
        
          i=1
           
     #else:
     if i!=1 and slog1>3: recur(slog1)
     elif i!=1 and slog1>3: 
         slog3.append(slog1)
         i=1
       
           
     if i!=1 and slog2>3: recur(slog2)
     elif i!=1 and slog1>3: 
        slog3.append(slog2)
        i=1  
      
                    
   else:
     chi=chi+1
     slog1=chi/2
     ss=ss+1
     slog2=chi-1-slog1
     slog11.append(slog1)
     slog22.append(slog2)
     print('slog2nech=',slog2)
     if slog1>3: recur(slog1)
     else:
         slog3.append(slog1)
         i=1
   
   if i==1:
      rr=ss-2
      slog2=slog22[rr]
      print('slog2=',slog2)
      
         
recur(chi)
print(slog3)
#print(ss)


