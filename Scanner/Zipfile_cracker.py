import zipfile
import optparse
from threading import Thread
def extractFile(zFile, password):
  try:
      zFile.extractall(pwd=password)
      print '[+] Found password ' + password + '\n'
  except:
      pass
  def main():
      parser = optparse.OptionParser("usuage%prog " +\ "-f <zipfile> -d <dictionary>")
      parser
