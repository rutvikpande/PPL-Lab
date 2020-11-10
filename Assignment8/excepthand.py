#Handling zero division error
def divide(x, y): 
    try:  
        result = x // y 
        print("Result:", result) 
    except ZeroDivisionError: 
        print("You cannot divide by Zero") 

divide(3,0)

#Raising error 
def raiserror(x):
	if x > 5:
		raise Exception('x cannot exceed 5.\n The value of x was: {}'.format(x))


#Handling raised error
def handlerror(x):
    try:
        raiserror(x)
    except:
        print("Cannot enter greater than 5")
        
handlerror(6)
