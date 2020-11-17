# import re
import time
from itertools import tee

import ply.lex as lex
from utils import readFile, Test, getNivel

tests = []
tests_aux = []


def auxOrg(test, listX):
    level = test.nivel
    if listX == None:
        listX.append(test)
    else:
        nivel = listX[-1].nivel
        if nivel < level:
            listX.append(test)
        elif nivel == level:
            if nivel == 1:
                aux = listX[-1]
                listX.clear()
                listX.append(test)
                return aux
            else:
                listX[-2].subtests.append(listX[-1])
                aux = listX[-1]
                del listX[-1]
                listX.append(test)
                return aux
        else:
            while nivel != level:
                listX[-2].subtests.append(listX[-1])
                del listX[-1]
                nivel = listX[-1].nivel
            if nivel == 1:
                aux = listX[-1]
                listX.clear()
                listX.append(test)
                return aux
            else:
                listX[-2].subtests.append(listX[-1])
                aux = listX[-1]
                del listX[-1]
                listX.append(test)
                return aux


tokens = ("OK", "NOTOK", "SUBOK", "SUBNOTOK", "TAB", "COMMENT", "COUNTER")


def t_COUNTER(t):
    r"\d.+.\n"
    return t


def t_OK(t):
    r"ok.+\n"
    return t


def t_SUBOK(t):
    r"(\s{4})+ok.+\n"
    return t


def t_NOTOK(t):
    r"not\sok.+\n"
    return t


def t_SUBNOTOK(t):
    r"(\s{4})+not\sok.+\n"
    return t


def t_TAB(t):
    r"\ {4}"
    pass


def t_COMMENT(t):
    r"\n|[ \t].*\n|.+\n"
    return t


def t_error(t):
    print("Unknown token: [%s]" % t.value)
    exit(1)


lexer = lex.lex()
lexer.input(readFile("test/teste6.t"))

for token in iter(lexer.token, None):
    taux = None
    if token.type == "SUBOK":
        ws = getNivel(token.value)
        saux = token.value.strip()
        taux = Test(saux[3], True, saux[6:], ws)
    if token.type == "SUBNOTOK":
        ws = getNivel(token.value)
        saux = token.value.strip()
        taux = Test(saux[7], False, saux[11:], ws)
    if token.type == "OK":
        taux = Test(int(token.value[3]), True, token.value[6:], 1)
    if token.type == "NOTOK":
        taux = Test(int(token.value[7]), False, token.value[11:], 1)
    if taux:
        nivel = taux.nivel
        if tests_aux:
            if nivel == 1:
                a = auxOrg(taux, tests_aux)
                if a:
                    tests.append(a)
            else:
                auxOrg(taux, tests_aux)
        else:
            tests_aux.append(taux)

while tests_aux[-1].nivel != 1:
    tests_aux[-2].subtests.append(tests_aux[-1])
    del tests_aux[-1]

tests.append(tests_aux[0])


# for test_ in tests:
#     test_.printTests()

for test_ in tests:
    print(test_.printHTML())
