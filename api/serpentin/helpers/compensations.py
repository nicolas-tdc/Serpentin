class CompensationHelpers:

    @staticmethod
    def calculate_simple_compensation(count, total):
        bonus = 0.1 * total if count < 4 else 0.2 * total
        return bonus if bonus > 500 else 500

    @staticmethod
    def calculate_complex_compensation(count, total):
        return 0
