class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
      # base case: endWord not found
      if endWord not in wordList: return 0
      
      # beginWord may not in wordList, add it
      wordList.append(beginWord)
      # hold all possible pattern
      patternDict = collections.defaultdict(list)
      
      # build adjacency list
      for word in wordList:
        for j in range(len(word)):
          pattern = word[:j] + "+" + word[j+1:]
          patternDict[pattern].append(word)
      
      # bfs
      # initialise with beginWord
      visit = set([beginWord])
      q = collections.deque([beginWord])
      result = 1
      # extract word from q
      while q:
        for i in range(len(q)):
          word = q.popleft()
          # base case: if equals the endWord
          if word == endWord:
            return result
          # turn the word into pattern, then find the word with the same pattern
          for j in range(len(word)):
            pattern = word[:j] + "" + word[j+1:]
            for similarWord in patternDict[pattern]:
              if similarWord not in visit:
                visit.add(similarWord)
                q.append(similarWord)
        result += 1
