class Point:
    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y

    def getAllPointsTo(self, toPoint:'Point') -> list['Point']:
        allPoints:list['Point'] = []

        start = self
        end = toPoint
        if self.x > toPoint.x or self.y > toPoint.y:
            start = toPoint
            end = self

        # horizontal/vertical lines
        if (start.x == end.x or start.y == end.y):
            #print("from", start, "to", end)
            for i in range(start.x, end.x+1):
                for j in range(start.y, end.y+1):
                    #print("indices", i, j)
                    nextPoint: 'Point' = Point(i, j)
                    allPoints.append(nextPoint)
            #print("allPoints", [(point.x, point.y) for point in allPoints])
            return allPoints
        else:
            # non horizontal/vertical lines => diagonal lines
            # 1st case: x and y higher
            if (start.x < end.x and start.y < end.y):
                for i in range(0, end.x - start.x + 1):
                    nextPoint: 'Point' = Point(start.x + i, start.y + i)
                    allPoints.append(nextPoint)
            # 2nd/3rd case: x or y higher, other one lower
            elif start.x > end.x:
                for i in range(0, end.y - start.y + 1):
                    nextPoint: 'Point' = Point(start.x - i, start.y + i)
                    allPoints.append(nextPoint)
            elif start.y > end.y:
                for i in range(0, end.x - start.x + 1):
                    nextPoint: 'Point' = Point(start.x + i, start.y - i)
                    allPoints.append(nextPoint)
            return allPoints

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


