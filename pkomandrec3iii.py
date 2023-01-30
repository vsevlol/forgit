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
print('chi=',chi)
def recur(chi):
   global aa
   global i
  
   slog1=0
   slog2=0
   #pdb.set_trace()
   global slog3           
   
   if chi%2==0:
     slog1=chi/2
     slog2=slog1
     #print('slog1,slog2 cht=',slog1,slog1)
     if ne==3:
       
        if slog1==6: 
          slog3.append('4')
          slog3.append('2')
          slog3.append('4')
          slog3.append('2')
          i=1
          k=k+1
        elif slog1==5:
          slog3.append('5')
          slog3.append('5')
          i=1
          aa=aa+1
        elif slog1==7:
          slog3.append('5')
          slog3.append('2')
          i=1
          aa=aa+1 
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
          slog3.append('4')
          slog3.append('4')
          slog3.append('4')
          slog3.append('4')
          aa=aa+1
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
     slog2=slog1-1
     #print('slog1,slog2  necht=',slog1,slog1)
     if slog1>3: recur(slog1)
     else:
         slog3.append(slog1)
         i=1
     if slog2>3: recur(slog2)
     else:
        slog3.append(slog2)
        i=1
        
     
       
      
recur(chi)
print(slog3)
print(aa)


