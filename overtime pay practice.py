rate1= 10
rate2= 15
hrs = raw_input ('How many hours did you work this week?')
hours = int(hrs)
if hours <= 40:
    pay= hours*rate1
    print pay
else:
    ovt=hours-40
    pay2=(40*rate1)+(ovt*rate2)
    print pay2
        
    #how to calculate overtime when overtime rate =1.5/hr 
    #using raw_input & if/else statements 