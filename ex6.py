for A in range(1, 10):        
    for B in range(0, 10):    
        AB = 10 * A + B
        result = AB * AB
        if 100 <= result <= 999:
            C = result // 100
            A2 = (result // 10) % 10
            B2 = result % 10
            if A == A2 and B == B2:
                print(result)
