class Solution:
  def sumNumbers(self, root: TreeNode | None) -> int:
    ans = 0

    def dfs(root: TreeNode | None, path: int) -> None:
      nonlocal ans
      if not root:
   
