class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_coords(pos):
            cols = len(matrix[0])
            return (pos // cols, pos % cols)
        
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows * cols - 1
        while low <= high:
            mid = (high + low) // 2
            row, col = get_coords(mid)
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                high = mid - 1
            else:
                low = mid + 1
        return False