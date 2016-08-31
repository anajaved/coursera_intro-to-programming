#Exercise 5.1 - user enters a series of numbers and once "done" is entered, will print the largest and smallest number

largest = None
smallest = None

while True:
    number = raw_input("Enter a number: ")
    if number == 'done' : break 
    if len(number) <1: break  #check for empty line
    try:
        num = float (number)
    except:
        print "invalid input"
        continue
    if smallest is None:
        smallest = number 
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
   
    
print "Maximum:", largest
print "Minimum:", smallest 