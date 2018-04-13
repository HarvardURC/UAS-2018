import numpy as np
# circle radius
RADIUS = 80;

def getBorderLines(circles):
    lines = []
    l = len(circles)
    for i in range(l):
        for j in range(i + 1, l):
            #print (i,j)
            if checkIntersection(circles, i, j):
                a = circles[i]
                b = circles[j]
                lines.append(([a[0], a[1]], [b[0], b[1]]))
    return lines


def checkIntersection(circles, i, j):
    p1 = circles[i]
    p2 = circles[j]

    for z in range(len(circles)):
        if (z == i or z == j):
            continue

        p3 = circles[z]

        p1 = np.asarray(p1)
        p2 = np.asarray(p2)
        p3 = np.asarray(p3)

        d = abs(np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1))
        
        if d < RADIUS:
            return False
    # if theres no intersection with other circles
    return True


