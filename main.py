#import re
import ply.lex as lex
from utils import readFile, Test, getNivel

tests = []

# t1 = Test(1, True, "test 1", 1)
# t2 = Test(2, True, "test sub1", 2)
# t3 = Test(3, True, "test sub sub1", 3)
# t4 = Test(4, True, "test 2", 1)
# t2.subtests.append(t3)
# t1.subtests.append(t2)
# tests.append(t1)
# tests.append(t4)
#
# for t in tests:
#     t.printTests()

tokens = ("OK", "NOTOK", "SUBOK", "SUBNOTOK", "TAB", "COMMENT", "COUNTER")

def t_COUNTER(t):
    r"\d.+.\n"
    return t

def t_OK(t):
    r"^ok.+\n"
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

pointer_record = []
lexer = lex.lex()
lexer.input(readFile("test/teste3.t"))

for token in iter(lexer.token, None):
    pass
    if token.type == "SUBOK":
        ws = getNivel(token.value)
        saux = token.value.strip()
        taux = Test(saux[3], True, saux[6:], ws)
    if token.type == "OK":
        taux = Test(int(token.value[3]), True, token.value[6:], 1)
    if token.type == "NOTOK":
        taux = Test(int(token.value[3]), False, token.value[6:], 1)

# for test_ in tests:
#     test_.printTests()
