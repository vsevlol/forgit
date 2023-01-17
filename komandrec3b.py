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
   if chi%2==0:
     slog1=chi/2
     slog2=slog1
     print('slog1,slog2 cht=',slog1,slog1)
     #pdb.set_trace()
     if slog1==ne:
        slog2=slog1-2
        if slog2!=ne:
           
           chi=chi-2 #проверка на то, что просчитали всё до конца
           slog3.append(2)
           
           if slog2>3: recur(slog2)
           else:
              slog3.append(slog2)
              i=1
        else: i=1   
        #or slog1==2:
                
     else:         
         slog3.append(slog1)
         slog3.append(slog2)
         recur(slog1)
         recur(slog2)
     
       
   else:
     chi=chi+1
     slog1=chi/2
     slog2=slog1-1
     print('slog1,slog2  necht=',slog1,slog1)
     
     if slog1==ne: #or slog1==2: 
        if slog1-2!=ne:
           chi=chi-2 #проверка на то, что просчитали всё до конца
           slog3.append(2)
        else: i=1    
     else:
       slog3.append(slog1)
       slog3.append(slog2)
       recur(slog2)
       recur(slog1)
         
recur(chi)
print(slog3)
