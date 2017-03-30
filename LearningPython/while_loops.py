import math


def while_loop():
    # Event controlled while loop
        average = 0.0
        total = 0
        count = 0 
        print("Enter the Grade (-1) to quit: ")
        grade = int(input())
        while grade != -1:
            total = total + grade
            count = count + 1 
            print("Enter the Grade (-1) to quit: ")
            grade = int(input())
        average = total / count
        print("Average garde is: " + str(average))

if __name__ == "__main__":
    while_loop()

# def while_loop():
# 	    balance = 5000
# 	    rate = 1.02
# 	    year = 1
# 	    while year <= 10:
# 	        (balance) = round(balance * rate)
# 	        print("Year:" + str(year) + ":" + str(balance))
# 	        year = year + 1

# 	if __name__ == "__main__":
# 	    while_loop()

	# def while_loop():
		#     number = 1
		#     # print("Sorry out of range" + ' ' + str(number))
		#     while number <= 10:
		#         print(number)
		#         number = number + 1

		# if __name__ == "__main__":
		#     while_loop()

		# Count-Controller while loops
		# def while_loop():
		#     sum = 0
		#     number = 1
		#     while number <= 10:
		#         sum = sum + number
		#         number = number + 1
		#     print("The Sum is:" + str(sum))

		# if __name__ == "__main__":
		#     while_loop()
		