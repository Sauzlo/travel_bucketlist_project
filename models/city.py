class City:
    def __init__(self, name, country, rating = None, visited = False, id = None):
        self.name = name
        self.country= country
        self.rating = rating
        self.visited = visited
        self.id = id

    
    def mark_as_visited(self):
        self.visited = True

    def change_name(self, name):
        self.name = name