# Problem: Network Delay Time

**Leetcode Link:** [Leetcode 743 - Network Delay Time](https://leetcode.com/problems/network-delay-time/)

## Description:

You are given a weighted, directed graph represented by a list of times as directed edges, and an integer `k`, representing the source node. You must calculate the time it takes for all nodes to receive the signal starting from node `k`.

If it is impossible to reach all nodes, return -1.

## Approach:

- Use **Dijkstra's Algorithm** to find the shortest time to all nodes.
- Use a priority queue (min-heap) to process nodes in increasing order of signal arrival time.
- Maintain a distance map to store the shortest time for each node.
- If all nodes are visited, return the maximum value in the distance map.

## Time Complexity: O((E + V) \* logV)

## Space Complexity: O(V + E)

## Tags:

Graph, Dijkstra, Priority Queue, Shortest Path
