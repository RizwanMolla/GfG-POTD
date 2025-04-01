def catchThieves(arr, k):
    thieves = []
    police = []
    
    # Store positions of thieves and police
    for i in range(len(arr)):
        if arr[i] == 'P':
            police.append(i)
        else:
            thieves.append(i)
    
    i, j = 0, 0
    count = 0
    
    # Process both lists to maximize thieves caught
    while i < len(police) and j < len(thieves):
        if abs(police[i] - thieves[j]) <= k:
            count += 1
            i += 1
            j += 1
        elif police[i] < thieves[j]:
            i += 1
        else:
            j += 1
    
    return count
