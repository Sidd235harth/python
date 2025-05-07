print(" Siddarth TR \n USN:1AY24AI106 \n sec:o")
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        raise ValueError("The number must be positive.")

    print(num, end=' ')
    while num != 1:
        num = collatz(num)
        print(num, end=' ')
except ValueError as e:
    print("Invalid input:", e)
