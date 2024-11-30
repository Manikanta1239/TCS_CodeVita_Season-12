# TCS_CodeVita_Season-12
## Desert Queen
Problem Description
The Desert Queen train takes you through the heart of the Thar Desert. It is a great way to travel and experience the Thar desert.

A group of tourists arrived for a sightseeing tour of the Thar Desert. Traveling through the Thar Desert is challenging without the assistance of the Desert Queen train. This train crosses the desert, picking up tourists from various locations. The Thar Desert is represented by a square matrix, featuring mountains, train tracks, and stretches of desert, denoted by the elements M, T, and D, respectively.

You are also given two elements: 'S' representing the start position and 'E' representing the end position. You can board or exit the train at any location. Water is essential in the desert, and except for moving from T to T, every cell transition costs 1 unit of water. You cannot travel to a cell with mountains.

Given a grid of size N*N with above elements, find a path between the start and end, such that less amount of water is consumed. The train track will be continuous, have turns and will not have branches.

Constraints
0 < N < 25

Input
First line consists of single Integer N, representing the size of the grid.
Next N lines consist of N space separated Elements which are either {D, T, M, S or E}.

Output
Print a single integer representing minimum water required to reach destination.

Time Limit (secs)
1

Examples
--------
Example 1

Input
4
S D D D
T T T T
D D D D
D E D D

Output
3

Explanation

From the input we know that it is 4*4 grid, with start at (0,0) and end at (3,1). Left top element is (0, 0) and right bottom element is (3, 3).
The path on which water will be consumed the least is (0, 0), (1, 0), (1, 1), (2, 1), (3, 1). The water consumption will be 1+0+1+1 = 3
Therefore, print 3, which is the minimum possible value.

Example 2

Input
5
S D D D M
T T T T D
D D D T D
D M D T D
D D D T E

Output
2

Explanation
From the input we know that it is 5*5 grid, with start at (0,0) and end at (4,4). Left top element is (0, 0) and right bottom element is (4, 4).
The path that water will be consumed less is (0,0), (1,0), (1,1), (1,2), (1,3), (2,3), (3,3), (4,3), (4,4). The water consumption will be 1 + 0 + 0 + 0 + 0 + 0 + 0 + 1 = 2
Therefore, print 2, which is the minimum possible value.
