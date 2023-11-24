# 이 문제는 그리디 알고리즘으로 보일 수도 있다, 그리디는 큰수로 계속 나누는 것이 먼저 1로 도달할 수 있지만
# 예를 들어 n=10일 경우 10->5->4->2->1보다 10에 먼저 1을 빼서 10->9->3->1이 더 빠르다. 즉 동적 계획법을 이용해야 한다.
# 제일 작은 수부터 미리 계산된 값을 저장해두고 필요할 떄 빼내야한다.

n=int(input())
memo=[0]*(n+1)  # 계산된 횟수 미리 저장해둘 memo 배열을 선언한다. 0일 경우 값이 저장 안됐다는 의미이다.

for i in range(2,n+1):  # 1로 만드는 것이 목표이기 때문에 1은 어차피 0번 계산을 하기 때문에 0으로 고정된 값이다
                        # 따라서  2부터 n까지 반복해준다.
    memo[i]=memo[i-1]+1 # 기본으로 -1을 할경우 횟수가 늘기 때문에 전에 수보다 횟수를 1 늘려준 것을 memo[i]에 담는다.
    
    if i%3==0:  # 그때 i가 만약 3으로 나뉜다면
        memo[i]=min(memo[i],memo[i//3]+1)   # 1을 빼서 memo[i-1]을 만들어 기존 경우의 수에 1회를 더한 'memo[i]'와
                                            # n을 3으로 나누고(나누었으니 횟수에 +1을 해준다) 그때의 경우의 수 'memo[i//3]'
                                            # 위 두가지 경우를 비교하여 최솟값을 i일 때 계산 횟수인 memo[i]에 담는다.
    if i%2==0:  # i%3일 경우와 같다.
        memo[i]=min(memo[i],memo[i//2]+1)

print(memo[n])  # 횟수를 출력한다.
