"""
Single Source Shortest Path
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
"""
from lib.graph.dijkstra import Dijkstra

if __name__ == '__main__':
    V_n, E_n, s = map(int, input().split())
    route_map = [dict() for _ in range(V_n)]

    for i in range(E_n):
        u, v, a = map(int, input().split())
        u, v = u, v
        route_map[u][v] = a

    # 返回从起点到每个顶点的最短距离的列表
    dijkstra_result = Dijkstra(route_map, s).execute()

    for v in dijkstra_result:
        if v == float('inf'):
            print('INF')
        else:
            print(v)
