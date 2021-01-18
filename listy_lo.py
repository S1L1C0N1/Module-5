def func():
    food = ["rice", "beans"]
    # print(food)
    food.append("broccoli")
    # print(food)
    badcarbs = ["bread", "pizza"]
    food.extend(badcarbs)
    # print(food)
    print(food[0:2])
    print(food[4])
    print("done")

    stringy = "eggs, fruit, orange juice"
    breakfast = stringy.split(", ")
    # print(breakfast)
    print([len(breakfast)])
    print("done")

    print("Please input a floating point number or type STOP to stop: ")
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

if __name__ == "__main__":
    func()