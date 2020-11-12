# import re
import time
from itertools import tee

import ply.lex as lex
from utils import readFile, Test, getNivel

tests = []
tests_aux = []


# t1 = Test(1, True, "test 1", 1)
# t2 = Test(2, True, "test sub1", 2)
# t3 = Test(3, True, "test sub sub1", 3)
#
# tests_aux.append(t1)
# tests_aux.append(t2)
# tests_aux.append(t3)


# t4 = Test(4, True, "test 2", 1)
# t2.subtests.append(t3)
# t1.subtests.append(t2)
# tests.append(t1)
# tests.append(t4)
#
# for t in tests:
#     t.printTests()

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
                listX[-1] = test
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
                del listX[-1]
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
    r"^not\sok.+\n"
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
lexer.input(readFile("test/testedummy.t"))

for token in iter(lexer.token, None):
    taux = None
    if token.type == "SUBOK":
        ws = getNivel(token.value)
        saux = token.value.strip()
        taux = Test(saux[3], True, saux[6:], ws)
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

for test_ in tests:
    test_.printTests()
