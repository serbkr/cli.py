class task:
    def __init__(self, description, completed=False):
        self.description= description
        self.completed= completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def __str__(self):
        return f"[{'✓' if self.completed else '✗'}] {self.description}"

    def to_dict(self):
        return {
            'description' : self.description,
            'completed' : self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(description=data['description'], completed=data['completed'])
