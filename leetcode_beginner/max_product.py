

import heapq
class Solution:
    def maximumProduct(self, number):
        a, b = heapq.nlargest(3, number), heapq.nsmallest(2, number)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])


number = [1, 2,3, 4]
print(Solution.maximumProduct(None, number))

