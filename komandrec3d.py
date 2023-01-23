import pdb

print('Введите натуральное число')
chi1=input()
chi=int(chi1)
print('Введите несчастливое  число')
ne1=input()
ne=int(ne1)
i=0
slog3=[]
print('chi=',chi)
def recur(chi):
   slog1=0
   slog2=0
   pdb.set_trace()
   if chi==6 and ne==3:
      slog3.append('4')
      slog3.append('2')
   if chi==5 and ne==2:
      slog3.append('5')
   if chi==5 and ne==3:
      slog3.append('5')                
   
   if chi%2==0:
     slog1=chi/2
     slog2=slog1
     print('slog1,slog2 cht=',slog1,slog1)
    
     if slog1>3: recur(slog1)      
     
     elif slog1+slog2==5:
         if ne==3:
          slog3.append(slog1+slog2)
         elif ne==2:
          slog3.append(slog1+slog2)
       
    
       
   else:
     chi=chi+1
     slog1=chi/2
     slog2=slog1-1
     #print('slog1,slog2  necht=',slog1,slog1)
     if slog1>3: recur(slog1)
     else:
         slog3.append(slog2)
         i=1
     if slog2>3: recur(slog2)
     else:
        slog3.append(slog2)
        i=1
        
     
       
         
recur(chi)
print(slog3)
