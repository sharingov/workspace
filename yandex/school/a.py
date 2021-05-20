class Robot:

    def __init__(self, t):
        self.x, self.y = t
        self.history = [(self.x, self.y)]

    def move(self, s):
        self.history.clear()
        self.history.append((self.x, self.y))
        for i in list(s):
            if i == 'N':
                self.y += 1
            elif i == 'S':
                self.y -= 1
            elif i == 'E':
                self.x += 1
            elif i == 'W':
                self.x -= 1
            self.history.append((self.x, self.y))
        return((self.x, self.y))

    def path(self):
        return(self.history)
