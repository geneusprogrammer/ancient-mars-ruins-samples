# Using memoization
import numpy as np
import time
import sys

class TraverseWithMemo:
    def __init__(self):
        self._memo = {}
        
    def traverse(self, map_data):
        map_np = np.array(map_data)
        assert isinstance(map_np, np.ndarray)
        assert len(map_np.shape) == 2
        trav_map = self._traverse(map_np)
        return trav_map
        
    def _traverse(self, map_data, row=0, col=0, direction='B'):
        if row < 0 or col < 0 or row >= len(map_data)\
            or col >= len(map_data[0]) or map_data[row][col] == 0:
                return ''
        
        if map_data[row][col] == 8:
            return direction + 'G!'
        
        key = f'{row}-{col}'
        if key in self._memo.keys():
            return  self._memo[key]
        
        map_data[row][col] = 0
        
        n = self._traverse(map_data, row-1, col, 'N')
        s = self._traverse(map_data, row+1, col, 'S')
        e = self._traverse(map_data, row, col+1, 'E')
        w = self._traverse(map_data, row, col-1, 'W')
        
        map_data[row][col] = 1
        
        valid_paths = [x for x in [n,s,e,w] if x]
        if not valid_paths:
            self._memo[key] = ''
            return ''
        
        path = direction + min(valid_paths, key=len)
        
        if len(valid_paths) > 1:
            self._memo[key] = path
        
        return  path

      
# Execution

t1 = time.process_time()
path5 = TraverseWithMemo().traverse(maze6_map)
t2 = time.process_time()

print(path5)
print(t2 - t1)
