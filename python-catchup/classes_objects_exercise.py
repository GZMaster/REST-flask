class Store:
  def __init__(self, name, items):
    self.name = name
    self.items = items
    
  def add_item(self, name, price):
    self.items.append({"name": name, "price": price})
    
    
  def stock_price(self):
    return sum([item["price"] for item in self.items])

store = Store("Rolf", [])

store.add_item("Laptop", 1000)
store.add_item("Phone", 500)

print(store.stock_price())