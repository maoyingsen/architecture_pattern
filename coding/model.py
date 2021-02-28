from dataclasses import dataclass


def allocate(batch, l):
    """
    for line in l:
        if batch.can_allocate(line):
            batch._allocation.add(line)
    """
    if batch.can_allocate(l) is True:
        batch.allocate(l)

@dataclass(frozen = True)
class OrderLine:
    orderid: int
    sku: str
    qty: int

class Batch:
    def __init__(self, ref, sku, eta, quantity):
        self.ref = ref
        self.sku = sku
        self.eta = eta
        self.quantity = quantity
        self._allocation = set()

    def can_allocate(self, line):
        if line.qty > self.quantity:
            return False
        if line.sku != self.sku:
            return False
        return True
    
    def allocate(self, line):
        self._allocation.add(line)
    
    def dellocate(self, line):
        self._allocation.remove(line)

    @property
    def available_num(self):
        num = 0
        for l in self._allocation:
            num += l.qty
        return self.quantity - num