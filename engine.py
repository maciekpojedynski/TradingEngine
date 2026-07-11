import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class TradingEngine:
    def __init__(self, price: list[int]):
        self.prices = price

    def max_revenue_v1(self) -> int:
        "Brutal-Force version. O(n^2) time, O(1) memory"
        max_revenue = 0
        for x in range(0, len(self.prices)):
            for y in range(x + 1, len(self.prices)):
                revenue = self.prices[y] - self.prices[x]
                if max_revenue < revenue:
                    max_revenue = revenue
        return max_revenue

    def max_revenue_v2(self) -> int:
        "Sliding window: O(n) time, O(1) memory"

        logging.info("TradingEngine waking up...")
        if not self.prices or len(self.prices) < 2:
            logging.error("The list has too few elements and cannot be processed")
            return 0
        else:
            max_revenue = float('-inf')
            min_price = float('inf')

            for index in range(0, len(self.prices)):
                revenue = self.prices[index] - min_price
                if revenue > max_revenue:
                    max_revenue = revenue
                if self.prices[index] < min_price:
                    min_price = self.prices[index]

            logging.info(f"Return from investment is equal to {max_revenue}")
            return max_revenue


if __name__ == '__main__':
    test_v1 = [100, 90, 80, 70, 50]
    engine = TradingEngine(test_v1)
    result_1 = engine.max_revenue_v1()
    result_2 = engine.max_revenue_v2()
    print(f"result_v1: {result_1}")
    print(f"result_v2: {result_2}")



