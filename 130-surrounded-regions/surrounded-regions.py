class Solution:
  def solve(self, board: list[list[str]]) -> None:
    if not board:
      return

    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(board)
    n = len(board[0])
    q = collections.deque()

    for i in range(m):
      for j in range(n):
        if i * j == 0 or i == m - 1 or j == n - 1:
          if board[i][j] == 'O':
            q.append((i, j))
         
      

