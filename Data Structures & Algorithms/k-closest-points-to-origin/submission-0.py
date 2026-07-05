class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        buckets = [[] for _ in range(100001)]

        for x,y in points:
            distance = x*x + y*y

            buckets[distance].append([x,y])

        results = []

        for bucket in buckets:
            for point in bucket:
                results.append(point)

                if len(results) == k:
                    return results