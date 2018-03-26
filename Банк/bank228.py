import Acc
import euro

rate = int(input("Введите процентную ставку: "))
money = int(input("Введите сумму: "))
period = int(input("Введите период ведения счета в месяцах: "))
result = Acc.calculate_income(money, rate, period)
print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)

currency = int(input("Укажите код валюты: доллары - 1, евро - 2"))
a = euro.procedure_perevod(currency, result)
print("Итого:", a)