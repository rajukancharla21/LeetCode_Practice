class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m=len(image),len(image[0])
        visited = []
        newImage=[]
        for _ in range(n):
            visited.append([0]*m)
            newImage.append(image[_].copy())
        def isValid(i, j):
            if i >= 0 and i < n and j >= 0 and j < m and visited[i][j] == 0 and image[i][j] == image[sr][sc]:
                return True
            return False
        
        def dfs(x,y):
            p=[[0,1],[0,-1],[1,0],[-1,0]]
            newImage[x][y]=color
            visited[x][y]=1
            for i in p:
                xx,yy=x+i[0],y+i[1]
                if isValid(xx,yy):
                    dfs(xx,yy)
        dfs(sr,sc)
        return newImage
        
        
        