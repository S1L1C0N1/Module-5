def func():
    pokedex = {}
    
    pokedex = {
        'venosaur':'grass, poison',
        'charizard':'fire, flying',
        'blastoise':'water',
    }
    print(pokedex)
    del pokedex['blastoise']
    print(pokedex)



if __name__ == "__main__":
    func()