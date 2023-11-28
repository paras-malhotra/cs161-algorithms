# CS161 Algorithms 🚀

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/paras-malhotra/cs161-algorithms/tests.yml?style=flat-square&logo=github&label=Tests)


## Overview
This repository contains Python implementations of algorithms covered in Stanford's CS161 course and comprehensive unit tests using pytest.

## Getting Started

### Using pip
```bash
git clone git@github.com:paras-malhotra/cs161-algorithms.git
cd cs161-algorithms
pip install -r requirements.txt
```

### Using Conda
```bash
git clone git@github.com:paras-malhotra/cs161-algorithms.git
cd cs161-algorithms
conda env create -f environment.yml
conda activate cs161
```

## Running Tests
Run the tests using pytest:
```bash
pytest
```

## Sorting Algorithms
| Algorithm     | Best Running Time | Average Running Time | Worst Running Time | Space Complexity | In Place | Stable | Type         | Ideal Use Case                        | Link |
|---------------|-------------------|----------------------|--------------------|------------------|----------|--------|--------------|--------------------------------------|------|
| Insertion Sort| O(n)              | O(n<sup>2</sup>)     | O(n<sup>2</sup>)   | O(1)             | ✅      | ✅    | Comparison   | Small or nearly sorted data sets     | [Link](src/insertion_sort.py) |
| Merge Sort    | O(n log n)        | O(n log n)           | O(n log n)         | O(n)             | ❌      | ✅    | Comparison   | Large data sets; prioritizes stability| [Link](src/merge_sort.py) |
| Quick Sort    | O(n log n)        | O(n log n)           | O(n<sup>2</sup>)   | O(log n)         | ✅      | ❌    | Comparison   | Large datasets; less concern for stability | [Link](src/quick_sort.py) |
| Heap Sort     | O(n log n)        | O(n log n)           | O(n log n)         | O(n) or O(1)\*   | ✅/❌   | ❌    | Comparison   | Large data sets; prioritizes memory | [Link](src/heap_sort.py) |
| Bucket Sort   | O(n+k)            | O(n+k)               | O(n<sup>2</sup>)   | O(n+k)           | ❌      | ✅    | Other        | Large, uniformly distributed datasets | [Link](src/bucket_sort.py) |
| Radix Sort    | O(d(n+r))         | O(d(n+r))            | O(d(n+r))          | O(d(n+r))        | ❌      | ✅    | Other        | Large data sets with fixed-length keys | [Link](src/radix_sort.py) |

\* Heap sort's implementation in this repository is not O(1) but rather O(n). However, there is an O(1) implementation.

Note: Even though all algorithms can be modified to become stable, it may affect space complexity.

## Data Structures

| Data Structure           | Seq. Access | Search      | Insert     | Delete     | Extract Min | Union | Type        | Link                        |
|--------------------------|-------------|-------------|------------|------------|-------------|-------|-------------|-----------------------------|
| Linked List              | O(n)        | O(n)        | O(1)       | O(n)       | N/A         | N/A   | Linear      | [Link](src/linked_list.py)  |
| Stack                    | O(n)        | O(n)        | O(1)       | O(1)       | N/A         | N/A   | Linear      | Todo                        |
| Queue                    | O(n)        | O(n)        | O(1)       | O(1)       | N/A         | N/A   | Linear      | [Link](src/linked_queue.py) |
| Unsorted Array           | O(1)        | O(n)        | O(1)\*     | O(n)       | N/A         | N/A   | Linear      | Native                      |
| Sorted Array             | O(1)        | O(log n)    | O(n)       | O(n)       | N/A         | N/A   | Linear      | Native                      |
| Hash Table               | N/A         | O(1)\*      | O(1)\*     | O(1)\*     | N/A         | N/A   | Hash-based  | Todo                        |
| Binary Heap              | O(n)        | O(n)        | O(log n)   | O(log n)   | O(log n)    | N/A   | Tree        | [Link](src/binary_heap.py)  |
| Priority Queue           | O(n)        | O(n)        | O(log n)   | O(log n)   | O(log n)    | N/A   | Tree        | [Link](src/priority_queue.py)|
| AVL Tree (BST)           | O(log n)    | O(log n)    | O(log n)   | O(log n)   | N/A         | N/A   | Tree        | [Link](src/avl_tree.py)     |
| Red Black Tree  (BST)    | O(log n)    | O(log n)    | O(log n)   | O(log n)   | N/A         | N/A   | Tree        | Todo                        |
| Union Find               | N/A         | O(1)        | O(1)       | N/A        | N/A         | O(1)  | Disjoint Set| [Link](src/union_find.py)   |

\* Amortized time complexity

## Single Source Shortest Path Algorithms

| Algorithm            | Time Complexity | Space Complexity | Unweighted Graphs | Cyclic | Positive Weights | Negative Weights | Negative Cycle Detection | Link |
|----------------------|-----------------|------------------|-------------------|--------|------------------|------------------|--------------------------|------|
| Breadth-First Search | O(V + E)        | O(V)             | ✅                | ✅    | ❌              | ❌               | ❌                      | [Link](src/breadth_first_search.py) |
| DAG Shortest Path    | O(V + E)        | O(V)             | ✅                | ❌    | ✅              | ✅               | ❌                      | [Link](src/dag_shortest_path.py) |
| Dijkstra             | O(V log V + E)  | O(V)             | ✅                | ✅    | ✅              | ❌               | ❌                      | [Link](src/dijkstra.py) |
| Bellman-Ford         | O(VE)           | O(V)             | ✅                | ✅    | ✅              | ✅               | ✅                      | [Link](src/bellman_ford.py) |

\* V: Number of vertices, E: Number of edges

## All Pairs Shortest Path Algorithms

| Algorithm            | Time Complexity             | Space Complexity | Unweighted Graphs | Cyclic | Positive Weights | Negative Weights | Negative Cycle Detection | Link |
|----------------------|-----------------------------|------------------|-------------------|--------|------------------|------------------|--------------------------|------|
| Breadth-First Search | O(V<sup>2</sup> + VE)       | O(V<sup>2</sup>) | ✅                | ✅    | ❌              | ❌               | ❌                      | [Link](src/breadth_first_search.py) |
| DAG Shortest Path    | O(V<sup>2</sup> + VE)       | O(V<sup>2</sup>) | ✅                | ❌    | ✅              | ✅               | ❌                      | [Link](src/dag_shortest_path.py) |
| Dijkstra             | O(V<sup>2</sup> log V + VE) | O(V<sup>2</sup>) | ✅                | ✅    | ✅              | ❌               | ❌                      | [Link](src/dijkstra.py) |
| Johnson              | O(V<sup>2</sup> log V + VE) | O(V<sup>2</sup>) | ✅                | ✅    | ✅              | ✅               | ✅                      | [Link](src/johnson.py) |
| Floyd-Warshall       | O(V<sup>3</sup>)            | O(V<sup>2</sup>) | ✅                | ✅    | ✅              | ✅               | ✅                      | [Link](src/floyd_warshall.py) |

\* V: Number of vertices, E: Number of edges

## Other Graph Algorithms

| Algorithm                 | Time Complexity | Space Complexity | Use Cases                        | Link                                 |
|---------------------------|-----------------|------------------|----------------------------------|--------------------------------------|
| Topological Sort          | O(V + E)        | O(V)             | Scheduling, task ordering        | [Link](src/depth_first_search.py)    |
| Checking Bipartite        | O(V + E)        | O(V)             | Bipartition validation           | [Link](src/breadth_first_search.py)  |
| Connected Components      | O(V + E)        | O(V)             | Network analysis, clustering     | [Link](src/depth_first_search.py)    |
| Depth-First Search        | O(V + E)        | O(V)             | Pathfinding, tree traversals     | [Link](src/depth_first_search.py)    |
| MST (Prim's Algorithm)    | O(V log V + E)  | O(V + E)         | Network design, clustering       | [Link](src/minimum_spanning_tree.py) |
| MST (Kruskal's Algorithm) | O(E log E)      | O(V + E)         | Network design (sparse graphs)   | [Link](src/minimum_spanning_tree.py) |

\* V: Number of vertices, E: Number of edges

## Other Algorithms

| Algorithm                  | Time Complexity      | Space Complexity | Strategy                | Use Cases                            | Link                                      |
|----------------------------|----------------------|------------------|-------------------------|--------------------------------------|-------------------------------------------|
| Binary Search              | O(log n)             | O(1)             | Divide and Conquer      | Sorted data lookup, monotonic function inverse | [Link](src/binary_search.py)    |
| Karatsuba Multiplication   | O(n<sup>1.585</sup>) | O(n)             | Divide and Conquer      | Large number multiplication          | [Link](src/karatsuba.py)                  |
| Kth Order Statistics       | O(n)                 | O(1)             | Divide and Conquer      | Finding kth smallest/largest element | [Link](src/select_k.py)                   |
| Fibonacci Sequence         | O(n)                 | O(1)             | Dynamic Programming     | Generating Fibonacci numbers         | [Link](src/fibonacci.py)                  |
| Unbounded Knapsack         | O(nW)                | O(W)             | Dynamic Programming     | Dynamic resource allocation          | [Link](src/knapsack.py)                   |
| 0/1 Knapsack               | O(nW)                | O(nW)            | Dynamic Programming     | Resource allocation with constraints | [Link](src/knapsack.py)                   |
| Longest Common Subsequence | O(mn)                | O(mn)            | Dynamic Programming     | Text comparison, DNA sequencing      | [Link](src/longest_common_subsequence.py) |
| Huffman Coding             | O(n log n)           | O(n)             | Greedy                  | Data compression, encoding schemes   | [Link](src/huffman.py)                    |

## Algorithm Reductions

This section highlights algorithms that can be effectively reduced to a different, well-known algorithm, showcasing the versatility and interconnectedness of algorithms.

| Algorithm | Reduced To                          | Time Complexity   | Space Complexity | Application Scenario            | Link                   | Reference |
|-----------|-------------------------------------|-------------------|------------------|---------------------------------|------------------------|-----------|
| 2-SAT     | Strongly Connected Components (SCC) | O(n + m)          | O(n + m)         | Logical satisfiability problems | [Link](src/two_sat.py) | [Ref](https://cp-algorithms.com/graph/2SAT.html) |

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests (with unit tests if possible).

## License
This project is licensed under the [MIT License](LICENSE).
