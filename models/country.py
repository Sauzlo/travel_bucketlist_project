class Country:
    def __init__(self, name, rating = None, visited = False, id = None):
        self.name = name
        self.rating = rating
        self.visited = visited
        self.id = id

    
    def mark_as_visited(self):
        self.visited = True