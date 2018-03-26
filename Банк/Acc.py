def calculate_income(money, period, rate):
    if money <= 0:
        return 0
    result = round(money + (money*rate/1200*period), 2)
    return result
if __name__ == "__main__":
    calculate_income()