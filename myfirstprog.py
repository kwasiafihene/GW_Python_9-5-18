# My first Python program

print("Hello, World!")

print("This Section sums two numbers 5 and 10" )

A = 5 + 10 

print(A)

n = input("Please enter your name: ")
n 

total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, " mins=", minutes,
"secs=", secs_finally_remaining)

p = 10000
r = 0.08
n = 12
t = int(input("Compounded Years:"))
A = p*(1 + (r/n))**(n*t)
print(A)
