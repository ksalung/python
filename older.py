
print("나의 나이를 입력하세요.")
age = int(input())
if not age.is_integer():
    print("나이를 숫자로 입력하세요.")
    exit

myBirthYear = 2025 - age + 1

if myBirthYear <= 1924 :
    print("The Great Generation.")
elif  1925 <= myBirthYear <= 1945 :
    print("The Slient Generation.")
elif 1946 <= myBirthYear <= 1964 :
    print("baby boomer.")
elif 1965 <= myBirthYear <= 1980 :
    print("Genration X")
elif 1981 <= myBirthYear <= 1996 :
    print("millennial.")
elif myBirthYear >= 1997 :
    print("Genration Z.")


