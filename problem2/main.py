def is_prime(n):
    prime_flag = 0
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def primeX(n):
    i = 2
    while(n > 0):

        if(is_prime(i)):
            n -= 1
        i += 1
    i -= 1 
    return i
    

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29