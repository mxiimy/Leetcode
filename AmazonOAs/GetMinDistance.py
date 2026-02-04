def getMinTotalDistance(dist_centers: List[int])->int:
    # 2D Clustering 
    dist_centers.sort()
    loc1 = dist_centers[0]
    loc2 = dist_centers[-1]
    min_dist = calc(dist_centers,loc1,loc2)
    if len(dist_centers)<3:
        return min_dist
    dist = min_dist + 1
    i = 1
    while dist > min_dist and i < len(dist_centers):
        move1 = calc(dist_centers, dist_centers[i], dist_centers[-i])
        move2 = calc(dist_centers, dist_centers[i-1], dist_centers[-i-1])
        moveBoth = calc(dist_centers, dist_centers[i], dist_centers[-i-1])
        minD = min(move1, move2, moveBoth)
        if minD == move1:
            loc1 = dist_centers[i]
        elif minD == move2:
            loc2 = dist_centers[-i-1]
        else:
            loc1 = dist_centers[i]
            loc2 = dist_centers[-i-1]
        if min(minD, min_dist) == min_dist:
            return min_dist
        else:
            min_dist = minD
            i += 1

    
def calc(dist_centers: List[int], loc1, loc2)->int:
    total = 0
    for i in dist_centers:
        if abs(loc1-i)<abs(loc2-i):
            total += abs(loc1-i)
        else:
            total+= abs(loc2-i)
    return total
