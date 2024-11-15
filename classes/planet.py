class Planet:
    def __init__(self, name, market_prices):
        self.name = name
        self.market_prices = market_prices
        
 class Planet:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose
        self.market = {'iron': 50, 'gold': 100, 'fuel': 20}  # Sample market items and prices

    def display(self):
        print(f"Planet: {self.name}")
        print(f"Purpose: {self.purpose}")
        if self.purpose == "trading":
            print("Items available in market:")
            for item, price in self.market.items():
                print(f"{item.capitalize()}: {price} credits")
        elif self.purpose == "fighting":
            print("Hostile environment! Be prepared for combat.")
        elif self.purpose == "repair":
            print("Repair and upgrade facilities available.")

    def buy(self, item):
        if self.purpose == "trading" and item in self.market:
            print(f"Bought {item} for {self.market[item]} credits.")
        else:
            print(f"{item} is not available for purchase here.")

    def sell(self, item, price):
        if self.purpose == "trading":
            self.market[item] = price
            print(f"Sold {item} for {price} credits.")
        else:
            print(f"{item} cannot be sold here.")


# Creating different planets
trade_planet = Planet("Mercury", "trading")
fight_planet = Planet("Mars", "fighting")
repair_planet = Planet("Venus", "repair")

# Display information for each planet
trade_planet.display()
fight_planet.display()
repair_planet.display()

# Example of buying and selling on a trading planet
trade_planet.buy("iron")
trade_planet.sell("platinum", 150)

    
    # Information about the market. We could display the name of the market, and the items and their price
