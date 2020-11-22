# import re
import sys
import time
from itertools import tee
import re
import ply.lex as lex
from utils import htmlIndexFormatter, readTestFolder, readFile, Test, getNivel, htmlFormatter, auxOrg

tests = []
tests_aux = []
total = 0
total_notok = 0

# region RegEx

tokens = ("OK", "NOTOK", "SUBOK", "SUBNOTOK", "TAB", "COMMENT", "COUNTER")


def t_COUNTER(t):
    r"\d.+.\n"
    pass


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
    pass


def t_error(t):
    print("Unknown token: [%s]" % t.value)
    exit(1)


# endregion

lexer = lex.lex()
testFileNames = readTestFolder(sys.argv[1])

# Cria um ficheiro HTML para cada Teste
for i in testFileNames:
    lexer.input(readFile(i))

    for token in iter(lexer.token, None):
        taux = None
        if token.type == "SUBOK":
            ws = getNivel(token.value)
            saux = token.value.strip()
            captures = re.fullmatch(r"(\s{4})+ok\s(\d+)(.*)\n", token.value)
            taux = Test(captures.group(2), True, captures.group(3), ws)
        if token.type == "SUBNOTOK":
            ws = getNivel(token.value)
            saux = token.value.strip()
            captures = re.fullmatch(r"(\s{4})+not\sok\s(\d+)(.*)\n", token.value)
            taux = Test(captures.group(2), False, captures.group(3), ws)
        if token.type == "OK":
            captures = re.fullmatch(r"ok\s(\d+)(.*)\n", token.value)
            taux = Test(captures.group(1), True, captures.group(2), 1)
            total += 1
        if token.type == "NOTOK":
            captures = re.fullmatch(r"not\sok\s(\d+)(.*)\n", token.value)
            taux = Test(captures.group(1), False, captures.group(2), 1)
            total += 1
            total_notok += 1
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
    htmlFormatter(tests, i, sys.argv[1], total, total_notok)
    tests = []
    tests_aux = []
    total = 0
    total_notok = 0

# Cria uma pagina HTML para poder aceder aos testes
htmlIndexFormatter()
