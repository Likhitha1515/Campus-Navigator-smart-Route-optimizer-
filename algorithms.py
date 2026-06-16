import heapq


def dijkstra(graph, start, end):

    distances = {
        node: float('inf')
        for node in graph
    }

    distances[start] = 0

    previous = {}

    pq = [(0, start)]

    while pq:
       current_distance, current_node = heapq.heappop(pq)

       if current_distance > distances[current_node]:
         continue

    for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    path = []

    current = end

    while current != start:

        path.append(current)

        current = previous.get(current)

        if current is None:
            return [], float('inf')

    path.append(start)

    path.reverse()

    return path, distances[end]