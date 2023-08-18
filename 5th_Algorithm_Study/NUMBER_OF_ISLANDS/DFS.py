# 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하는 문제
# 입력       입력
# -----      -----  
# 11110      11000
# 11010      11000
# 11000      00100
# 00000      00011
# -----      -----
# 출력:1     출력:3

def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(i,j):
        # 더 이상 땅이 아닌 경우 종료 -> 0일 경우
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid) or \
            grid[i][j] != '1':
                return

        grid[i][j] = 0

        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 추가
                count += 1
    return count
