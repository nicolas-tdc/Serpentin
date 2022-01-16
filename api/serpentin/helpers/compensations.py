class CompensationHelpers:

    @staticmethod
    def calculate_simple_compensation(count, total):
        bonus = 0.1 * total if count < 4 else 0.2 * total
        return bonus if bonus > 500 else 500

    @staticmethod
    def calculate_complex_compensation(count, total, target):
        bonus = 0
        target_achievement = total / target
        if 0 <= target_achievement <= 0.5:
            bonus = 0
        elif 0.5 <= target_achievement <= 1:
            bonus = total * 8 / 100
        elif 1 <= target_achievement <= 1.5:
            bonus = total * 12 / 100
        elif target_achievement > 1.5:
            bonus = total * 16 / 100

        return bonus + 500 if count > 7 else bonus
