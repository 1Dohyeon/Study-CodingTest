# 다이나믹 프로그래밍이란 문제의 크기의 큰 문제를 작은 문제 여러개로 나눈 다음에 푸는 방법이다. 동적 계획법이라고 불린다.
# 이와 같은 특징을 공통점으로 가지는 분할 정복이라는 코딩방법도 있다. 단 분할 정복은 중복이 발생하지 않는다.

# 다이나믹 프로그래밍에서 각 문제는 한 번만 풀어야 한다.
# optimal substructure를 만족하기 때문에, 같은 문제는 구할 때마다 정답이 같다
# 따라서, 정답을 한 번 구했으면, 정답을 어딘가에 메모해놓고 그 메모를 Memoization이라고 한다.
# 예를 들면 피보나치의 수에서 N(N>4)번째를 구할 때 4번째 피보나치의 수를 꼭 구해야하고, N=100일 때나 50, 20, 10일 때도 
# 4번째 피보나치의 수를 구해야하며 4번째 피보나치의 수는 어떤 식에서든지 값이 같으므로 optimal substructure을 만족한다.
# 따라서 이미 구한 피보나치의 수는 메모를 하여 여러번 더 구하지 않게 하여 시간복잡도를 줄인다.

# 피보나치의 수(재귀함수: Top-down)
def fibonacci1(n):
    if n<=1:
        return n
    else:
        return fibonacci1(n-1)+fibonacci1(n-2)
# 위 식은 일반적인 피보나치 수를 구하는 재귀함수이다. 하지만 이것은 이미 구한 수를 또다시 구해야하는 비효율적인 방법이다.
# 아래는 위의 단점을 보완한 memo를 이용한 방법이다.

memo=[0]*100 # 모든 메모 memo[i]는 0이다, 이는 답을 아직 안구했다는 의미이고
def fibonacci2(n):
    if n<=1:
        return n
    else:
        if memo[n]>0:   # 피보나치의 수는 양수이므로 0보다 크다면, 답이 구해진 것이므로
            return memo[n]  # 아래 식을 다시 구하지 않고 그 값을 return한다.

        memo[n]=fibonacci2(n-1)+fibonacci2(n-2) # 답을 구할 때 마다 memo라는 배열에 추가한다. 이제 memo는 0이 아니므로
                                                # 답을 구했으니 다신 안구해도 된다는 의미이다.
        return memo[n]

# fibonacci1의 방법은 함수의 길이가 n이고, 1개를 호출하면 2개, 2개면 4개, 4개면 8개로 증가하므로 2의 n제곱의 시간복잡도를 
# 가지지만 fibonacci2는 문제를 한번 푸는데 걸리는 시간은 +만 계산하면 되기 떄문에 1이고 문제의 개수는 n이므로 
# n이라는 시간복잡도를 가진다.

# fibonacci1을 적을 때 옆에 Top-down이라고 적혀있는데 이것은 다이나믹 프로그래밍의 구형 방식이다.

'''
다이나믹의 구현에는 두가지 방식이 있다. 
Top-down
Bottom-up
이 있다.

말 그대로 top down은 큰문제부터 작은문제로 쪼개고 다시 큰문제를 푸는 방식이고 bottom up은 작은문제부터 시작해서 큰문제를
푸는 방법이다.
두가지 모두 연습하기 보단 우선 한가지 방법에 익숙해지는 것이 좋다. 둘의 시간복잡도는 다를 수도 있고 같을 수도 있지만 
대부분의 문제에서는 비슷하고 정답을 알 수 없다. 또한 한가지 방법으로만 풀리는 문제를 풀 수준이면 이미 두가지 방법을 다
이용할 수 있을 수준일 것이니 한가지 방법만 이용하면 좋다. '파이썬'의 경우 스택오버플로우 에러가 자주 등장하므로 bottom-top
을 추천한다.
'''
