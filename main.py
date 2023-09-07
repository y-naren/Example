def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    print("Prime numbers between 1 and 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()
