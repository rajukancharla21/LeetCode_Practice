class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        totR,totC=len(grid),len(grid[0])
        def isValid(x,y):
            if x>=0 and x<totR and y>=0 and y<totC and grid[x][y]=="1":
                return True
            return False
        def dfs(i,j):
            grid[i][j]="-1"
            p=[[0,1],[0,-1],[1,0],[-1,0]]
            for d in p:
                ii,jj=i+d[0],j+d[1]
                if isValid(ii,jj):
                    dfs(ii,jj)
        for row in range(totR):
            for col in range(totC):
                if grid[row][col]=="1":
                    res+=1
                    dfs(row,col)
        return res