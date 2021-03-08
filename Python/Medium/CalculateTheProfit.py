
def profit(dictionary):
    cost_per_unit = dictionary["cost_price"]
    sell_per_unit = dictionary["sell_price"]
    units = dictionary["inventory"]
    total_cost = cost_per_unit * units
    total_value = sell_per_unit * units
    total_profit = total_value - total_cost

    print(int(total_profit))

profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
})

profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
})

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
})