from os import environ,path,popen
from sys import argv,exit,stderr

#file-path of dumpbin binary, here assuming that the Visual C++ for Python 2.7 package is installed
#Visual Studio installations or platform SDKs will also work
dumpbin = path.join(environ['LOCALAPPDATA'],'Programs/Common/Microsoft/Visual C++ for Python/9.0/VC/Bin/dumpbin.exe')
#if not installed for single user, but globally, dumpbin could be in Program Files
#dumpbin = path.join(environ['COMMONPROGRAMFILES(X86)'],'Microsoft/Visual C++ for Python/9.0/VC/Bin/dumpbin.exe')
#or
#dumpbin = path.join(environ['COMMONPROGRAMFILES'],'Microsoft/Visual C++ for Python/9.0/VC/Bin/dumpbin.exe')
#or if vcvars[.bat] has been loaded and dumpbin.exe is in %PATH%,
#dumpbin = 'dumpbin.exe'

#explain usage
if len(argv)!=3:
    stderr.write('Usage: '+argv[0]+' destination.def source.dll\n')
    exit(1)

#check that output file is .def to avoid accidentally overwriting .dll files
if argv[1][-4:]!='.def':
    stderr.write('Error: first argument destination.def must have suffix .def\n')
    exit(2)

#call dumpbin.exe to list dll exports
p = popen('"'+dumpbin+'" -exports '+argv[2])
#create output .def file
x = p.readline()
if x=='':
    stderr.write('No output from dumpbin, is the dumpbin variable in\n'+argv[0]+' correctly set up?\n')
    exit(3)
d = open(argv[1], 'w')
d.write('EXPORTS\n')
#skim through output until exports output begins
while x.replace(' ','').replace('\t','').strip()!='ordinalhintRVAname' and x!='':
    x = p.readline()
if x=='':
    d.close()
    p.close()
    exit(0)
x = p.readline()
while len(x.strip())==0:
    x = p.readline()
    if x=='':
        d.close()
        p.close()
        exit(0)
while len(x.strip())!=0:
    #discard aliases
    y = x.split('(')[0].split('=')[0].split()
    #extract ordinal and call name
    ordinal = y[0]
    name = y[-1]
    #write to def file
    d.write('    '+name+' @'+ordinal+'\n')
    x = p.readline()
d.close()
p.close()
