import requests as req
import tkinter as tk
from bs4 import BeautifulSoup

# Setting the window
window = tk.Tk()
window.title("Currency Viewer")
window.geometry("500x220")
window.resizable(0, 0)

# Link to prices
CHF = "https://cinkciarz.pl/wymiana-walut/kursy-walut/chf/pln"
USD = "https://cinkciarz.pl/wymiana-walut/kursy-walut/usd/pln"
EURO = "https://cinkciarz.pl/wymiana-walut/kursy-walut/eur/pln"
GBP = "https://cinkciarz.pl/wymiana-walut/kursy-walut/gbp/pln"

# Creating requests for prices
chf_page = req.get(CHF)
usd_page = req.get(USD)
euro_page = req.get(EURO)
gbp_page = req.get(GBP)

chf = BeautifulSoup(chf_page.content, 'html.parser')
usd = BeautifulSoup(usd_page.content, 'html.parser')
eur = BeautifulSoup(euro_page.content, 'html.parser')
gbp = BeautifulSoup(gbp_page.content, 'html.parser')

chf_buy_course = chf.find('td', {'data-buy': 'true'})
chf_sell_course = chf.find('td', {'data-sell': 'true'})

try:
    span_chf_buy_element = chf_buy_course.find_all('span').pop(1)
    span_chf_sell_element = chf_sell_course.find_all('span').pop(1)
    chf_buy_course_label_str = "Buy: " + str(span_chf_buy_element).replace("<span>", "").replace("</span>", "") + " PLN"
    chf_sell_course_label_str = "Sell: " + str(span_chf_sell_element).replace("<span>", "").replace("</span>", "") + " PLN"
except Exception as e:
    chf_buy_course_label_str = "Can't read a price!"
    chf_sell_course_label_str = "Can't read a price!"

chf_label = tk.Label(window, text="CHF: ", font='Sans 16 bold', pady=5, padx=5)
chf_buy_label = tk.Label(window, text=chf_buy_course_label_str, font='Sans 12')
chf_sell_label = tk.Label(window, text=chf_sell_course_label_str, font='Sans 12')
chf_label.grid(row=0, column=0)
chf_buy_label.grid(row=1, column=1)
chf_sell_label.grid(row=2, column=1)

usd_buy_course = usd.find('td', {'data-buy': 'true'})
usd_sell_course = usd.find('td', {'data-sell': 'true'})

try:
    span_usd_buy_element = usd_buy_course.find_all('span').pop(1)
    span_usd_sell_element = usd_sell_course.find_all('span').pop(1)
    usd_buy_course_label_str = "Buy: " + str(span_usd_buy_element).replace("<span>", "").replace("</span>", "") + " PLN"
    usd_sell_course_label_str = "Sell: " + str(span_usd_sell_element).replace("<span>", "").replace("</span>", "") + " PLN"
except Exception as e:
    usd_buy_course_label_str = "Can't read a price!"
    usd_sell_course_label_str = "Can't read a price!"

usd_label = tk.Label(window, text="USD:", font='Sans 16 bold', pady=5, padx=5)
usd_buy_label = tk.Label(window, text=usd_buy_course_label_str, font='Sans 12')
usd_sell_label = tk.Label(window, text=usd_sell_course_label_str, font='Sans 12')
usd_label.grid(row=3, column=0)
usd_buy_label.grid(row=4, column=1)
usd_sell_label.grid(row=5, column=1)

euro_buy_course = eur.find('td', {'data-buy': 'true'})
euro_sell_course = eur.find('td', {'data-sell': 'true'})

try:
    span_euro_buy_element = euro_buy_course.find_all('span').pop(1)
    span_euro_sell_element = euro_sell_course.find_all('span').pop(1)
    euro_buy_course_label_str = "Buy: " + str(span_euro_buy_element).replace("<span>", "").replace("</span>", "") + " PLN"
    euro_sell_course_label_str = "Sell: " + str(span_euro_sell_element).replace("<span>", "").replace("</span>", "") + " PLN"
except Exception as e:
    euro_buy_course_label_str = "Can't read a price!"
    euro_sell_course_label_str = "Can't read a price!"

euro_label = tk.Label(window, text="EUR: ", font='Sans 16 bold', pady=5, padx=10)
euro_buy_label = tk.Label(window, text=euro_buy_course_label_str, font='Sans 12')
euro_sell_label = tk.Label(window, text=euro_sell_course_label_str, font='Sans 12')
euro_label.grid(row=0, column=5)
euro_buy_label.grid(row=1, column=6)
euro_sell_label.grid(row=2, column=6)

gbp_buy_course = gbp.find('td', {'data-buy': 'true'})
gbp_sell_course = gbp.find('td', {'data-sell': 'true'})

try:
    span_gbp_buy_element = gbp_buy_course.find_all('span').pop(1)
    span_gbp_sell_element = gbp_sell_course.find_all('span').pop(1)
    gbp_buy_course_label_str = "Buy: " + str(span_gbp_buy_element).replace("<span>", "").replace("</span>", "") + " PLN"
    gbp_sell_course_label_str = "Sell: " + str(span_gbp_sell_element).replace("<span>", "").replace("</span>",
                                                                                                    "") + " PLN"
except Exception as e:
    gbp_buy_course_label_str = "Can't read a price!"
    gbp_sell_course_label_str = "Can't read a price!"

gbp_label = tk.Label(window, text="GBP: ", font='Sans 16 bold', pady=5, padx=10)
gbp_buy_label = tk.Label(window, text=gbp_buy_course_label_str, font='Sans 12')
gbp_sell_label = tk.Label(window, text=gbp_sell_course_label_str, font='Sans 12')
gbp_label.grid(row=3, column=5)
gbp_buy_label.grid(row=4, column=6)
gbp_sell_label.grid(row=5, column=6)

exit_button = tk.Button(window, text="Exit", font='Sans 12', padx=15, pady=5, command=window.destroy)
exit_button.grid(row=6, column=4)

if __name__ == "__main__":
    window.mainloop()
