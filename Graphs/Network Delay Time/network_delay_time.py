# Leetcode 743 - Network Delay Time
# Time: O((E + V) * logV)
# Space: O(V + E)

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = {}
        adj_list = defaultdict(list)
        
        for u, v, w in times:
            adj_list[u].append((v, w))

        pq = [(0, k)]  # (current_time, node)

        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            if curr_node in distance:
                continue
            distance[curr_node] = curr_time

            for neighbor, time in adj_list[curr_node]:
                if neighbor not in distance:
                    heapq.heappush(pq, (curr_time + time, neighbor))

        if len(distance) != n:
            return -1
        return max(distance.values())
