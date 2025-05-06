#Get age input from the user
age = int(input("enter your age :"))
if age <13 :
	print("you are in 'child' age group")	
elif 13 <= age<=19:
	print("you are in the 'teenager'age group")	
elif 20<=age <=59:
	print("you are in the 'adult' age group")  
else :
	print("you are in the 'senior' age group")
#get input from the user
number= float(input("enter a number:"))
#check whether the number is positive,negative or zero
if number > 0 :
	print("the number is positive")
elif number < 0:
	print("age number is negative")	
else:
	print("the number is zero")
#list of numbers 
numbers = {10,20,30,40,50,60,70}
#1. print the 2nd and 5th items from the list 
print("2nd item:","index" [ 1 ] )
print("5th item:","index" [ 4 ] )
#2. alternatively,findand print the maximum number in the list 
max_number = max(numbers)
print("maximum number in the list :",max_number)
car= {"brand": " toyota", "model": " corolla", "year": 2021}
#update the value of "year" to 2022
car["year"]= 2022
#print the updated dictionary
print (car)

