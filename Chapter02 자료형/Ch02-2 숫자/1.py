import sys
sys.stdin = open('SampleInput.txt') #파일을 불러서 한줄씩 읽음

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
#    print(f'#{test_case}')
    for i in range(N,-1,-1):
        print(i,end = ' ' )
