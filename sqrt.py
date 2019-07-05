def sqrt(x):
    a = b = c = d = e = 0
    epsilon = 0.0000000001
    
    while b <= x:
        b = b+a+a+1
        a = a+1
        
    c = a-1
    d = a

    while (d - c) > epsilon:
        e = (c+d)/2
        if (e*e < x):
            c = e
        else:
            d = e

    return c
