#Question 1
#Write down a program in Python for Opening a File and Writing " I Love LetsUpgrade" And close
#it, and read it back again, and then append some data to it and close it.
f= open("shreeja.txt","w+")
f.write(" I Love LetsUpgrade")
f.close()
f= open("shreeja.txt","r")
print(f.read())
f = open("shreeja.txt", "a")
f.write("Today is lecture")
f.close()
print("Question 1 ends")

#Question 2
#Write a function which can return a Factorial of any numbers as INT, given in the argument.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
num = 10
print("Factorial of", num, "is",
      factorial(num))
print("Question 2 ends")
