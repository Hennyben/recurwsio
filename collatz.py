


def collatz(n,c):
    if n == 1:
        print(c)
        return
    else:
        if n % 2 == 0:
        
            return collatz(n/2,c+1)
            
        else:
        
            return collatz(3*n + 1, c + 1)
  
print(collatz(50,0))
