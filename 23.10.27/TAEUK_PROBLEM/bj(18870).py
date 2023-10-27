import sys #sys 모듈 import (입력)

input = sys.stdin.readline #input 속도, '\n' 개행 문자 표함된 문자열 반환
coord = {}

N = int(input()) #variable n에 입력 숫자 개수
arr = list(map(int, input().split())) #int인 input을 map한 후, 이들을 적용하여 숫자들의 list 작성

for i in arr:
    coord[i] = 0

arr2 = sorted(list(set(arr))) #중복된 숫자 제거(set), list 변환 
coord = {arr2[i] : i for i in range(len(arr2))} #딕셔너리(key arr2 element, 해당 원소의 index)
for i in arr: #arr 원소 반복
    print(coord[i], end = ' ') #dic 숫자 index 출력