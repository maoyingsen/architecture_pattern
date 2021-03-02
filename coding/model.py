from dataclasses import dataclass
from typing import List, Optional

def allocate(line: OrderLine, batches: List[Batch]) -> str:
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
    def __init__(self, ref: str, sku: str, qty: int, eta, Optional[Date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_num >= line.qty
    
    def allocate(self, line):
        if self.can_allocate(line):
            self._allocation.add(line)
    
    def dellocate(self, line):
        if line in self._allocations:
            self._allocation.remove(line)

    @property
    def available_num(self):
        num = 0
        for l in self._allocation:
            num += l.qty
        return self.quantity - num