print("\tregistration")
a=str(input("\twrite your name:"))
b=str(input("\twrite your name:"))
c=str(input("\twrite your email:"))
d=str(input("\twrite your code:"))
print(f"\tname:{a }")
print(f"\tsurename:{b }")
print(f"\temail:{c }")
print(f"\tpassword:{d }")
print("\tchecking that you are not robot, \n\tjust solve the question below:")
	
e=int(input("\t       9*8="))
print(f"\t{e}")
if e==72:
	print("\tyou are not robot")
	print(f"\t{a} thanks for registration :)")
	print("\tyou are successfuly registrated!!!")
if e<72:
		print("\tyou are robot")
		print("\tyou couldn't registrate as you finded as robot")
if e>72:
	    print("\tyou are robot")
	    print("\tyou couldn't registrate as you finded as robot")
	    
