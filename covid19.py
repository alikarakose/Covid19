import numpy as np
import matplotlib.pyplot as plt
import csv
import datetime 


with open('COVID-19.csv', newline='') as csvfile:
    next(csvfile) 
    covidfile = csv.reader(csvfile, delimiter=',')
    data = list(covidfile)

myData=np.asarray(data)



land=input("Geben Sie ein Land ein = ")
    
countryindex=np.argwhere(myData[:,6]==land)
country=myData[countryindex]
date1=myData[countryindex][:,:,0].reshape(len(country))
   
times=[]
for zeit in date1:
    a=datetime.datetime.strptime(zeit,'%d/%m/%Y')
    times.append(a)
    
sum1=0
casray=[]
    
for cases in country[:,:,4]:
    casray.append(int(cases))
    sum1=sum1+int(cases)
        
        
print("Number of Case =>" , sum1)
      
sum2=0
deatray=[]
       
for deaths in country[:,:,5]:
    deatray.append(int(deaths))
    sum2=sum2+int(deaths)
     
print("Number of Death => ", sum2)
    
print("Percent of death %", "{:0.2f}".format((sum2*100)/sum1))
    
fig,ax1=plt.subplots()
ax2=ax1.twinx()

ax1.plot(times,casray,color="r")
ax2.plot(times,deatray,color="b")

ax1.set_xlabel('Time')
ax1.set_ylabel('Case', color='r')
ax2.set_ylabel('Death', color='b')


    
plt.show()
    
    
#%%moving average
def myMovAvg(x,w):
    return np.convolve(x,np.ones(w),'valid')/w

MAdegree=20

MAcases=myMovAvg(casray, MAdegree)
MAdeath=myMovAvg(deatray, MAdegree)

timex=times[0:len(MAcases)]

fig2,ax3=plt.subplots()
ax4=ax3.twinx()

ax3.plot(timex,MAcases,color="r")
ax4.plot(timex,MAdeath,color="b")

ax3.set_xlabel('Time')
ax3.set_ylabel('MA Cases', color='r')
ax4.set_ylabel('MA Death', color='b')



plt.show()






#%%
times=[]
for zeit in date1:
    a=datetime.datetime.strptime(zeit,'%d/%m/%Y')
    times.append(a)








#%%
datetime.datetime.strptime('14/12/2020', '%d/%m/%Y')








#%%

import csv

with open('COVID-19.csv', newline='') as csvfile:
    covidfile = csv.reader(csvfile, delimiter=',')
    next(csvfile) # skip first line
    for row in covidfile:
        # print(', '.join(row))
        dateRep,day,month,year,cases,deaths,countriesAndTerritories,geoId,countryterritoryCode,popData2019,continentExp,cumulative = row



