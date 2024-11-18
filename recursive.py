

def factorial(x):
    #base case
    if x <= 1:
        return 1
    
    #recursive case
    else: 
        return x * factorial(x-1)

#for i in range(1,11):
   # print(f"{i}! = {factorial(i)}")
    
def fib(x):
    if x <= 1:
        return x
    
    else:
        return fib(x-1) + fib(x-2)
    
#for i in range(1,11):
    #print(f"Fibonacci of {i} = {fib(i)}")

def prepare_String(input_string):
    output_string = ""
    for c in input_string:
        if c.isalpha():
            output_string += c.lower()
    return output_string

test_string = "Go hang salami, I'm a lasagna hog"

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    
print(is_palindrome(prepare_String(test_string)))
        
def hanoi_solver(start, end, helper, disks):
    if disks == 0:
        return
    else:
        #solve disks -1 from start to helper
        hanoi_solver(start, helper, end, disks-1)
        print(f"move disks from {start} to {end}")
        #solve disk -1 from helper to end
        hanoi_solver(helper, end, start, disks-1)

hanoi_solver("A", "C", "B", 4)