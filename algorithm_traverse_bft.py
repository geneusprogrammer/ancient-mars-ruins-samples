# Breadth First Traversal (BFT)

import numpy as np
import time
import sys

class TraverseBFT:
    def traverse(self, map_data):
        map_np = np.array(map_data)
        assert isinstance(map_np, np.ndarray)
        assert len(map_np.shape) == 2
        trav_map = self._traverse(map_np)
        return trav_map
    
    def _is_open(self, map_data, row, col):
        return row >= 0 and col >= 0 and \
                row < len(map_data) and col < len(map_data[0]) and \
                map_data[row][col] != 0
    
    def _traverse(self, map_data, points=[(0,0,'B')]):
        
        child_points = []
        
        for point in points:
            row, col, direction = point
            
            if map_data[row][col] == 0: continue
            
            if map_data[row][col] == 8:
                return direction + 'G!'
        
            map_data[row][col] = 0
        
            if self._is_open(map_data, row-1, col):
                child_points.append((row-1,col,direction+'N'))
        
            if self._is_open(map_data, row+1, col):
                child_points.append((row+1,col,direction+'S'))
        
            if self._is_open(map_data, row, col+1):
                child_points.append((row,col+1,direction+'E'))
        
            if self._is_open(map_data, row, col-1):
                child_points.append((row,col-1,direction+'W'))
                
        return self._traverse(map_data, child_points) if child_points else 'NONE'
      
      
# Execution
t1 = time.process_time()
path6 = TraverseBFT().traverse(maze6_map)
t2 = time.process_time()

print(path6)
print(t2 - t1)
