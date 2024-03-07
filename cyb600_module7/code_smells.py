def check_if_prime(number):
    '''
    Check if number is prime
    checks if number the given number is a prime number
        number (int):
    Returns:
          if temp == 1:
        return"given number is not prime"
    else:
        return"given number is prime"
    '''
    number = int(str(int(input("please give a number : "))))
    temp = 0
    for i in range(2, number // 2):
        if number % i == 0:
            temp=1
            break
    if temp == 1:
        return"given number is not prime"
    return"given number is prime"

if __name__ == "__main__":
    print(check_if_prime())