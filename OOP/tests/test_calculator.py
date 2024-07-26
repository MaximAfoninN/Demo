import pytest
from Calculator import Calculator
from contextlib import nullcontext as does_not_raise

@pytest.fixture
def initial_variables(first_input = 0, second_input = 0, sum = 0):
    return first_input, second_input, sum

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print("Создание базы данных: ")
    pass


@pytest.mark.usefixtures("setup_db")
@pytest.mark.usefixtures("initial_variables")
class TestCalculator:
    @pytest.mark.parametrize(
        "first_input, second_input, sum, expectation",
        [
            (2, 4, 6, does_not_raise()),
            (3, 3, 6, does_not_raise()),
            (3, "3", 6, pytest.raises(TypeError)),
        ]
    )


    def test_calculator(self, first_input, second_input, sum, expectation):
        with expectation:
            assert Calculator.sum(first_input, second_input) == sum




