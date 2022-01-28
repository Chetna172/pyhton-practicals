if _name_ == '_main_':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    x = max(arr)
    y = -9999999
    for i in range(0, n):
        if arr[i] < x and arr[i] > y:
            y = arr[i]

    print(y)