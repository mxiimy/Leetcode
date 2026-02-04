def getSequence(dna: List[List[str]])->List[bool]: 
    result = [] 
    for pair in dna: 
        chars = {} 
        for char in pair[0]: 
            if char in chars: 
                chars[char]+= 1 
            else: 
                chars[char]=1 
        seen = {} 
        for c in pair[1]: 
            if c in seen: 
                seen[c]+= 1 
            else: 
                seen[c]=1 
        rm1 = 0 
        rm2 = 0 
        longer = {} 
        shorter = {} 
        if len(seen) > len(chars): 
            longer = seen 
            shorter = chars 
        else: 
            longer = chars 
            shorter = seen 
        for i in longer: 
            if i in shorter: 
                if longer[i] - shorter[i]>0: 
                    rm1+=1 
                elif longer[i] - shorter[i]<0: 
                    rm2+=1 
            else: 
                rm1+=1 
        if (rm1>1 or rm2>1): 
            result.append(False) 
        else: 
            result.append(True) 
    return result