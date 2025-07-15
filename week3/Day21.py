#Write a Recursion Function to find is the given number in armstrong or not
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_recursive(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return digit**power + armstrong_recursive(n // 10, power)

def is_armstrong(num):
    power = count_digits(num)
    return num == armstrong_recursive(num, power)

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
