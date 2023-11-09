#calculator

print("welcame to calculator")
operation_list = {"*" ,"/","+","-"}

name = input("pliz enter your name: ")
family = input("plz enter your family name: ")

pasword_1 = input("pliz create your pasword: ")
pasword_2 = input("pliz enter your pasword: ")

for pasword in range(2):
    while pasword_1 != pasword_2:
        print("rong pasword")
        pasword_2 = input("try again")
print("your pasword is accepted")


for operation in operation_list:
    print(operation)

a = int (input("pliz enter your ferst namber: "))
operation = input("what`s yuor operation: ")
b = int (input("pliz enter your sec namber: "))


def my_function(a, b) :
	if operation == "*" :
		print (a * b)
	elif operation == "/" :
		print (a / b)
	elif operation == "+" :
		print (a + b)
	elif operation == "-" :
		print (a - b)
	else :
		print ("") 
my_function(a, b)
