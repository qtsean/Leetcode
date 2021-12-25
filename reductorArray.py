import bisect


def refectorArray(a, b, d):
    b.sort()
    count = 0
    for n in a:
        left = bisect.bisect_left(b, n-d)
        right = bisect.bisect_right(b, n+d)
        if left == right:
            count += 1
    return count

print((refectorArray([7, 5, 9], [13, 1, 4], 3)))