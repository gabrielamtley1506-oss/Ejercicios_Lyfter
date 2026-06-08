from Tarea_Func_5 import count_case
import pytest

def test_count_case_with_long_paragraph(capsys):
    #Arrange
    text_input = "La programación es una de las habilidades más poderosas que una persona puede desarrollar en el siglo veintiuno. " \
    " Con solo una computadora y acceso a internet, es posible construir herramientas que impacten la vida de miles de personas en el mundo entero." \
    " Aprender a programar no es sencillo, pero cada línea de código representa un pequeño paso hacia el dominio de un lenguaje que hablan las máquinas." \
    " Python es elegante y legible, permite enfocarse en resolver problemas reales sin perderse en sintaxis complicadas. " \
    " Desde aplicaciones web hasta inteligencia artificial, Python está presente en casi todos los campos de tecnología." \
    " Quienes eligen este camino descubren que programar no es solo profesión, sino una forma de pensar." \
    " Aprendes a dividir problemas en partes pequeñas, encontrar patrones donde otros ven caos, y construir soluciones con lógica." \
    " El camino puede ser difícil, pero cada error es una lección. Con práctica y determinación, cualquier persona puede convertirse en desarrollador."
    #Act
    count_case(text_input)
    #Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == 'The number of uppercase letters is 10 and the number of lower cases is 819'



def test_count_case_with_short_paragraph(capsys):
    #Arrange
    text_input = "La"
    #Act
    count_case(text_input)
    #Assert
    captured = capsys.readouterr()
    assert captured.out.strip() =='The number of uppercase letters is 1 and the number of lower cases is 1' 


def test_count_case_with_numbers_and_letters_paragraph(capsys):
    #Arrangem
    text_input = "152369874563214548965368njhmk43848396843438398435463857498743jmfyhj84854638574385436jk,mfhj,h543685436854368AEEHYGGGGGGERG546843648554364"
    #Act
    count_case(text_input)
    #Assert
    captured = capsys.readouterr()
    assert captured.out.strip() =='The number of uppercase letters is 14 and the number of lower cases is 18' 