import pytest
from model import Batch, OrderLine, allocate

@pytest.fixture
def batch_abc():
    return Batch(2345, "abc", "today", 20)

@pytest.fixture
def line_abc():
    return OrderLine(123, "abc", 10)

@pytest.fixture
def line_bcd():
    return OrderLine(123, "bcd", 10)

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

def test_allocate_with_same_sku(batch_abc, line_abc):
    allocate(batch_abc, line_abc)
    assert batch_abc.available_num == 10

def test_can_allocate_if_available_greater_than_required(batch_abc, line_abc):
    assert batch_abc.can_allocate(line_abc)

def test_cannot_allocate_if_skus_do_not_match(batch_abc, line_bcd):
    assert batch_abc.can_allocate(line_bcd) is False