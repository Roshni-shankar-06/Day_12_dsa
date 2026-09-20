class Solution:
  def candy(self, ratings: list[int]) -> int:
    n = len(ratings)

    ans = 0
    l = [1] * n
    r = [1] * n

 
    
