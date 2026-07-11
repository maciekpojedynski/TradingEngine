from engine import TradingEngine

def test_stagnation():
    price_stagnation = [50, 50, 50, 50]
    engine = TradingEngine(price_stagnation)

    assert engine.max_revenue_v2() == 0

def test_bessa():
    price_bessa = [100, 90, 80, 70, 50]
    engine = TradingEngine(price_bessa)

    assert engine.max_revenue_v2() == -10

def test_emptiness():
    price_empty = []
    engine = TradingEngine(price_empty)

    assert engine.max_revenue_v2() == 0