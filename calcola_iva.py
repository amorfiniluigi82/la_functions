# -*- coding: utf-8 -*-

from libs.la_functions import InputOutput, Finance


def main():
    prezzo = InputOutput().input_float('Prezzo : ', 'Inserire il prezzo')
    iva = InputOutput().input_int('Iva : ', "Inserire l'iva")
    r = Finance().calculate_tax(prezzo, iva)
    prezzo_con_iva = prezzo + round(r, 2)
    print("Prezzo : {}, Iva : {} , Prezzo con Iva {}".format(prezzo, iva, prezzo_con_iva))

if __name__ == '__main__':
    main()
