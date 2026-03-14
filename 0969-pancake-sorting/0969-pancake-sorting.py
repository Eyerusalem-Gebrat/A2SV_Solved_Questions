class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = []
        sort = sorted(arr)
        n = len(arr)

        j = n - 1
        for i in range(n):
            ind = arr.index(sort[j])
            if ind == j:
                j -= 1
                continue
            if ind != 0:
                k.append(ind+1)
                arr[:ind+1] = arr[:ind+1][::-1]
            k.append(j+1)
            arr[:j+1] = arr[:j+1][::-1]
            j -= 1

        return k