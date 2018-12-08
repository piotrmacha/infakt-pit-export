import urllib.request
import json

print('')
print("{:^80}".format("inFakt: eksporter danych do PIT"))
print('')
apiKey = input("API Key: ")
year = input("Rok: ")
print('')
print('-' * 80)
print('')

def money(raw):
    return "%s zł" % '{:17.2f}'.format(raw / 100.00).replace('.', ',')

books = json.loads(urllib.request.urlopen("https://api.infakt.pl/v3/books.json?api_key=" + apiKey).read())
taxes = json.loads(urllib.request.urlopen("https://api.infakt.pl/v3/income_taxes.json?api_key=" + apiKey).read())
zus = json.loads(urllib.request.urlopen("https://api.infakt.pl/v3/insurance_fees.json?api_key=" + apiKey).read())

income_sum = 0
expenses_sum = 0
profit_sum = 0

print("KPIR %s%s%s%s" % ('{:>15}'.format('Okres'), '{:>20}'.format('Przychód'), '{:>20}'.format('Koszty'), '{:>20}'.format('Dochód')))
print('-' * 80)
for book in books['entities']:
    if (year in book['period_name']):
        income_sum += book['income_price']
        expenses_sum += book['expenses_price']
        profit_sum += book['profit_price']
        period_name = "{:>20}".format(book['period_name'])
        income_price = "{:>20}".format(money(book['income_price']))
        expenses_price = "{:>20}".format(money(book['expenses_price']))
        profit_price = "{:>20}".format(money(book['profit_price']))
        print("%s%s%s%s" % (period_name, income_price, expenses_price, profit_price))

print('-' * 80)
period_name = "{:>20}".format('SUMA')
income_price = "{:>20}".format(money(income_sum))
expenses_price = "{:>20}".format(money(expenses_sum))
profit_price = "{:>20}".format(money(profit_sum))
print("%s%s%s%s" % (period_name, income_price, expenses_price, profit_price))
print('')

tax_sum = 0
print("Zaliczki %s%s" % ('{:>11}'.format('Okres'), '{:>60}'.format('Zaliczka')))
print('-' * 80)
for tax in taxes['entities']:
    if (year in tax['period_name']):
        tax_sum += tax['to_pay_price']
        period_name = "{:>20}".format(tax['period_name'])
        to_pay = "{:>60}".format(money(tax['to_pay_price']))
        print("%s%s" % (period_name, to_pay))
print('-' * 80)
period_name = "{:>20}".format('SUMA')
to_pay_price = "{:>60}".format(money(tax_sum))
print("%s%s" % (period_name, to_pay_price))
print('')

social_sum = 0
health_sum = 0
work_sum = 0
print("ZUS %s%s%s%s" % ('{:>16}'.format('Okres'), '{:>20}'.format('Społeczne'), '{:>20}'.format('Zdrowotne'), '{:>20}'.format('FP')))
print('-' * 80)
for m in zus['entities']:
    if (year in m['period_name']):
        social_sum += m['social_amount_paid']
        health_sum += m['health_amount_paid']
        work_sum += m['work_amount_paid']
        period_name = "{:>20}".format(m['period_name'])
        social_amount_paid = "{:>20}".format(money(m['social_amount_paid']))
        health_amount_paid = "{:>20}".format(money(m['health_amount_paid']))
        work_amount_paid = "{:>20}".format(money(m['work_amount_paid']))
        print("%s%s%s%s" % (period_name, social_amount_paid, health_amount_paid, work_amount_paid))
print('-' * 80)
period_name = "{:>20}".format('SUMA')
social_amount_paid = "{:>20}".format(money(social_sum))
health_amount_paid = "{:>20}".format(money(health_sum))
work_amount_paid = "{:>20}".format(money(work_sum))
print("%s%s%s%s" % (period_name, social_amount_paid, health_amount_paid, work_amount_paid))
print('')