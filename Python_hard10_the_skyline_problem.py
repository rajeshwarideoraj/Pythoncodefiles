class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        # Create a list to store the building points
        building_points = []
        
        # Convert the building information into building points
        for left, right, height in buildings:
            # Use negative height for the start point of the building
            building_points.append((left, -height, right))
            # Use positive height for the end point of the building
            building_points.append((right, 0, 0))
        
        # Sort the building points based on their x-coordinate and heights
        building_points.sort()
        
        # Max heap to store the heights of the active buildings
        max_heap = [(0, float('inf'))]
        
        for left, neg_height, right in building_points:
            # If it's the start point of the building, add it to the max heap
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, right))
            # If it's the end point of the building, remove it from the max heap
            else:
                while max_heap[0][1] <= left:
                    heapq.heappop(max_heap)
            
            # Get the current max height from the max heap
            current_max_height = -max_heap[0][0]
            
            # If the max height changes, add the current point to the result
            if not result or current_max_height != result[-1][1]:
                result.append([left, current_max_height])
        
        return result
        