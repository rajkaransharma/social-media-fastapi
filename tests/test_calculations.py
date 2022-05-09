# import pytest
# from app.calculations import *

# @pytest.fixture
# def zero_bank_account():
#     return BankAccount()

# @pytest.fixture
# def bank_account():
#     return BankAccount(50)

# @pytest.mark.parametrize("num1, num2, expected", [
#     (1, 2, 3),
#     (5, 4, 9),
#     (9, 11, 20)
# ])
# def test_add(num1, num2, expected):
#     print("testing add fuction")
#     assert add(num1, num2) == expected

# def test_subtract():
#     assert subtract(9, 4) == 5

# def test_multiply():
#     assert multiply(3, 4) == 12

# def test_divide():
#     assert divide(12, 4) == 3


# def test_bank_set_initial_amount(bank_account):
#     assert bank_account.balance == 50

# def test_bank_default_amount(zero_bank_account):
#     assert zero_bank_account.balance == 0

# def test_withdraw(bank_account):
#     bank_account.withdraw(15)
#     assert bank_account.balance == 35

# def test_deposit(zero_bank_account):
#     zero_bank_account.deposit(100)
#     assert zero_bank_account.balance == 100

# def test_collect_interest(bank_account):
#     bank_account.collect_interest()
#     assert round(bank_account.balance, 6) == 55


# @pytest.mark.parametrize("deposited, withdrew, expected", [
#     (400, 300, 100),
#     (500, 200, 300),
#     (100, 50, 50)
# ])
# def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
#     zero_bank_account.deposit(deposited)
#     zero_bank_account.withdraw(withdrew)
#     assert zero_bank_account.balance == expected

# def test_insufficient_funds(bank_account):
#     with pytest.raises(Exception):
#         bank_account.withdraw(300)
