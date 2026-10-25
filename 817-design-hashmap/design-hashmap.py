class MyHashMap(object):
    def __init__(self):
        self.map = []
    def put(self, key, value):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map[i][1] = value
                return
        self.map.append([key, value])
    def get(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                return self.map[i][1]
        return -1
    def remove(self, key):
        for i in range(len(self.map)):
            if self.map[i][0] == key:
                self.map.pop(i)
                return

