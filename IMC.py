import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num = float(altura.get())
        num2 =float(peso.get())

        result =float(num2 / (num*num))
        
        if result <= 16.99:
            muito_baixo = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está muito abaixo do peso')
            muito_baixo.pack(padx=10, pady=10)

        if result >=17 and result <= 18.49:
            baixo = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está abaixo do peso')
            baixo.pack(padx=10, pady=10)

        if result >=18.5 and result <= 24.99:
            ideal = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está no peso ideal')
            ideal.pack(padx=10, pady=10)

        if result >=25 and result <= 29.99:
            ideal = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está acima do peso')
            ideal.pack(padx=10, pady=10)

        if result >=30 and result <= 34.99:
            ideal = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está com obesidade grau 1')
            ideal.pack(padx=10, pady=10)

        if result >=35 and result <= 39.99:
            ideal = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está com obesidade grau 2')
            ideal.pack(padx=10, pady=10)

        if result >=40:
            ideal = tk.Label(janela, text=f'{nome.get()}, O seu IMC é de {result} e você está com obesidade grau 3')
            ideal.pack(padx=10, pady=10)
    
    except ZeroDivisionError:
        messagebox.showerror('Aviso', 'Impossivel dividir por zero')

    except ValueError: messagebox.showinfo('aviso', 'Preencher Campos em branco')
        



janela = tk.Tk()

lb1 = tk.Label(janela, text='Cálculo de IMC')
lb1.pack(padx=10, pady=0)

tr = tk.Label(janela, text='---------------------------------')
tr.pack()

nome_label = tk.Label(janela, text='Qual seu nome?')
nome_label.pack()

nome = tk.Entry(janela)
nome.pack(padx=10, pady=10)
nome.configure(width=20)

lb2 = tk.Label(janela, text='Insira sua altura em Metros ex:(0.00):')
lb2.pack()

altura = tk.Entry(janela)
altura.pack(padx=10, pady=10)
altura.configure(width=20)

lb3 = tk.Label(janela, text='Insira seu peso em Kg:')
lb3.pack()

peso = tk.Entry(janela, text='Insira seu peso em Kg:')
peso.pack(padx=10, pady=10)
peso.configure(width=20)


botao = tk.Button(janela, text='Calcular', command=calcular)
botao.pack(padx=10, pady=10)

janela.geometry('500x300')
janela.title('Calculo de IMC')
janela.mainloop()