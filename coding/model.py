from dataclasses import dataclass

@dataclass
class OrderLine:
    orderid: orderid
    sku: sku
    qty: qty

class Batch:
    def __init__(self, ref, sku, eta, quantity):
        self.ref = ref
        self.sku = sku
        self.eta = eta
        self.quantity = quantity
        self._allocation = set()

    def 
    