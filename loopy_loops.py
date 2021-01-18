def func():
    pokemon = ("picachu", "charmander", "bulbasaur")
    print(pokemon[0])
    print("done")

    (starter1, starter2, starter3) = pokemon
    print(starter2)
    print("done")

    tuple = ("J", "A", "C", "K")
    print(f"Is i in tuple: {'i' in tuple}")
    print("done")

    for x in range(2, 11):
        x += 0
        print (x)
    print("done")

    x = 2
    while x < 11:
        print(x)
        x += 1
    print("done")
        
    stringy = "This is a simple string"
    x = 0
    for x in range(23):
        print(stringy[x])
        x += 1
    print("done")

    setty = ('this', 'is', 'a', 'simple', 'set')
    index = 0
    times = 0
    for index in range(5):
        times = 0
        while times < 3:
            print(setty[index])
            times += 1
        index += 1
    print("done")
            
            
        



if __name__ == "__main__":
    func()