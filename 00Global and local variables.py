#This topic is often a source of confusion, tried clearing it here
#Using global variables from a local scope
def spam():
	print(eggs) #reffered to a global variable in a local scope
eggs= 42 #global variable
spam()
print(eggs) #should say 42
print("________________")
print("both global and local variable with same name")

def spam1():
	eggs1='spam local variable'
	print(eggs1)
def bacon1():
	eggs1='bacon local variable'
	print(eggs1) #called inside bacon local scope so will print bacon local variable
	spam1() #prints from the spam local variable
	print(eggs1) #prints bacon local because local scopes cannot use variables in other local scopes
eggs1='global eggs variable'
bacon1()
print(eggs1) #prints global eggs because it is global-> global variables can read in a local space