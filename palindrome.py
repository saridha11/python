def main():
    num = input('Enter any number : ')
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
main()
