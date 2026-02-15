numbers = []
for i in range(15):
        num = int(input("Please enter a number: "))
        numbers.append(num)
for number in numbers:
    if number % 2 == 0:
            print(str(number) + " is an even number.")
    else: 
            print(str(number) + " is an odd number.")

    
