# CS161 Algorithms 🚀

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

\* Heap sort's current implementation is not O(1) but rather O(n). However, it can be made O(1) if the underlying heap array is shared with the input data.

Note: Even though all algorithms can be modified to become stable, it may affect space complexity.

## Data Structures

| Data Structure           | Seq. Access | Search      | Insert         | Delete        | Extract Min | Type       | Link |
|--------------------------|-------------|-------------|----------------|---------------|-------------|------------|------|
| Linked List              | O(n)        | O(n)        | O(1)           | O(n)          | N/A         | Linear     | [Link](src/linked_list.py) |
| Stack                    | O(n)        | O(n)        | O(1)           | O(1)          | N/A         | Linear     | Todo |
| Queue                    | O(n)        | O(n)        | O(1)           | O(1)          | N/A         | Linear     | [Link](src/queue.py) |
| Unsorted Array           | O(1)        | O(n)        | O(1)\*         | O(n)          | N/A         | Linear     | Native |
| Sorted Array             | O(1)        | O(log n)    | O(n)           | O(n)          | N/A         | Linear     | Native |
| Hash Table               | N/A         | O(1)\*      | O(1)\*         | O(1)\*        | N/A         | Hash-based | [Link](src/hash_table.py) |
| Binary Heap              | O(n)        | O(n)        | O(log n)       | O(log n)      | O(log n)    | Tree       | [Link](src/binary_heap.py) |
| Priority Queue           | O(n)        | O(n)        | O(log n)       | O(log n)      | O(log n)    | Tree       | [Link](src/priority_queue.py) |
| AVL Tree (BST)           | O(log n)    | O(log n)    | O(log n)       | O(log n)      | N/A         | Tree       | [Link](src/avl_tree.py) |
| Red Black Tree  (BST)    | O(log n)    | O(log n)    | O(log n)       | O(log n)      | N/A         | Tree       | Todo |

\* Amortized time complexity

## Single Source Shortest Path Algorithms

| Algorithm            | Time Complexity | Space Complexity | Unweighted Graphs | Cyclic | Positive Weights | Negative Weights | Negative Cycle Detection | Link |
|----------------------|-----------------|------------------|-------------------|--------|------------------|------------------|--------------------------|------|
| Breadth-First Search | O(V + E)        | O(V)             | ✅                | ✅    | ❌              | ❌               | ❌                      | [Link](src/breadth_first_search.py) |
| DAG Shortest Path    | O(V + E)        | O(V)             | ✅                | ❌    | ✅              | ✅               | ❌                      | [Link](src/dag_shortest_path.py) |
| Dijkstra             | O(V + E log V)  | O(V)             | ✅                | ✅    | ✅              | ❌               | ❌                      | [Link](src/dijkstra.py) |
| Bellman-Ford         | O(VE)           | O(V)             | ✅                | ✅    | ✅              | ✅               | ✅                      | [Link](src/bellman_ford.py) |

\* V: Number of vertices, E: Number of edges

## All Pairs Shortest Path Algorithms

| Algorithm            | Time Complexity             | Space Complexity | Unweighted Graphs | Cyclic | Positive Weights | Negative Weights | Negative Cycle Detection | Link |
|----------------------|-----------------------------|------------------|-------------------|--------|------------------|------------------|--------------------------|------|
| Breadth-First Search | O(V(V + E))                 | O(V<sup>2</sup>) | ✅                | ✅    | ❌              | ❌               | ❌                      | [Link](src/breadth_first_search.py) |
| DAG Shortest Path    | O(V(V + E))                 | O(V<sup>2</sup>) | ✅                | ❌    | ✅              | ✅               | ❌                      | [Link](src/dag_shortest_path.py) |
| Dijkstra             | O(V<sup>2</sup> + VE log V) | O(V<sup>2</sup>) | ✅                | ✅    | ✅              | ❌               | ❌                      | [Link](src/dijkstra.py) |
| Floyd-Warshall       | O(V<sup>3</sup>)            | O(V<sup>2</sup>) | ✅                | ✅    | ✅              | ✅               | ✅                      | [Link](src/floyd_warshall.py) |

\* V: Number of vertices, E: Number of edges

## Other Graph Algorithms

| Algorithm              | Time Complexity | Space Complexity | Use Cases                        | Link                                 |
|------------------------|-----------------|------------------|----------------------------------|--------------------------------------|
| Topological Sort       | O(V + E)        | O(V)             | Scheduling, task ordering        | [Link](src/depth_first_search.py)    |
| Checking Bipartite     | O(V + E)        | O(V)             | Bipartition validation           | [Link](src/breadth_first_search.py)  |
| Connected Components   | O(V + E)        | O(V)             | Network analysis, clustering     | [Link](src/depth_first_search.py)    |
| Depth-First Search     | O(V + E)        | O(V)             | Pathfinding, tree traversals     | [Link](src/depth_first_search.py)    |

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

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests (with unit tests if possible).

## License
This project is licensed under the [MIT License](LICENSE).
