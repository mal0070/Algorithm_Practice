n = int(input())

def fibo(n):
    f = [0] * (n+1) #이전 값 저장할 공간
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1): #for문을 통해 차례대로 값 저장
        f[i] = f[i-1] + f[i-2] 
    return f[n] #마지막값이 답!

print(fibo(n))
