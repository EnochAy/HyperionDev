#anagram.py
class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for i in strs:
          x = "".join(sorted(strs)) #TypeError: sorted expected 1 argument, got 0
          if x in result:
              result[x].append(i)
        else:
            result[x] = [i]
            return(list(result.values()))
ob1 = Solution()

print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
