import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)

    while len(cables) > 1:

        cost = heapq.heappop(cables) + heapq.heappop(cables)

        heapq.heappush(cables, cost)

    return cost


cable_lengths = [4, 2, 7, 6, 17, 32]
total_min_cost = min_cost_to_connect_cables(cable_lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {total_min_cost}")
