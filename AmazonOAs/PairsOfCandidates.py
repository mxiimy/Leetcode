getNumTeams(cost: List[int], min_cost: int, max_cost: int)->int:
    count = 0
    for i in range(len(cost)):
        for j in range(i+1, len(cost)):
            if min_cost <= cost[i] + cost[j] and cost[i] + cost[j] <= max_cost:
                count += 1
                print(cost[i])
                print(cost[j])
                
    return count