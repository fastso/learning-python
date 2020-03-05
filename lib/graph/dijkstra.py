import heapq


class Dijkstra:

    def __init__(self, rote_map, start_point, goal_point=None):
        self.rote_map = rote_map
        self.start_point = start_point
        self.goal_point = goal_point

    def execute(self):
        num_of_city = len(self.rote_map)
        dist = [float("inf") for _ in range(num_of_city)]
        prev = [float("inf") for _ in range(num_of_city)]

        dist[self.start_point] = 0
        heap_q = []
        heapq.heappush(heap_q, (0, self.start_point))
        while len(heap_q) != 0:
            prev_cost, src = heapq.heappop(heap_q)

            if dist[src] < prev_cost:
                continue

            for dest, cost in self.rote_map[src].items():
                if cost != float("inf") and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(heap_q, (dist[dest], dest))
                    prev[dest] = src
        if self.goal_point is not None:
            return self.get_path(self.goal_point, prev)
        else:
            return dist

    def get_path(self, goal, prev):
        path = [goal]
        dest = goal

        while prev[dest] != float("inf"):
            path.append(prev[dest])
            dest = prev[dest]

        return list(reversed(path))


n = int(input())
s, t = map(int, input().split())
route_map = [dict() for _ in range(n)]
for i in range(n):
    u, v, a = map(int, input().split())
    u, v = u - 1, v - 1
    route_map[u][v] = a

# 返回从起点到每个顶点的最短距离的列表
dijkstra_result = Dijkstra(route_map, s - 1).execute()

# 从起点到终点的最短距离
dijkstra_result = Dijkstra(route_map, s - 1, t - 1).execute()
