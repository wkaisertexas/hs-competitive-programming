if __name__=="__main__":
    n = int(input())
    for x in range(n):
        a = 0 
        b = 1

        y = int(input())
        equal = False
        while a <= y:
            if b == y:
                equal = True
            if a == y:
                equal = True
            b_temp = b
            b = a + b
            
            a = b_temp

        print(equal)
        ## This solution is terrible

