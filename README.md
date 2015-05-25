# Traveling Salesman Problem

This is the last project for the Graph Theory class @ UFRJ.

What we done here was trying different approachs to approximate solution of the Euclidian TSP.
We then combined some of them and plotted out the results.

## The algorithms

We used four algorithms: 

* **Genetic Algorithm**: The first and simpler approach was trying to implement it with a genetic algorithm.
This was simple to do for the first and smaller cases, we actually didn't tought about the problem and just
wrote the commmon genetic algorithm with the cost function being the sum of all edges.

* **Greedy with 2opt optimization**: Our second approach was to do what everyoneelse was trying to do.
Just run a greedy algorithm and run with 2opt optimization, which in our case was done with the euclidean
simplification. (Just checking if the edges were crossing.

* **MST+DFS**: Our third approach was, as we've seen on some papers, to run a MST+BFS.

* **Amorim's Algorithm**: Our last approach was to try to create a new algorithm.
The main point of this algorithm is making a smarter greedy algorithm. Instead of picking the closest
point, we look to all the edges sorted from the lightest to the heaviest and add edges that do not link
to the middle of another path nor creates a cycle.

* **Amorim's Algorithm + 2opt**: As this algorithm gave us really good 1st shot but with some edges crossing,
we decided to run 2opt optimization to get better yet results.

#### Results

The table belows shows the result (sum of edges) for each algorithm

| Algorithm     | 5       | 10      | 20      | 50      | 100      | 200      | 500      | 1000     | 2000     | 5000      | 10000    |
|:-------------:|:-------:|:-------:|:-------:|:-------:|:--------:|:--------:|:--------:|:--------:|:--------:|:---------:|:--------:|                                                        
| Genetic       | 2115293 | 3487592 | 4143998 | 7209944 | 9241248  | 16324823 | 30843830 | 44704344 | 64321060 | 101418657 |          |
| Greedy+2opt   | 2115293 | 4914477 | 5878573 | 7732150 | 11262244 | 15641890 | 25155354 | 34685640 | 49434559 | 88584392  |          |
| MST+DFS       | 2115293 | 3878649 | 4582949 | 6773072 | 9927885  | 13336644 | 21239251 | 29437728 | 41503373 | 65988039  | 93165982 |
| Amorim's+2opt | 2115293 | 3747949 | 4259563 | 5781312 | 8943129  | 10943885 | 18461195 | 25678535 | 34997859 | 55895610  | 79514170 |

You can see the images for them in

* [Genetic Results](/genetic)
* [Greedy+2opt Results](/2opt)
* [Amorim's Results](/amorim_v3)
* [MST+DFS](/mstdfs)

#### Why I liked the Amorim's algorithm

The first result, before the 2opt was really good.
Check this comparison between Amorim's and MST+DFS

##### Amorim
Sum of Edges: 83586646
![Amorim](/amorim_v3/points-10000_amorim.png)

##### MST+DFS
Sum of Edges: 102805367
![MST+DFS](/mstdfs/points-10000_mst_dfs.png)

#### A note on Amorim's Algorithm Complexity

The first implementation of Amorim's algorithm had complexity of O(n^3) given the fact that I had to join
paths constantly. However, given that only the two vertices of each edge of a path are important on each run,
I abstracted the path as a tree of subpaths. Where each node of the tree was represented by (NL, NR, PL, PR, INV).
Where NL and NR are the Left and Right nodes at the time this was the root, PL and PR are pointers to another node,
representing the path on the left and on the right and INV is a flag to indicate that this path are inverted when
merged to another path.

With this, I can merge paths in O(1) and when I have the final path, i traverse them in O(n)

Given this and given N = the number of vertices and M = N^2 = number of edges,
We have for our three steps for our algorithm

* Sort the edges (O(N^2*log(N^2)) = O(N^2*log(N)) )
* Chec all edges and merge if needed (O(N^2))
* Traverse the final path (O(N))

So the final complexity is O(N^2*log(N))
