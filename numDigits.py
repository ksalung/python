def numOfDigits(number):
    return len(str(number))

num = int(input())
print(num,' 의 자릿수는 ', numOfDigits(num), '입니다.')


print("원하는 구구단 : ")
num = int(input())
for i in range(num):
    print(f'{num} * {i} = {num * i}')


def triple(x):
    return x * 3
num = int(input())
print('3곱하기 x는 ',triple(num))


from datetime import datetime
age = int(input())
def koreanAge(birthYear):
    today = datetime.today()
    return today.year - birthYear - 1
print('korean birth year is ', koreanAge(age))
