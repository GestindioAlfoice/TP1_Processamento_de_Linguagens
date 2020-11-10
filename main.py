import re
import ply.lex as lex
from utils import readFile, Test, printTests
tests = []
tokens = ("OK", "NOTOK", "SUBOK", "TAB", "COMMENT", "COUNTER")


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
    r"not\sok.+\n"
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
lexer.input(readFile("test/teste3.t"))

for token in iter(lexer.token, None):
    if token.type == "SUBOK":
        s=token.value
        ws=len(s) - len(s.lstrip())
        ws=ws/4
        ws+=1
        print("Nivel:%s" % ws)
    # print(token)
    # if token.type== "OK":
    #     tests.append(Test(int(token.value[3]),True,token.value[6:]))
    # if token.type== "NOTOK":
    #     tests.append(Test(int(token.value[3]),False,token.value[6:]))

# for test_ in tests:
#     printTests(test_);



