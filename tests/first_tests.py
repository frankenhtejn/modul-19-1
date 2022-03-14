import pytest
from app.calc import calculator

class TestCalc:
    def setup(self):
        self.calc=calculator
    def test_multiply_calculate_correcty(self):
        assert self.calc.multiply(self , 3, 3) == 9
    def test_division_calculate_correcty(self):
        assert self.calc.division(self, 27, 3) == 9
    def test_substraction_calculate_correcty(self):
        assert self.calc.substraction(self, 45, 4) == 41
    def test_adding_calculate_correcty (self):
        assert self.calc.adding(self, 4, 9) == 13

