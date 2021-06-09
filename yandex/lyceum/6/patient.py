class Doctor:
    def __init__(self, name, n, m):
        self.name = name
        self.n = n
        self.m = m
        self.phrases = [
            "The puppet is dead.",
            "However, if he wasn't completely dead, "
            "it would be a sure sign that he was still alive.",
            "The puppet is still alive.",
            "However, if he were not alive, "
            "it would be a sure sign that he was actually dead.",
        ]
        self.count = 3

    def __str__(self):
        return f"Doctor {self.name} - {self.n}"

    def difference(self):
        return self.n - self.m

    def say_clever_phrases(self):
        self.count = (self.count + 1) % 4
        return self.phrases[self.count]

    def treat_patients(self, name):
        if len(name) % 2 == self.n % 2:
            self.n += 1
            return True
        else:
            self.m += 1
            return False

    def __eq__(self, other):
        return (self.n, self.m, self.name) == (other.n, other.m, other.name)

    def __lt__(self, other):
        return (self.n, -self.m, self.name) < (other.n, -other.m, other.name)

    def __le__(self, other):
        return self == other or self < other
