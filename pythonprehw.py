
#Python Q1: Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("hello_" + user_name.upper() +"!")

hello_name("USERNAME")


#Python Q1 Answer
def hello_name(user_name):
    print("hello_" + user_name +"!")

hello_name("USERNAME")


#Python Q2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    for value in range(1,100,2):
        print(value)
first_odds()


#Python Q3:
#Please write a Python function, max_num_in_list to return the max number of a given list.
#The first line of the code has been defined as below. def max_num_in_list(a_list):
def max_num_in_list(a_list):
    #for value in range(0,len(a_list)):
    #a_list = [0,5,10,55,78]
    max(a_list) 
    return (max(a_list))

max_num_in_list([0,5,10,55,78])


#Python Q4:
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

'''
def is_leap_year(a_year):
    print("Erm")
    if a_year%4 == 0:
        print(a_year)
        if a_year%100 != 0:
            print("hola")
        elif a_year%400 == 0:
                print("True")
    else:
        print("False")
'''
#PythonQ4 Answer:
def is_leap_year(a_year):
    if a_year%4 == 0:
    
        if a_year%100 != 0 or a_year%400 == 0:
            print("True")
    else:
        print("False")



is_leap_year(2000)
#def is_leap_year(a_year):
#if a_year %4 == 0 and a_year%100 != 0 or a_year%400 == 0


#Python Q5:
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.


'''
def is_consecutive(b_list,x):
    print(x)
    if b_list == sorted(b_list):
        print("True")

    else:
        print("false")
is_consecutive([1,2,3,4,6,7,99], True)
'''


'''
def is_consecutive(a_list):
    for index in range(0, len(a_list)-1):
        if a_list[index] + 1 == a_list[index+1]:
            continue
        else:
            return False

    return True
x=is_consecutive([1,2,3,4,5,6,7])
print(x)
'''
#PythonQ5 Answer
def is_consecutive(a_list):
    for index in range(0, len(a_list)-1):
        if a_list[index] + 1 == a_list[index+1]:
            continue
        else:
            return False

    return True
