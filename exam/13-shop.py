class Batch:

    def __init__(self, index):
        self.index = index
        self.deliveries = {}

    def total(self):
        return sum(self.deliveries.values())

    def __str__(self):
        header = "## Batch %d - %d items" % (self.index, self.total())
        addresses = ["- %s: %d" % (k, v) for k, v in self.deliveries.items()]
        return '\n'.join([header] + addresses)

class BatchList:

    def __init__(self, capacity=7):
        self.capacity = capacity
        self.batches = [Batch(1)]

    def add(self, address, amount):
        batch = self.batches[-1]
        if self.capacity - batch.total() >= amount:
            batch.deliveries[address] = amount
        else:
            fit = self.capacity - batch.total()
            batch.deliveries[address] = fit
            self.batches.append(Batch(batch.index + 1))
            self.add(address, amount - fit)
    
    def __str__(self):
        return "Toilerpaper delivery" + '\n\n' + '\n\n'.join([str(b) for b in self.batches])

def main():
    orders = [
        ("Address 1", 4),
        ("Address 2", 15),
        ("Address 3", 3),
        ("Address 4", 8)
    ]

    batches = BatchList(capacity=7)
    for order in orders:
        batches.add(order[0], order[1])
    print(batches)

if __name__ == "__main__":
    main()

    

    

