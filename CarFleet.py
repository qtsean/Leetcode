class Solution:
    def carFleet(self, target, position, speed):
        cars = [(target - p) / s for p, s in sorted(zip(position, speed))]
        res = 0
        cur = 0
        for car in cars[::-1]:
            if car > cur:
                cur = car
                res += 1
        return res