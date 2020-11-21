# As nossas funções uteis
import os
import glob

def readTestFolder():
    testFiles = []
    for i in glob.glob(r'test\\*.t'):
        testFiles.append(i)

    return testFiles

def readFile(filename):
    fh = open(filename, mode="r")
    contents = fh.read()
    fh.close()
    return contents

def getNivel(string):
    ws = len(string) - len(string.lstrip())
    ws=ws/4
    ws+=1
    return int(ws)


class Test:
    def __init__(self, id, ok, desc,nivel):
        self.id = id
        self.ok = ok
        self.desc = desc
        self.nivel=nivel
        self.subtests=[]

    def getPrint(self):
        if self.ok:
            return "ok %s %s" % (self.id, self.desc)
        else:
            return "not ok %s %s" % (self.id, self.desc)

    def printTests(self):
        tabs=""
        for x in range(self.nivel-1):
            tabs += "\t"
        print("%s%s"% (tabs,self.getPrint()))
        if self.subtests:
            self.printSTests()

    def printHTML(self):
        html=""
        if self.nivel==1:
            if len(self.subtests)>0:
                if self.ok==True:
                    html = '''<div class="test_header_ok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-success"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
                else:
                    html = '''<div class="test_header_notok">
                                                <h2>''' + self.getPrint() + '''</h2>
                                                <button data-toggle=collapse data-target="#teste''' + str(self.id) + '''" type="button" class="btn btn-danger"
                                                    style="transform:translateY(-20%); ">
                                                Ver subtestes
                                                </button>
                                            </div>'''

                    html += '''<div id="teste''' + str(self.id) + '''" class="collapse">'''
                    for sub in self.subtests:
                        html += sub.printHTML()

                    html += '''</div>'''
            else:
                if self.ok==True:
                    html='''<div>
                                <div class="test_header_ok">
                                    <h2> '''+ self.getPrint() +'''</h2>
                                </div>
                            </div>'''
                else:
                    html = '''<div>
                                <div class="test_header_notok">
                                    <h2> ''' + self.getPrint() + '''</h2>
                                </div>
                            </div>'''
        else:
            if len(self.subtests) > 0:
                if self.ok== True:
                    margin= (self.nivel-1)*40
                    html+='''<div class="subtest" style="margin-left: '''+str(margin)+'''px">
                                <div class="card w-50">
                                    <div class="subtest_content_ok">
                                        '''+self.getPrint()+'''
                                    </div>
                                </div>
                            </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                    for sub in self.subtests:
                        html+=sub.printHTML()
            else:
                if self.ok== True:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_ok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''
                else:
                    margin = (self.nivel - 1) * 40
                    html += '''<div class="subtest" style="margin-left: ''' + str(margin) + '''px">
                                    <div class="card w-50">
                                        <div class="subtest_content_notok">
                                            ''' + self.getPrint() + '''
                                        </div>
                                    </div>
                                </div>'''

        return html

    def printSTests(self):
        for test_ in self.subtests:
            test_.printTests()



def htmlFormatter(tests, filename):
    filename = filename.replace("test\\", "html\\")
    filename = filename.replace(".t", "")

    Html_file = open(filename + ".html", "w")
    pagina = ""

    Html_file.write('''<!DOCTYPE html>
<html>
<title>Test Anything Protocol</title>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <style>
        h2 {
            display: inline;
        }

        .test_header_ok {
            padding: 10px;
            color: rgb(29, 173, 29);
        }

        .test_header_notok {
            padding: 10px;
            color: rgb(219, 63, 63);
        }

        .subtest {
            padding-top: 2px;
            padding-bottom: 2px;
        }

        .subtest_content_ok {
            padding-top: 2px;
            padding-bottom: 2px;
            padding-left: 5px;
            color: white;
            background-color: rgb(41, 165, 30);
        }

        .subtest_content_notok {
            padding-top: 2px;
            padding-bottom: 2px;
            padding-left: 5px;
            color: white;
            background-color: rgb(219, 63, 63)
        }

        p {
            margin-left: 10px;
        }

        body {
            font-family: "Lato", sans-serif;
        }

        .sidenav {
            height: 100%;
            width: 225px;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: rgb(49, 49, 49);
            overflow-x: hidden;
            padding-top: 10px;
        }

        .sidenav a {
            padding: 0px 6px 25px 12px;
            text-decoration: none;
            font-size: 20px;
            color: #818181;
            display: block;
        }

        .sidenav a:hover {
            color: #f1f1f1;
        }

        .main {
            margin-left: 240px; /* Same as the width of the sidenav */
        }

        @media screen and (max-height: 450px) {
            .sidenav {
                padding-top: 15px;
            }

            .sidenav a {
                font-size: 18px;
            }
        }
    </style>

</head>

<body>

<div class="sidenav">
    <a href="https://testanything.org"><h1 style="size:20px">Test Anything Protocol</h1></a>
    <a href="htmlhome.html">HOME</a>
    <div>
    <table class="table table-hover table-secondary">
      <tbody>
        <tr>
          <th scope="row">Number of Tests:</th>
          <td>4</td>
        </tr>
        <tr>
          <th scope="row">Successful Tests:</th>
          <td>3</td>
        </tr>
        <tr>
          <th scope="row">Unsuccessful Tests:</th>
          <td>1</td>
        </tr>
        <tr>
          <th scope="row">Percentage of Success:</th>
          <td>75%</td>
        </tr>
      </tbody>
    </table>
    </div>
</div>

<div class="main">\n''')

    for test_ in tests:
        pagina += test_.printHTML()
        pagina += "<hr>"

    Html_file.write(pagina)
    Html_file.write('''</div>
</div>


</body>
</html>''')


    Html_file.close

def readHtmlFolder():
    htmlFiles = []
    for i in glob.glob(r'html\\*.html'):
        if i != "html\\htmlhome.html":
            htmlFiles.append(i)

    return htmlFiles


def htmlHomeFormatter():
    htmlHomeFile = open("html\\htmlhome.html", "w")
    htmlFiles = readHtmlFolder()

    htmlHomeFile.write('''<!DOCTYPE html>
<html>
<title>Test Anything Protocol</title>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <style>


        body {
            font-family: "Lato", sans-serif;
        }

        .sidenav {
            height: 100%;
            width: 225px;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: rgb(49, 49, 49);
            overflow-x: hidden;
            padding-top: 10px;
        }

        .sidenav a {
            padding: 0px 6px 25px 12px;
            text-decoration: none;
            font-size: 20px;
            color: #818181;
            display: block;
        }

        .sidenav a:hover {
            color: #f1f1f1;
        }

        .main {
            margin-left: 240px; /* Same as the width of the sidenav */
        }

        @media screen and (max-height: 450px) {
            .sidenav {
                padding-top: 15px;
            }

            .sidenav a {
                font-size: 18px;
            }
        }
    </style>

</head>

<body>

<div class="sidenav">
    <a href="https://testanything.org"><h1 style="size:20px">Test Anything Protocol</h1></a>
    <a href=".">HOME</a>
</div>

<div class="main">

<div class="container">
  <h1>Ficheiros de Teste</h1>
</div>
''')

    for i in htmlFiles:
        testName = i.replace("html\\", "")

        htmlHomeFile.write('''<nav class="navbar navbar-expand-sm bg-secondary navbar-dark">
  <ul class="navbar-nav">
    <li class="nav-item active">
      <a class="nav-link" href="''' + testName + '''" style="font-size:20px">''' + testName + '''</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="''' + testName + '''">Visualizar</a>
    </li>
  </ul>
</nav>''')

    htmlHomeFile.write('''</div>

</body>
</html>''')
    htmlHomeFile.close()
