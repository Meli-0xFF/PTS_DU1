from pyrsistent import pset, PClass, field, PSet

class Relation(PClass):

    M = field(type=PSet, mandatory=True)
    R = field(type=PSet, initial=pset())

    def __iter__(self):
        return self.R.__iter__()

    def __next__(self):
        return self.R.__next__()

    def contains(self, x, y):
        return (x,y) in self.R

    def add(self, x, y):
        return Relation(M=self.M, R=self.R | pset([(x,y)]))

    def remove(self, x, y):
        return Relation(M=self.M, R=self.R - pset([(x,y)]))

    def union(self, R2):
        return Relation(M=self.M, R=self.R | R2.R)

    def intersection(self, R2):
        return Relation (M=self.M, R=self.R & R2.R)

    def subtraction(self, R2):
        return Relation(M=self.M, R=self.R - R2.R)

    def inverse(self):
        return Relation(M=self.M, R=pset(map(lambda t : t[::-1], self.R)))
 
    def composition(self, R2):
        return Relation(M=self.M, R=pset((t1[0], t2[1]) for t1 in self.R for t2 in R2.R if t1[1] == t2[0]))

    def is_reflexive(self):
        return pset() == pset(filter(lambda m : True if not self.contains(m, m) else False, self.M))

    def is_symetric(self):
        return pset() == pset(filter(lambda t : True if not self.contains(t[1], t[0]) else False, self.R))

    def is_transitive(self):
        return pset() == pset((t1, t2) for t1 in self.R for t2 in self.R if t1[1] == t2[0] and not self.contains(t1[0], t2[1]))

    def reflexive_transitive_closure(self):
        closure = self.R | (pset(map(lambda m : (m, m), self.M)))
        while True:
            closure_until_now = closure | pset((x,w) for x,y in closure for q,w in closure if q == y)
            if closure_until_now == closure: break
            closure = closure_until_now
        return Relation(M=self.M, R=closure_until_now)

def get_relation_class(M):
    return Relation(M=M)
