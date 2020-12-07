#coding=utf-8

import os
import sys
import time

def decom():
        time.sleep(1)
        print ("")
        file = open(raw_input(" File > ")).read()
        print ("")
        while True:
                if "exec" in file and "marshal" in file and "import" in file:
                        out = file.replace("exec", "x = ")
                        time.sleep(0.7)
                else:
                        print ("/n")
                        try:
                                os.remove("sc.py")
                                print ("Berhasil")
                                raw_input("Back > ")
                                decom()
                        except:
                                print ("Gagal")
                                raw_input("Back > ")
                                decom()
                        break
                sc = """from sys import stdout
import marshal
from uncompyle6.main import decompile
"""+out+"""
decompile(2.7,x, stdout) """
                open("sc.py","w").write(sc)
                os.system("python2 sc.py > decompile.py")
                file = open("decompile.py").read()

decom()