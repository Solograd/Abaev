def main():
        rate = int(input("Процентная ставка: "))
        money = int(input("Введите сумму: "))
        period = int(input("Период: "))
        valuta = int(input("Укажите код валюты(Рубли - 0, Доллары - 1, Евро - 2 )"))
        if valuta == 1:
            price = 57
            print("Курс доллара: ", price)
            total = money * price
            print("Итог: ", total)
        elif valuta == 2:
            price = 60
            print("Курс евро: ", price)
            total = money * price
            print("Итог: ", total)
        else:
            print("Далее")
            total = money
        mrate = (rate / 1200)
        plata = round(total/12 + total*mrate, 2)
        pere = (plata * period - total)
        itog = round(plata * period, 2)
        print(" Ежемесячная оплата: ", round(plata, 2), " rub в течение", period, " месяцев")
        print("Переплата ", round(pere, 2), " rub.^^")
        print("Сумма, которую вы заплатите ", itog)
main()
