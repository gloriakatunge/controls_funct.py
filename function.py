#functions

# def add_nums (a,b):
#     answer= a+b
#     return answer
# Sum = add_nums(10,2)
# print("Sum:",Sum)

#four variables that are associated with python functions
#local scope 
# global scope
# enclosing scope
# buit in scope e.g print,for ,def ,in etc

global_var = 20
def nums_add(a,b):
    total = a+b
    print("Global_var in outer function:",global_var)
    def double_it():
        double =total*2
        print("Global_var in inner function:",global_var)
    double_it()
    return total

nums_add(23,3)

