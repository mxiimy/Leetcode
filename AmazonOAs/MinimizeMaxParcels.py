def minimize_maximum_parcels(parcels: List[int], extra_parcels: int)->int:
    currmax = max(parcels)
    while extra_parcels > 0:
        parcels[parcels.index(min(parcels))] += 1
        extra_parcels -= 1
        currmax = max(parcels)
    
    return currmax