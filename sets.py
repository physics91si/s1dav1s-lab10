class Set():
    def __init__(self):
        self.listset=[]
    def contains(self, element):
        for i in self.listset:
            if (i == element):
                return True
        return False
    def add(self, element):
        if (self.contains(element)==False):
            self.listset.append(element)
    def remove(self, element):
        if (self.contains(element)):
            self.listset.remove(element)
    def size(self):
        return self.listset.__len__()
    def __union__ (self, setB):
        u=Set()
        for element in self.listset:
            u.add(element)
        for element in setB.listset:
            u.add(element)
        return u
    def __intersection__ (self, setB):
        i=Set()
        for element in self.listset:
            if (setB.contains(element)):
                i.add(element)
        return i
    def __subtract__ (self, setB):
        s=Set()
        for element in self.listset:
            if not(setB.contains(element)):
                s.add(element)
        return s
    def __print__(self):
        print(self.listset)