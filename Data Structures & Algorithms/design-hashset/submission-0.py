class MyHashSet:

    def __init__(self):
        self.hashmap = [False] * 1000001

    def add(self, key: int) -> None:
        self.hashmap[key] = True

    def remove(self, key: int) -> None:
        self.hashmap[key] = False

    def contains(self, key: int) -> bool:
        return self.hashmap[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)