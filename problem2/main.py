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
    count = 0
    num = 0
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1 

    

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29