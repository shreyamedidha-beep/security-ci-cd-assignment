# Unit tests for the security CI/CD assignment

from app import calculate_total, apply_discount


def test_calculate_total():
    assert calculate_total(25, 3) == 75


def test_apply_discount():
    assert apply_discount(100, 0.10) == 90


def test_calculate_total_zero_quantity():
    assert calculate_total(25, 0) == 0


def test_apply_discount_zero():
    assert apply_discount(100, 0) == 100