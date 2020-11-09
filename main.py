
import re
import ply.lex as lex
from utils import readFile

tokens = ("OK", "NOTOK","SUBOK", "TAB","COMMENT", "COUNTER")


def t_COUNTER(t):
    r"\d.+.\n"
    return t

def t_OK(t):
    r"ok.+\n"
    return t


def t_SUBOK(t):
    r"[ok].+\n"
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
    print(token)
    if token.type == "COUNTER":
        print(str(token.value)[0])
        print(str(token.value)[3])
