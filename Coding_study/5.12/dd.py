import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
m=int(input())
palindrome=[[0 for i in range(n+1)]for j in range(n+1)] #dp테이블
for i in range(1,n):
    #[1][1]/[2][2]/[3][3]...은 항상 팰린드롬이니까 1로 초기화
    palindrome[i][i]=1
    #[1]==[2]?/[2]==[3]?...이 팰린드롬인지
    if arr[i-1]==arr[i]:
        palindrome[i][i+1]=1
palindrome[-1][-1]=1

for i in range(1,n):
    for j in range(1, n+1-i):
        #가운데가 팰린드롬인지 확인 후 끝이 같은지 확인
        #ex1)1,3,3,1 [2][3](=3,3)이 팰린드롬?+[1](=1)==[4](=1)?
        #ex2)1,3,5,3,1 [2][4](=3,5,3)이 팰린드롬?+[1](=1)==[5](=1)?
        if palindrome[j + 1][j + i - 1] == 1 and arr[j - 1] == arr[j - 1 + i]:
            palindrome[j][j+i]=1
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(palindrome[a][b])