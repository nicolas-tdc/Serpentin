class CompensationHelpers():
    def __init__(self, count, closed_count, total, target=0):
        self.count = count
        self.closed_count = closed_count
        self.total = total
        self.target = target

    def calculate_simple_compensation(self):
        bonus = 0.1 * self.total if self.closed_count < 4 else 0.2 * self.total
        return bonus if bonus > 500 else 500

    def calculate_complex_compensation(self):
        bonus = 0
        target_achievement = self.total / self.target
        if 0 <= target_achievement <= 0.5:
            bonus = 0
        elif 0.5 <= target_achievement <= 1:
            bonus = self.total * 8 / 100
        elif 1 <= target_achievement <= 1.5:
            bonus = self.total * 12 / 100
        elif target_achievement > 1.5:
            bonus = self.total * 16 / 100

        return bonus + 500 if self.count > 7 else bonus
