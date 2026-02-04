def getMinimumBoxes(boxes: List[int], capacity: int) -> int:
    boxes.sort()
    n = len(boxes)
    max_kept = 0
    left = 0
    
    for right in range(n):
        while boxes[right] > capacity * boxes[left]:
            left += 1
        
        current_window_size = right - left + 1
        max_kept = max(max_kept, current_window_size)
            
    return n - max_kept