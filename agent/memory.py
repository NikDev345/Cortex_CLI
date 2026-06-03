from collections import deque


class Memory:
    def __init__(self, max_interactions=5):
        self.history = deque(maxlen=max_interactions * 2)

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

    def get_history(self):
        return list(self.history)

    def clear(self):
        self.history.clear()