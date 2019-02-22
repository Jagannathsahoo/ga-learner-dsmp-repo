# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=',',skip_header=1)
#print(data)
census=np.concatenate([data,new_record])
print(census)


# --------------
#Code starts here
age=np.array(census[...,0])
print(age)
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(age_mean)
print(max_age)
print(min_age)
print(age_std)
print(census)
print(np.shape(census))



# --------------
#Code starts here
race_0=np.array(census[census[...,2]==0])
race_1=np.array(census[census[...,2]==1])
race_2=np.array(census[census[...,2]==2])
race_3=np.array(census[census[...,2]==3])
race_4=np.array(census[census[...,2]==4])
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(race_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)
minority_race=3


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len

print(avg_working_hours)
'''mask=census[...,0]<55
print(mask)

senior_citizens=census[census[:,0]>55]
print(senior_citizens)
#working_hours_sum=sum(senior_citizens[...,6])
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens
print(avg_working_hours)'''


# --------------
#Code starts here
high=census[census[...,1]>10]
low=census[census[...,1]<=10]
#print(high)
#print(low)
avg_pay_high=np.mean(high[...,7]).round(2)
avg_pay_low=np.mean(low[...,7]).round(2)
print(avg_pay_high)
print(avg_pay_low)
print(avg_pay_high > avg_pay_low)



