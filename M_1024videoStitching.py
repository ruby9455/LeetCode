class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
      # sort the clips according to the starting time
      clips.sort()
      
      # initialise
      dp = [sys.maxsize] * 100 # 1 <= time <= 100
      
      # base case
      df[0] = 0
      
      # DP
      for start, end in clips:
        # if the clip already cover the time interval
        if start >= time:
          break
          
        for i in range(start, end + 1):
          # dp[start] = clips needed to cover 0 to curr starting point
          dp[i] = min(dp[i], dp[start] + 1)
          
      # return dp[time] if dp[time] has been modified after initialisaiton
      return dp[time] if dp[time] < sys.maxsize else -1
