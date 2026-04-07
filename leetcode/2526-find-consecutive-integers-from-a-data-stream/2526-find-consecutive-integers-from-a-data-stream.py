from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
        
        if len(self.queue) > self.k:
            delete = self.queue.popleft()
            if delete == self.value:
                self.count -= 1
            
        if len(self.queue) == self.k and self.count == self.k:
            return True
        else:
            return False



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)