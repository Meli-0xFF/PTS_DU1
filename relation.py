class Relation:
    def __init__(self, M, R=set()):
        self.R = R
        self.M = M

    def __iter__(self):
        return self.R.__iter__()

    def __next__(self):
        return self.R.__next__()

    def contains(self, x, y):
        return (x,y) in self.R

    def add(self, x, y):
        return Relation(self.M, R=self.R | {(x,y)})

    def remove(self, x, y):
        return Relation(self.M, R=self.R - {(x,y)})

    def union(self, R2):
        return Relation(self.M, R=self.R | R2.R)

    def intersection(self, R2):
        return Relation (self.M, R=self.R & R2.R)

    def subtraction(self, R2):
        return Relation(self.M, R=self.R - R2.R)

    def inverse(self):
        return Relation(self.M, R=set(map(lambda t : t[::-1], self.R)))
 
    def composition(self, R2):
        return Relation(self.M, R=set((t1[0], t2[1]) for t1 in self.R for t2 in R2.R if t1[1] == t2[0]))

    def is_reflexive(self):
        return set() == set(filter(lambda m : True if not self.contains(m, m) else False, self.M))

    def is_symetric(self):
        return set() == set(filter(lambda t : True if not self.contains(t[1], t[0]) else False, self.R))

    def is_transitive(self):
        for t1 in self.R:
            for t2 in self.R:
                if t1[1] == t2[0] and not self.contains(t1[0], t2[1]): return False
        return True

    def reflexive_transitive_closure(self):
        closure = self.R.union(set(map(lambda m : (m, m), self.M)))
        while True:
            closure_until_now = closure | set((x,w) for x,y in closure for q,w in closure if q == y)
            if closure_until_now == closure: break
            closure = closure_until_now
        return Relation(self.M, closure_until_now)
