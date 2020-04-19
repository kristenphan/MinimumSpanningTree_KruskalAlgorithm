# Minimum Spanning Tree (MST): Kruskal's Algorithm

__Repository Description:__
<br/>
This repository stores the work as part of the Data Structures and Algorithms specialization courses by University California of San Diego. Course URL: https://www.coursera.org/specializations/data-structures-algorithms. Code in this repository is written by myself, Kristen Phan.
<br/>
<br/>
__Assignment Description:__
<br/>
Problem Introduction: In this problem, the goal is to build roads between some pairs of the
given cities such that there is a path between any two cities and the
total length of the roads is minimized.
<br/>
<br/>
Task: Given 𝑛 points on a plane, connect them with segments of minimum total length such that there is a
path between any two points. Recall that the length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
is equal to sqrt[(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2].
<br/>
<br/>
Input Format; The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point
(𝑥𝑖, 𝑦𝑖).
<br/>
<br/>
Constraints: 1 ≤ 𝑛 ≤ 200; −103 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 103 are integers. All points are pairwise different, no three
points lie on the same line.
<br/>
<br/>
Output Format: Output the minimum total length of segments. The absolute value of the difference
between the answer of your program and the optimal value should be at most 10−6. To ensure this,
output your answer with at least seven digits after the decimal point (otherwise your answer, while
being computed correctly, can turn out to be wrong because of rounding issues).
<br/>
<br/>
Time Limits: Python - 10 seconds
<br/>
<br/>
Memory Limit: 512MB.
<br/>
<br/>
__Disclaimer__: 
<br/>
If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)"
