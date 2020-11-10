# As nossas funções uteis

def readFile(filename):
    fh = open(filename, mode="r")
    contents = fh.read()
    fh.close()
    return contents


class Test:
    def __init__(self, id, ok, desc):
        self.id = id
        self.ok = ok
        self.desc = desc
        self.subtests=[]

def printTests(t):
    print("Id:%s" % t.id)
    if t.ok == True:
        print("Resultado:%s" % "PASSOU")
    else:
        print("Resultado:%s" % "NÃO PASSOU")
    print("Description:%s" % t.desc)

