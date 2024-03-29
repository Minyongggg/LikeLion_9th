# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보세요. (단 입력으로 들어오는 수의 개수는 정해져 있지 않으며, 입력값으로 -1이 들어오면 더 이상 값을 받지 않는다.)

"""
[힌트]
1. 입력값을 받는 함수는 input함수입니다.
예시) core = input("양의 정수를 입력해주세요: ")

2. 입력으로 숫자가 몇 개가 들어올 지 모르는 상황입니다. 이 경우에는 일단 계속 반복을 하다가, 특정 조건인 경우에 반복문을 탈출해야 겠죠?

3. 입력된 숫자는 리스트에 저장을 해놨다가, 이후 평균을 계산할 때 이용해보세요!

어려우시면 운영진에게 언제든 물어보세요~
"""

###########################################################
# Step1. 리스트 모든 수의 평균을 계산하는 함수 작성하기
def average(input_list):
    sum = 0
    for i in input_list:
        sum += i
    return sum / len(input_list)

# Step2. 모든 수 입력받고 list에 저장하기
temp = 0
input_list = []
while True:
    temp = int(input("양의 정수를 입력해주세요: "))
    
    if temp == -1:
        break

    input_list.append(temp)

# Step3. 함수 호출하고 결과값 출력하기
result = average(input_list)
print(f"입력 값의 평균: {result}")