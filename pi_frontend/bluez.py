import bluetooth
import time


def getBlue():
    checklst = {'Stu1': False, 'Stu2': False, 'Stu3': False, 'Stu4': False, 'Stu5': False, 'Stu6': False,
         'Stu7': False, 'Stu8': False, 'Stu9': False, 'Stu10': False}
    print("checking "+ time.strftime("%a %d %b %Y %H:%m:%S",time.gmtime()))
    result1 = bluetooth.lookup_name("3C:A6:F6:32:DA:36", timeout = 3)
    result2 = bluetooth.lookup_name("34:42:62:55:59:9A", timeout = 3)
    result3 = bluetooth.lookup_name("4C:F2:02:EC:DF:49", timeout = 3)
    result4 = bluetooth.lookup_name("B8:3B:CC:03:18:AE", timeout = 3)
    if (result1 != None):  
        print("Pauvrete's mac in")
        checklst['Stu1'] = True
    if (result2 != None):  
        print("Pauvrete's ipad in")
        checklst['Stu2'] = True
    if (result3 != None):  
        print("Pauvrete's xiaomi in")
        checklst['Stu3'] = True
    if (result4 != None):  
        print("Pauvrete's redmi in")
        checklst['Stu4'] = True
    print(checklst)
    return checklst