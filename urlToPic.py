import win32com.client as win32
import time, os
from config import vba_code
# import win32api
# import win32con


def urlToPic(filename):
    print(f'Generating new xlsm file~')
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(os.path.abspath('data/'+filename+'.xlsx'))
    excel.DisplayAlerts = False
    wb.DoNotPromptForConvert = True
    wb.CheckCompatibility = False
    wb.SaveAs(os.path.abspath(r"data/"+filename+"pic.xlsm"), FileFormat=52)
    excel.Application.Quit()
    del excel
    excel = None
    print('wait for 10 sec!')
    time.sleep(10)
    print('Start opening file and adding macro!\nIt might take more time! plz wait until finish!')
    excel2 = win32.gencache.EnsureDispatch('Excel.Application')
    excel2.Visible = False
    # key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"SOFTWARE\\Microsoft\\Office\\16.0\\Excel\\Security", 0, win32con.KEY_ALL_ACCESS)
    # store original value
    # val, _ = win32api.RegQueryValueEx(key,'AccessVBOM') 
    # win32api.RegSetValueEx(key, "AccessVBOM", 0, win32con.REG_DWORD, 1)
    wb = excel2.Workbooks.Open(os.path.abspath(r'data/'+filename+'pic.xlsm'))
    origin_val = excel2.Application.AutomationSecurity
    excel2.Application.AutomationSecurity = 3
    mod = wb.VBProject.VBComponents.Add(1)
    mod.CodeModule.AddFromString(vba_code)
    # wb.VBProject.VBComponents.Import(os.path.abspath("vbaProject.bin"))
    print(f'start running macro!')
    excel2.Application.Run("Module1.URLPictureInsert")
    excel2.DisplayAlerts = False
    wb.DoNotPromptForConvert = True
    wb.CheckCompatibility = False
    excel2.Application.AutomationSecurity = origin_val
    wb.SaveAs(os.path.abspath(r"data/"+filename+"pic.xlsx"), FileFormat=51, ConflictResolution=2) # Macro disapears here
    print(f'Finished!!!')
    # win32api.RegCloseKey(key)
    excel2.Workbooks(1).Close(SaveChanges=1)
    excel2.Application.Quit()
    del excel2
    excel2 = None
    print(f'start removing xlsm file\n')
    os.remove(r'data/'+filename+'pic.xlsm')
    # return val
# urlToPic('astro.jiang20220815-2220fwi')