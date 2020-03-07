class Relation:
    M = set()
    R = set()

    def contains(self, *elements):
        return tuple(elements) in self.R

    def add(self, *elements):
        self.R.add(tuple(elements))

    def remove(self, *elements):
        self.R.remove(tuple(elements))

    def union(self, R2):
        return self.R.union(R2)

    def intersection(self, R2):
        return self.R.intersection(R2)

    def subtraction(self, R2):
        return self.R.difference(R2) 
