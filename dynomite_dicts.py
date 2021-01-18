def func():
    pokedex = {}
    
    pokemon = (
        ('venosaur', 'grass, poison'),
        ('charizard,', 'fire, flying'),
        ('blastoise', 'water'),
    )
    pokedex = dict(pokemon)
    print(pokedex)



if __name__ == "__main__":
    func()