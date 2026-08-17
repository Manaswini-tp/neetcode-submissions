class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        n = len(position)
        for i in range(n):
            stack.append([position[i], speed[i]])
        stack.sort(reverse=True)
        time = [0]*n
        for i in range(n):
            time[i] = (target-stack[i][0])/stack[i][1]
        count = 1
        curr = time[0]
        for i in range(1,n):
            if curr>=time[i]:
                continue
            count+=1
            curr = time[i]
        return count