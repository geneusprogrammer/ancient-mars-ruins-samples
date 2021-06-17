using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;

namespace Algorithms
{
    public class Maze
    {
        int[,] maze = new int[20, 20]
        {
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 },
            {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 },
            {0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1 }
        };


        private bool IsOpen(int[,] map, int row, int col) =>
            row < map.GetLength(0) && row >= 0 &&
            col < map.GetLength(1) && col >= 0 &&
            map[row, col] != 0;

        public string Traverse() =>
            Traverse(maze, new List<ValueTuple<int, int, string>> { (0, 0, "B") });

        private string Traverse(int[,] map, IList<ValueTuple<int, int, string>> points)
        {
            var childPoints = new List<ValueTuple<int, int, string>>();

            foreach(var point in points)
            {
                var (row, col, direction) = point;

                if (map[row, col] == 0) continue;

                if (map[row, col] == 8)
                    return direction + "G!";

                map[row, col] = 0;

                if (IsOpen(map, row - 1, col))
                    childPoints.Add((row - 1, col, direction + "N"));

                if (IsOpen(map, row + 1, col))
                    childPoints.Add((row + 1, col, direction + "S"));

                if (IsOpen(map, row, col + 1))
                    childPoints.Add((row, col + 1, direction + "E"));

                if (IsOpen(map, row, col - 1))
                    childPoints.Add((row, col - 1, direction + "W"));
            }
            return childPoints.Count > 0 ? Traverse(map, childPoints) : "NONE";
        }
    }
}
