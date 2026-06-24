def euclidean_distance():
    PointA = list(map(int, input("Enter Coordinaates of point A: ").split()))
    PointB = list(map(int, input("Enter Coordinaates of point B: ").split()))
    #To find euclidean distance
    #First we will find Difference in x and y coordinates.
    dx = PointA[0]-PointB[0]
    dy = PointA[1]-PointB[1]
    #Now we will Use Formula
    distance = (dx**2 + dy**2)* 0.5
    return distance

print(euclidean_distance())
