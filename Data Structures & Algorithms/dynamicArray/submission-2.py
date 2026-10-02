class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.length = 0
        self.arr = [0] * self.cap


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.cap:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # print(self.length)
        # print(self.arr)
        # print(self.cap)
        # print(self.arr[self.length])
        popped = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length -= 1
        return popped

        # if self.length > 0:
        #     # soft delete the last element
        #     self.length -= 1
        # # return the popped element
        # return self.arr[self.length]

    def resize(self) -> None:
        new_arr = [0] * self.cap
        self.arr += new_arr
        self.cap *= 2


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap
