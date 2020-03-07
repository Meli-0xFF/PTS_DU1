class Relation:
    def __init__(self):
        self.R=set()
        self.M=set()

    def __iter__(self):
        return self.R.__iter__()

    def contains(self, *elements):
        return tuple(elements) in self.R

    def add(self, *elements):
        self.R.add(tuple(elements))

    def remove(self, *elements):
        self.R.remove(tuple(elements))

    def union(self, R2):
        self.R.union(R2.R)

    def intersection(self, R2):
        self.R.intersection(R2.R)

    def subtraction(self, R2):
        self.R.difference(R2.R)

    def inverse(self):
        self.R = set(map(lambda t : t[::-1], self.R))
 
    def composition(self, R2):
        res = set()
        for t1 in self.R:
            for t2 in R2.R:
                if t1[1] == t2[0]:
                    res.add((t1[0], t2[1]))
        self.R = set(res)

    def is_reflexive(self):
        return len(self.M) == len(filter(lambda m : True if (m, m) in self.R else False, self.M))

    def is_symetric(self):
        return 0 == len(filter(lambda t : True if (t[1], t[0]) not in self.R else False, self.R))

    def is_transitive(self):
        for t1 in self.R:
            for t2 in self.R:
                if t1[1] == t2[0]:
                    if (t1[0], t2[1]) not in self.R:
                        return False
        return True
