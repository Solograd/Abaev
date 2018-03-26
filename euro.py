def procedure_perevod (currency, result):
    usd = 59
    euro = 70
    if currency == 1:
        result = round (result / usd, 2)
        return result
    if currency == 2:
        result = round (result / euro, 2)
        return result
if __name__ == '__main__':
    procedure_perevod()