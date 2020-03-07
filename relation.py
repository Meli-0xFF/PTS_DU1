class Relation:
    M = set()
    R = set()

    def contains(self, *elements):
        return tuple(elements) in self.R

    def add(self, *elements):
        self.R.add(tuple(elements))

    def remove(self, *elements):
        self.R.remove(tuple(elements))
