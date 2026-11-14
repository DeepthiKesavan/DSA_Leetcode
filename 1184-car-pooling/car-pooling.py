class Solution:
    def carPooling(self, trips, capacity):
        passengers = [0] * 1001
        for num, start, end in trips:
            passengers[start] += num
            passengers[end] -= num
        current = 0
        for i in range(1001):
            current += passengers[i]
            if current > capacity:
                return False
        return True
