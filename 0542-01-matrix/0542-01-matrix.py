from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        distance = [["."]*cols for i in range(rows)]
        visited = set()
        q = deque([])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    q.append(((i,j),0))
                    distance[i][j]=0
                    visited.add((i,j))
                    
        while q:
            (r,c),step = q.popleft()
            
            for dr,dc in directions:
                row = r+dr
                col = c+dc
                
                if row not in range(rows) or col not in range(cols) or (row,col) in visited or mat[row][col]==0:
                    continue
                    
                visited.add((row,col)) 
                distance[row][col]=step+1
                q.append(((row,col),step+1))
                
        return distance 