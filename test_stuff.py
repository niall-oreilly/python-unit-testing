import unittest


class TestThatStuffWorks(unittest.TestCase):
    def test_this_string_is_on(self):
        self.assertEqual(1, 1)


class TestVendingMachine(unittest.TestCase):
    denominations = [5, 10, 20, 50, 100, 200]
    denominations.sort(reverse=True)

    def give_change(self, amount, change):
        if amount < 5:
            return change
        else:
            for denom in self.denominations:
                if amount >= denom:
                    change.append(denom)
                    amount -= denom
                    return self.give_change(amount, change)



    def test_no_change(self):
        coins = self.give_change(0, [])
        self.assertEqual(coins, [])


    def test_return_some_change(self):
        coins = self.give_change(12, [])
        self.assertEqual(coins, [10])

