def is_prime(start):
    prime_flag = 0
    if(start>1):
        for i in range(2,int(start**0.5)+1):
            if (start % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def primeX(n,start):
    count = 0
    num = start
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1 

def primeX(n,start):
    i = start
    c = 0
    while(c < n):
        if(is_prime(i)):
            n -= 1
        i += 1
    i -= 1 
    return i

def generate_primes_grid(width, height, start):
    grid = ""
    start_prime = primeX(1, start)
    if start == start_prime:
        start_prime += 1 
    for i in range(height):
        row = ""
        for j in range(width):
            prime = primeX(i * width + j + 1, start_prime)
            row += str(prime)
            if len(str(prime)) == 1:
                row += " "
            row += " "
        grid += row.strip() + "\n"
    return grid.strip() + "\n"




if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """