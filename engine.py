class TradingEngine:
    def __init__(self, price: list[int]):
        self.prices = price

    def max_revenue_v1(self) -> int:
        max_revenue = 0

        #slow pointer
        for x in range(0, len(self.prices)):
            #fast pointer
            for y in range(x+1, len(self.prices)):
                 revenue = self.prices[y] - self.prices[x]
                 if max_revenue < revenue:
                    max_revenue = revenue
                 else:
                    pass
        
        return max_revenue

if __name__ == '__main__':
    test_v1 = [105, 102, 103, 101, 104, 110, 100, 108]
    engine = TradingEngine(test_v1)
    result = engine.max_revenue_v1()
    print(result)



