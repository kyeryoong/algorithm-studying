# Q07. 럭키 스트레이트
# [백준] https://www.acmicpc.net/problem/18406


numbers = [int(i) for i in list(input())]

if sum(numbers[0 : int(len(numbers) / 2)]) == sum(numbers[int(len(numbers) / 2) : ]):
    print("LUCKY")

else:
    print("READY")