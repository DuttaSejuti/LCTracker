class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort intervals based on the end points
        points.sort(key=lambda x: x[1])

        nonOverlappedPoints = []
        end = points[0][1]

        for i in range(1, len(points)):
            nextPoint = points[i]
            start = nextPoint[0]
            if start > end:
                nonOverlappedPoints.append(end)
                end = points[i][1]

        nonOverlappedPoints.append(end)

        return len(nonOverlappedPoints)
