# from tkinter import *
import asyncio
import httpx
import tkinter as tk
import tkinter.messagebox 

class NewConverter():
    
    def __init__(self, m, currency_from_et, currency_to_et, amount_et) -> None:
        self._m = m
        self._currency_from_et = currency_from_et
        self._currency_to_et = currency_to_et
        self._amount_et = amount_et
        
    @staticmethod
    def response_func(currency_from):
        # flake8: noqa
        response = httpx.get(
            f"https://v6.exchangerate-api.com/v6/d57b4c08bb9102c88023d3f0/latest/{currency_from}")
        r = response.json()
        return r
            
    def clear(self): 
        self._currency_from_et.delete(0, tk.END)
        self._currency_to_et.delete(0, tk.END)
        self._amount_et.delete(0, tk.END)
        
    def convert(self):

        # flake8: noqa
        if (self._currency_from_et.get() == "" or self._currency_to_et.get() == "" or 
                self._currency_from_et.get() == "" and self._currency_to_et.get() == ""):
            tkinter.messagebox.showinfo("Error !!",
                "Currency Not Selected.\n Please enter FROM and TO Currency!")
        
        # flake8: noqa
        elif (len(self._currency_from_et.get()) != 3 or len(self._currency_to_et.get()) != 3 or
        self._currency_from_et.get().isupper() is False or self._currency_to_et.get().isupper() is False):
            tkinter.messagebox.showinfo("Error !!",
                "No such currency.\n Please enter FROM and TO Currency!")
        
        r = NewConverter.response_func(self._currency_from_et.get())
        
        # flake8: noqa
        if (self._currency_from_et.get() not in r['conversion_rates'].keys() or 
            self._currency_to_et.get() not in r['conversion_rates'].keys()):
            tkinter.messagebox.showinfo("Error !!",
                "No such currency.\n Please enter FROM and TO Currency!")

        elif (self._amount_et.get() == ""):
            tkinter.messagebox.showinfo("Error !!", 
                "Amount Not Entered.\n Please enter valid amount!")
            
        amount = float(self._amount_et.get())
        rate = "{}".format(r['conversion_rates'][self._currency_to_et.get()])
        result = float("{:.4f}".format(amount *float(rate)))

        res = tk.Label(self._m, text =result,font='Helvetica 10 bold')
        res.grid(row=8, column=1)
    
async def main():
    m = tk.Tk()
    m.title('Currency Converter')
    m.geometry("350x200")
    m.eval('tk::PlaceWindow . center')

    tk.Label(m, text='From Currency :').grid(row=0)
    tk.Label(m, text=' To Currency :').grid(row=1)
    tk.Label(m, text='   Amount :').grid(row=2)
    tk.Label(m, text='Result :').grid(row=8)
    
    currency_from_et = tk.Entry(m)
    currency_to_et = tk.Entry(m)
    amount_et = tk.Entry(m)

    currency_from_et.grid(row=0, column=1)
    currency_to_et.grid(row=1, column=1)
    amount_et.grid(row=2, column=1)   
    
    rate = NewConverter(m, currency_from_et, currency_to_et, amount_et)
    
    button = tk.Button(m, text='Convert', command=rate.convert)
    button.grid(row=3, column=1)

    button2 = tk.Button(m, text='Clear', command=rate.clear)
    button2.grid(row=4, column=1)

    m.mainloop()
    
if __name__ == "__main__":
    asyncio.run(main())
