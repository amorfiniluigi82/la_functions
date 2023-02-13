# -*- coding: utf-8 -*-

from libs.la_functions import InputOutput, Web


def main():
    url = InputOutput().input_string("Url : ", 'Inserire l\'url')
    n = Web().download_file(url)
    print("{}".format(n))


if __name__ == '__main__':
    main()
