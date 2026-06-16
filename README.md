# Campus-Navigator-smart-Route-optimizer-

**Overview**

Campus Navigator & Smart Route Optimizer is an interactive route optimization application designed to solve real-world navigation challenges within a campus environment using graph-based algorithms and efficient pathfinding techniques.

The application models campus infrastructure as a weighted graph, where locations are represented as nodes and connecting pathways are represented as edges. It leverages Dijkstra's algorithm and priority queues (heaps) to compute the shortest and most efficient route between selected destinations.

The system also includes a road-block simulation feature that dynamically recalculates alternative routes when specific locations become unavailable, demonstrating adaptability in changing environments.

This project was developed to bridge theoretical Data Structures and Algorithms (DSA) concepts with practical software engineering applications. It showcases problem-solving abilities, algorithmic thinking, and the implementation of optimization techniques through an interactive user interface built with Streamlit.


**Features**

- Interactive campus navigation system
- Shortest path computation using Dijkstra's algorithm
- Dynamic road-block simulation
- Route recalculation and optimization
- Graph visualization of campus locations
- Distance calculation between locations
- User-friendly interface

**Technologies Used**

- Python
- Streamlit
- NetworkX
- Matplotlib


**Data Structures & Algorithms Used**

- Graphs
- Priority Queue (Heap)
- Dijkstra's Algorithm
- Hash Maps (Dictionaries)


**Project Structure**

campus_navigator/

- app.py
- graph_data.py
- algorithms.py
- requirements.txt
  

**Installation**

Install dependencies:
python -m pip install -r requirements.txt

Run the application:
python -m streamlit run app.py


**Future Enhancements**

- Multiple route recommendations
- Estimated travel time prediction
- Interactive map integration
- Enhanced UI and analytics dashboard

  
