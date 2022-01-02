def throttlingGateway(arr):
    ans = 0
    for i in range(len(arr)):
        if i >= 3 and arr[i] - arr[i-3] < 1:
            ans += 1
        elif i >= 20 and arr[i] - arr[i-20] < 10:
            ans += 1
        elif i >= 60 and arr[i] - arr[i-60] < 60:
            ans += 1
    return ans

arr = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
print(throttlingGateway(arr))
