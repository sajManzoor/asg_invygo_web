class BrandName:
    def __init__(self, key, label, count):
        self.key = key
        self.label = label
        self.count = count

    def __str__(self):
        return f"Key: {self.key}, Label: {self.label}, Count: {self.count}"
