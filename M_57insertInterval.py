class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # without overlapping
            # 1. end of new interval < start of intervals
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # 2. start of new interval > end of intervals
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # with overlapping
            # update with min of start and max of end
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
                
        result.append(newInterval)

        return result
