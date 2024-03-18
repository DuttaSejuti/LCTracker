class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[0])
        # points = sorted(new_points, key = lambda x:x[1])
        nonOverlappedPoints = list()
        i = 0
        print(points)

        if len(points) == 1:
            return 1

        while i < len(points)-1:
            currPoint = points[i]
            nextPoint = points[i+1]

            # non-overlap points condition
            if currPoint[1] < nextPoint[0]:
                nonOverlappedPoints.append(currPoint)
                
                if i+1 == len(points) - 1:
                    nonOverlappedPoints.append(nextPoint)
                    break
            else:
                newPoint = [max(currPoint[0], nextPoint[0]), min(currPoint[1], nextPoint[1])]
                
                if i + 1 == len(points) - 1:
                    nonOverlappedPoints.append(newPoint)
                    break
                
                i += 2
                while i < len(points):
                    thirdPoint = points[i]
                    if newPoint[1] < thirdPoint[0]:
                        nonOverlappedPoints.append(newPoint)

                        if i == len(points) - 1:
                            nonOverlappedPoints.append(thirdPoint)

                        i -= 1
                        break
                    if newPoint[1] >= thirdPoint[0]:
                        newPoint = [max(newPoint[0], thirdPoint[0]), min(newPoint[1], thirdPoint[1])]

                        if i == len(points) - 1:
                            nonOverlappedPoints.append(newPoint)
                    i += 1

            i += 1

        return len(nonOverlappedPoints)


