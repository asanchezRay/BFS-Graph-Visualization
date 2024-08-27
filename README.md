# BFS-Graph-Visualization
A Python tool for visualizing the Breadth-First Search (BFS) algorithm on large graphs with real-time queue interaction.

# BFS Graph Visualization

This repository provides a Python tool for visualizing the Breadth-First Search (BFS) algorithm on large graphs (30-60 nodes). The tool highlights how BFS explores nodes in a graph and displays real-time updates to the FIFO queue used by the algorithm.

## Features

- **Visualize BFS on Large Graphs:** The tool includes examples of graphs with 30-40 nodes, including random, scale-free, and small-world graphs.
- **Real-time Queue Interaction:** See how the BFS algorithm interacts with the queue, adding and removing nodes as the search progresses.
- **Customizable Graph Types:** Easily modify or add new graph types for different BFS visualizations.

## Prerequisites

Make sure you have Python installed on your machine. You'll also need to install the following Python packages:

```
pip install networkx matplotlib
```

## How to use

### Clone the repository:
```
git clone https://github.com/asanchezRay/BFS-Graph-Visualization.git
cd BFS-Graph-Visualization
```


### Run the BFS Visualization:
Run the Python script to see BFS in action on different types of large graphs:

```
python bfs_visualization.py
```
The visualization will show the graph and a live update of the BFS queue.

### Example Graphs

The tool includes three types of graphs for visualization:
- **Random Graph:** A graph with 30 nodes and 60 edges.
- **Scale-Free Graph:** A graph with 35 nodes generated using the Barabási-Albert model.
- **Small-World Graph:** A graph with 40 nodes generated using the Watts-Strogatz model.

### Customization

Feel free to modify the graph types, node counts, or even the BFS visualization settings to suit your needs. You can do this by editing the create_large_graphs() function in the bfs_visualization.py file.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

Contributions are welcome! If you have any improvements or new features in mind, feel free to open an issue or create a pull request.
