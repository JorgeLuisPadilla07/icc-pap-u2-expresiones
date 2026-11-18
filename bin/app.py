
import re

def main():
    runEjemplo1()
    runEjemplo2()
    runEjemplo3()


def runEjemplo1():
    patter = "ab*"
    palabras = ["a", "ab", "abbb", "abab", "b", ""]

    for p in palabras:
        print(f"{p}->{bool(re.fullmatch(patter, p))}")


def runEjemplo2():
    regex = r"[TO][0-9]{3}"
    lista = ["T001", "0120", "T01", "X001", "T0001"]

    for codigo in lista:
        print(f"{codigo} => {bool(re.fullmatch(regex, codigo))}")


def runEjemplo3():
    texto = "Sensores: T001 reporta 23.5 C; O001 reporta 12 PERSONAS; T002 reporta -2 C."
    patron = r"[TO][0-9]{3}"

    coincidencias = re.finditer(patron, texto)

    for matcher in coincidencias:
        print(f"Encontrado: {matcher.group()}, posicion: {matcher.start()}")


if __name__ == "__main__":
    main()
