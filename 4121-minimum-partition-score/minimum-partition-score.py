class Solution:
    def minPartitionScore(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        prev = [float('inf')] * (n + 1)
        prev[0] = 0
        for parts in range(1, k + 1):
            curr = [float('inf')] * (n + 1)
            def solve(left, right, optLeft, optRight):
                if left > right:
                    return
                mid = (left + right) // 2
                bestCost = float('inf')
                bestPos = -1
                for j in range(optLeft, min(optRight, mid - 1) + 1):
                    s = prefix[mid] - prefix[j]
                    cost = s * (s + 1) // 2
                    total = prev[j] + cost
                    if total < bestCost:
                        bestCost = total
                        bestPos = j
                curr[mid] = bestCost
                solve(left, mid - 1, optLeft, bestPos)
                solve(mid + 1, right, bestPos, optRight)
            solve(parts, n, parts - 1, n - 1)
            prev = curr

        return prev[n]