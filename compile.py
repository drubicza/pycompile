#!/usr/bin/env python
import py_compile, os, sys, platform
N = '\x1b[00m'
R = '\x1b[91m'
Y = '\x1b[93m'
B = '\x1b[94m'

def clear():
    if 'unix' or 'linux' or 'linux2' in sys.platform:
        os.system('clear')
    else:
        if 'win' in sys.platform:
            os.system('cls')
        else:
            os.system('clear')


def info():
    print '\n%s{==============================}\n[ %sCoder  %s: %sGunadiCBR           %s]\n[ %sGitHub %s: %sgithub.com/afelfgie %s]\n{==============================}%s\n' % (R, Y, B, N, R, Y, B, N, R, N)


try:
    try:
        clear()
        info()
        file = sys.argv[1]
        py_compile.compile(file)
        print ''
        print '%s[%s+%s] %sFile saved%s: %s%sc' % (R, Y, R, N, R, N, file)
        print ''
        sys.exit()
    except IndexError:
        print '%s[%s+%s] %sUsage %s: %spython2 %s [filename.py]' % (R, B, R, B, Y, N, sys.argv[0])
        print ''
        sys.exit()

except IOError as e:
    print '%s[%s!%s] %sERROR: %s%s' % (R, B, R, R, N, e)
    print ''
    sys.exit(1)
