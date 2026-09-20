class Solution:
  def minCut(self, s: str) -> int:
    n = len(s)
    # isPalindrome[i][j] := True if s[i..j] is a palindrome
    isPalindrome = [[True] * n for _ in range(n)]
    # dp[i] := the minimum cuts needed for a palindrome partitioning of s[0..i]
    dp = [n] * n

    for l in range(2, n + 1):
   
      

