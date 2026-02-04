def maxPalette(colors, paletteSize, threshold):
    """
    :type colors: List[int]
    :type paletteSize: int
    :type threshold: int
    :rtype: int
    """
    count = 0 # How many palettes we can make--> return this
    if not colors:
        return 0
    if paletteSize == 1:
        return len(colors)
    sorted_colors = sorted(colors)
    print(sorted_colors)
    seen = []
    for i in range(len(sorted_colors)-paletteSize+1):
        j = len(sorted_colors)-1
        print("i:" + str(i))
        print("j:" + str(j))
        while j >= i+paletteSize-1:
            print(sorted_colors[j])
            print(sorted_colors[i])
            print(sorted_colors[j] - sorted_colors[i])
            if j not in seen and i not in seen and (sorted_colors[j] - sorted_colors[i]) <= threshold:
                count += 1
                seen.append(j)
                seen.append(i)
                break
            j -= 1
            
    return count
            