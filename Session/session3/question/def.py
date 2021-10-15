#입력받은 문자열의 역순을 출력하는 함수를 작성하세요.
#ex) python -> nohtyp

# def reverse(str):
#     for i in range(len(str)):
#         print(str[-(i+1)], end="")
def reverse(str):
    for i in range(len(str)-1, -1, -1):
        print(str[i], end="")


str = input()
reverse(str)