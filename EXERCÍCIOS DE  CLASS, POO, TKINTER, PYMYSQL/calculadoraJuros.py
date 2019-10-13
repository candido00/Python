import tkinter

janela = tkinter.Tk()
janela.geometry("250x300")


titulo = tkinter.Label(janela,text="Calculadora do Prejuízo")
titulo.grid(row=0, column=0, columnspan=4)

#----------- Linha da Taxa---------------

taxaLabel = tkinter.Label(janela,text="Taxa:")
taxaLabel.grid(column=0, row=1, sticky="w", columnspan=2)

taxaEntry = tkinter.Entry(janela)
taxaEntry.grid(column=2, row=1, columnspan=2)


#----------- Linha do valor solicitado ---------------

valorLabel = tkinter.Label(janela,text="Valor solicitado:")
valorLabel.grid(column=0, row=2, sticky="w", columnspan=2)

valorEntry = tkinter.Entry(janela)
valorEntry.grid(column=2, row=2, columnspan=2)

#----------- Linha do valor solicitado ---------------

parcelasLabel = tkinter.Label(janela,text="Qtd parcelas:")
parcelasLabel.grid(column=0, row=3, sticky="w", columnspan=2)

parcelasEntry = tkinter.Entry(janela)
parcelasEntry.grid(column=2, row=3, columnspan=2)

#----------- Função de cálculo ---------------
def calc():
    parcelas = (float(valorEntry.get())/int(parcelasEntry.get()))#parcela sem juros
    vParcela = parcelas*float(taxaEntry.get())/100+parcelas#valor com juros
    vTotal = vParcela*int(parcelasEntry.get())#valor total a ser pago
    labResParcelas.config(text = ("Valor da parcela = %.2f"%vParcela))
    labResTotal.config(text = ("Valor Total = %.2f"%vTotal))
    pass

#----------- Linha do Botao ---------------
bt = tkinter.Button(janela,text="calcular",command=calc, width="16")
bt.grid(row=4,column=2,columnspan=2)

#----------- Linha do resultado parcelas ---------------
labResParcelas = tkinter.Label(janela,text = "Valor da parcela = ")
labResParcelas.grid(row=5, column=0, columnspan=4, sticky="w")

#----------- Linha do resultado total ---------------
labResTotal = tkinter.Label(janela,text = "Valor Total = ")
labResTotal.grid(row=6, column=0, columnspan=4, sticky="w")


janela.mainloop()
