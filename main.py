import unittest
import random

class CodeCoverageSimulator:
    def __init__(self):
        self.code_coverage = {}

    def add_code(self, code_name, code_lines):
        self.code_coverage[code_name] = code_lines

    def simulate_execution(self, code_name, executed_lines):
        if code_name in self.code_coverage:
            self.code_coverage[code_name] = [line for line in self.code_coverage[code_name] if line not in executed_lines]
            return len(self.code_coverage[code_name])
        else:
            return 0

class TestCodeCoverageSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = CodeCoverageSimulator()

    def test_add_code(self):
        self.simulator.add_code("code1", [1, 2, 3, 4, 5])
        self.assertEqual(self.simulator.code_coverage, {"code1": [1, 2, 3, 4, 5]})

    def test_simulate_execution(self):
        self.simulator.add_code("code1", [1, 2, 3, 4, 5])
        self.assertEqual(self.simulator.simulate_execution("code1", [1, 2, 3]), 2)
        self.assertEqual(self.simulator.simulate_execution("code1", [1, 2, 3, 4, 5]), 0)

    def test_simulate_execution_multiple_codes(self):
        self.simulator.add_code("code1", [1, 2, 3, 4, 5])
        self.simulator.add_code("code2", [6, 7, 8, 9, 10])
        self.assertEqual(self.simulator.simulate_execution("code1", [1, 2, 3]), 2)
        self.assertEqual(self.simulator.simulate_execution("code2", [6, 7, 8]), 3)

if __name__ == "__main__":
    unittest.main()
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Kodni yuklab oling va Python ni o'rnatgan kompyuterda ishlab chiq.
2. Kodni yuklab oling va ishlab chiq qilish uchun quyidagilarni amalga oshiring:
   - `python -m unittest test_code_coverage_simulator.py` (testlar uchun)
   - `python code_coverage_simulator.py` (simulyator uchun)

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `CodeCoverageSimulator` klassi yaratib, `add_code` metodidan foydalanib, kodni qo'shing.
2. `simulate_execution` metodidan foydalanib, kodni bajarishni simulyatsiya qiling.
3. Simulyatsiya qilingan kodning qancha qismi bajarilganligini tekshiring.
