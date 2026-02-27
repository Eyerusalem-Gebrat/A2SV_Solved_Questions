class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dic = {}
        maximum = 0
        for response in responses:
            for word in set(response):
                dic[word] = dic.get(word, 0) + 1
                maximum = max(maximum, dic[word])

        ans = None
        for key, val in dic.items():
            if val == maximum:
                if ans is None or key < ans:
                    ans = key

        return ans