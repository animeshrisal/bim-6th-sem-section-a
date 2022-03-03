num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
arr1 = [1,2,3]
try:
    print(arr1[1])
    num3 = num1 / num2
    print(num3)
except ZeroDivisionError as e:
    print("Cannot divide by zero!")
except Exception as e:
    print("Some other error!")
finally:
    print("Got here!")