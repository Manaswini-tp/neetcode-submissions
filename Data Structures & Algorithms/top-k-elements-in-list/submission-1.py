class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        freq_sorted = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        freq_list = []
        count = 1
        for key,value in freq_sorted.items():
            if count>k:
                break
            freq_list.append(key)
            count+=1
        return freq_list