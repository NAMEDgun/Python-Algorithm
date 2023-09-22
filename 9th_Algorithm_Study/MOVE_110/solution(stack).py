def solution(s):
    def remove_110(string):
        stack = []
        count_110 = 0
        
        # 문자열 내에서 "110" 패턴을 탐색하고 제거
        for char in string:
            if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and char == '0':
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(char)
        
        # 남은 문자열에서 연속된 '1' 개수 계산
        count_1 = 0
        for char in stack[::-1]:
            if char == '0':
                break
            else:
                count_1 += 1
        
        # 최종 결과 문자열 생성
        result = ''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1
        return result

    answer = []

    for string in s:
        modified_string = remove_110(string)
        answer.append(modified_string)

    return answer
