class Solution(object):
    def findCrossingTime(self, n, k, time):
        """
        :type n: int
        :type k: int
        :type time: List[List[int]]
        :rtype: int
        """
        # Sort workers based on their efficiency
        time.sort(key=lambda x: (-x[0] - x[2], x[3]))

        # Create heap for left and right side of the bridge
        left_heap = []
        right_heap = []

        current_time = 0
        boxes_left = n
        left_worker_times = [-1] * k

        while boxes_left > 0:
            # Move workers from right to left
            while right_heap and right_heap[0][1] <= current_time:
                worker_index, end_time = heapq.heappop(right_heap)
                left_heap.append((current_time + time[worker_index][3], worker_index))

            # Move workers from left to right
            while left_heap and left_heap[0][0] <= current_time:
                end_time, worker_index = heapq.heappop(left_heap)
                left_worker_times[worker_index] = current_time
                heapq.heappush(right_heap, (current_time + time[worker_index][2], worker_index))
                boxes_left -= 1

            # Add waiting workers on the left side to the right heap
            while left_heap and left_heap[0][0] > current_time:
                end_time, worker_index = heapq.heappop(left_heap)
                heapq.heappush(right_heap, (end_time, worker_index))

            # Move a worker from the right side to the left side if the bridge is free
            if right_heap:
                end_time, worker_index = heapq.heappop(right_heap)
                current_time = max(current_time, time[worker_index][0])
                heapq.heappush(left_heap, (current_time + time[worker_index][1], worker_index))
            else:
                current_time += 1

        # Find the time at which the last worker reaches the left bank
        last_worker_time = max(left_worker_times)

        return last_worker_time
        