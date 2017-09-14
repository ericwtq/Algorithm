def find_max(left, right, A):
    temp1 = temp2 = sum1 = sum2 = 0
    if left == right :
        ans = [left, right]
        return ans
    mid = (left + right) // 2
    max_left = find_max(left, mid, A)
    max_right = find_max(mid + 1, right, A)
    x = mid
    sum1 = A[mid]
    for i in range(mid, left - 1, -1):
        temp1 = temp1 + A[i]
        if temp1 > sum1:
            sum1 = temp1
            x = i
    y = mid + 1
    sum2 = A[mid +1]
    for i in range(mid + 1, right):
        temp2 = temp2 + A[i]
        if temp2 > sum2:
            sum2 = temp2
            y = i
    ans_total = sum1 + sum2
    ans = [x, y]
    if ans_total < sum(A[max_left[0]:max_left[1]+1]):
        ans_total = sum(A[max_left[0]:max_left[1]+1])
        ans = max_left
    if ans_total < sum(A[max_right[0]:max_right[1]+1]):
        ans_total = sum(A[max_right[0]:max_right[1]+1])
        ans = max_right
    return ans

A3 = [2, 8, -9, 20, 25, -127, 90, 50, -89, -2, 125, 64, 8, -15, -8, 10, 11, -30, 22]
A2 = [-9, -5, -2, -1]
A1 = [2, 18, -22, 20, 8, -6, 10, -24, 13, 3]
print(find_max(0, len(A1)-1, A1))
print(find_max(0, len(A2)-1, A2))
print(find_max(0, len(A3)-1, A3))