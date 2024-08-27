import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import time

def bfs_visual(graph, start_node):
    visited = set()
    queue = deque([start_node])
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(12, 8))
    
    while queue:
        plt.clf()
        
        #Draw Graph
        node_colors = ['red' if node in visited else 'orange' if node in queue else 'lightblue' for node in graph.nodes()]
        nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=10)
        
        # Draw FIFO
        queue_text = f"Queue: {list(queue)}"
        plt.text(0.05, 0.95, queue_text, horizontalalignment='left', verticalalignment='top', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
        
        plt.pause(1)
        
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.neighbors(node):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    plt.show()

def create_large_graphs():
    # Grafo 1: Grafo aleatorio con 30 nodos
    G1 = nx.gnm_random_graph(30, 60)
    
    # Grafo 2: Grafo libre de escala con 35 nodos
    G2 = nx.barabasi_albert_graph(35, 2)
    
    # Grafo 3: Grafo de pequeño mundo con 60 nodos
    G3 = nx.watts_strogatz_graph(60, 4, 0.1)
    
    return [G1, G2, G3]

if __name__ == "__main__":
    graphs = create_large_graphs()
    start_nodes = [0, 0, 0]
    
    for i, graph in enumerate(graphs):
        print(f"Running BFS on Graph {i + 1}")
        bfs_visual(graph, start_nodes[i])
        time.sleep(4)
