# Security CI/CD Assignment
# Simple order calculator for automated testing

def calculate_total(price, quantity):
    """Calculate the total cost of an order."""
    return price * quantity


def apply_discount(total, discount):
    """Apply a discount to the total."""
    return total - (total * discount)


if __name__ == "__main__":
    total = calculate_total(25, 3)
    discounted_total = apply_discount(total, 0.10)

    print("Original total:", total)
    print("Total after discount:", discounted_total)