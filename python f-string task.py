def order_summary(name, items):
    print(f"Order Summary for {name}")
    print("---------------------------")

    grand_total = 0
    for item, qty, price in items:
        line_total = qty * price
        grand_total += line_total
        print(f"{item} - Qty: {qty}, Price: {price}, Total: {line_total}")

    print("---------------------------")
    print(f"Grand Total: {grand_total}")
items = [("Apple", 3, 0.5), ("Banana", 2, 0.3)]
order_summary("Ahmad", items)

