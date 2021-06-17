# Algorithm original OOP style

import numpy as np
import time
import sys

class TraverseMap:
    def traverse(self, map_data):
        map_np = np.array(map_data)
        assert isinstance(map_np, np.ndarray)
        assert len(map_np.shape) == 2
        return self._traverse(map_np)
        
    def _traverse(self, map_data, row=0, col=0, direction='B'):
        if row < 0 or col < 0 or row >= len(map_data)\
            or col >= len(map_data[0]) or map_data[row][col] == 0:
                return ''
        
        if map_data[row][col] == 8:
            return direction + 'G!'

        map_data[row][col] = 0
        
        n = self._traverse(map_data, row-1, col, 'N')
        s = self._traverse(map_data, row+1, col, 'S')
        e = self._traverse(map_data, row, col+1, 'E')
        w = self._traverse(map_data, row, col-1, 'W')

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
          
# Execution
print(TraverseMap().traverse(maze2_map))
