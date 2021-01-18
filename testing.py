# nums = []
# user_input = 1
# while user_input != "stop":

#     user_input = input("Enter an number: ")
#     nums.append(user_input)
#     print(nums)


minval = None
maxval = None
nums = []

while True :
    num = input("Enter a number or type STOP: ")

    if num == "STOP" :
        break
    try :
        num = float(num)
        nums.append(num)
        print(nums)
    except :
        print("Invalid input")
        continue
    if maxval is None :
        maxval = num
    elif maxval < num :
        maxval = num
    if minval is None :
        minval = num
    elif num < minval :
        minval = num

average = sum(nums)/len(nums)
print("Maximum is", maxval)
print("Minimum is", minval)
print("Average is", average)