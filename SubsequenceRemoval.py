import collections


def remove_arr(array):
    if not array or len(array) < 2:
        return []
    num_remained = collections.Counter(array)
    num_to_remove = {}
    for num in num_remained:
        if num_remained[num] > 1:
            num_to_remove[num] = num_remained[num] - 1
    if not num_to_remove:
        return []
    res = []
    for num in array:
        num_remained[num] -= 1
        if num in num_to_remove:
            while res and res[-1] > num:
                if res[-1] in num_to_remove:
                    num_to_remove[res[-1]] += 1
                else:
                    num_to_remove[res[-1]] = 1
                if num_to_remove[res[-1]] > num_remained[res[-1]]:
                    print([-1])
                    return
                res.pop()
            res.append(num)
            num_to_remove[num] -= 1
            if num_to_remove[num] == 0:
                del num_to_remove[num]
    print(res)