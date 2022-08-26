def crazy_funk(): 
    x = "maylindenberg"
    i = 0  

    for letter in x: 
        if i % 2 == 0: 
            print(letter.lower(), end= "")
        else:
            print(letter.upper(), end= "")
        i += 1  

crazy_funk()