from collections import Counter
import random


class homeWorkTwo():
    def first_task_str(self):
        new_str = 'spam and eggs or eggs with spam'

        #total symbols
        print('Total amount = ', len(set(new_str)))
        print(' '.join(new_str))

        #each symbols separately
        counter = Counter(new_str)
        print('Total amount "s" = ', counter['s'])
        print('Total amount "p" = ', counter['p'])
        print('Total amount "a" = ', counter['a'])
        print('Total amount "m" = ', counter['m'])
        print('Total amount "n" = ', counter['n'])
        print('Total amount "d" = ', counter['d'])
        print('Total amount "e" = ', counter['e'])
        print('Total amount "g" = ', counter['g'])
        print('Total amount "o" = ', counter['o'])
        print('Total amount "r" = ', counter['r'])
        print('Total amount "w" = ', counter['w'])
        print('Total amount "i" = ', counter['i'])
        print('Total amount "t" = ', counter['t'])
        print('Total amount "h" = ', counter['h'])

    def second_task_array(self, sequence, value):
        lo, hi = 0, len(sequence) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sequence[mid] < value:
                lo = mid + 1
            elif value < sequence[mid]:
                hi = mid - 1
            else:
                return mid
        return None


    def third_task_str_palindrome(self):
        str_palindrome = str(input())
        a = str_palindrome[::-1]
        if str_palindrome == a:
            print("Yes, this string is palindrome")
        else:
            print("No, this string is not palindrome")


    def fourth_task(self, new):
        new = new.split()
        new.reverse()
        new2 = ""
        for i in new:
            new2 += i + ' '
        return new2

    string = input()
    string = conversely(string)
    print(string)


    def five_task(self):
        valid_chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = input('Number of passwords?' + "\n")
        length = input('password length?' + "\n")
        number = int(number)
        length = int(length)
        your_pass = 'Your password:'

        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(valid_chars)
            print(your_pass, password)


    def six_task(self):
        line = "English = 78 Science = 83 Math = 68 History = 65"
        words = line.split()
        product = 0
        for word in words:
            try:
                value = int(word)
                product += value
            except:
                pass
        return product
