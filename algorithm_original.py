# Original DFS algorithm used in the video

def traverse_map(map_data, row=0, col=0, direction='B'):
    if row < 0 or col < 0 or row >= len(map_data)\
        or col >= len(map_data[0]) or map_data[row][col] == 0:
        return ''
    
    if map_data[row][col] == 8:
        return direction + 'G!'
    
    map_data[row][col] = 0
    
    n = traverse_map(map_data, row-1, col, 'N')
    s = traverse_map(map_data, row+1, col, 'S')
    e = traverse_map(map_data, row, col+1, 'E')
    w = traverse_map(map_data, row, col-1, 'W')
    
    if n:
        return direction + n
    elif s:
        return direction + s
    elif e:
        return direction + e
    elif w:
        return direction + w
    else:
        return ''
        
