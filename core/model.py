import time
import os
import sys
import shutil
import itertools

# defining the functions
def rc(rf):
 alphabet="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+-"
 start=time.time()
 tryn=0
 for a in range(1,len(alphabet)+1):
  for b in itertools.product(alphabet,repeat=a):
   k="".join(b)
   if rf[-4:]==".rar":
    print("Trying:",k)
    kf=os.popen("unrar t -y -p%s %s 2>&1|grep 'All OK'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="All OK\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   elif rf[-4:]==".zip" or rf[-3:]==".7z":
    print("Trying:",k)
    kf=os.popen("7za t -p%s %s 2>&1|grep 'Everything is Ok'"%(k,rf))
    tryn+=1
    for rkf in kf.readlines():
     if rkf=="Everything is Ok\n":
      print("Found password:",repr(k))
      print("Tried combination count:",tryn)
      print("It took",round(time.time()-start,3),"seconds")
      print("Exiting...")
      time.sleep(2)
      sys.exit(1)
   else:
    print("We Are Cracking (rar , zip , 7z) only , Do Not Be Idiot\nExiting...")

# Check That The File Already Exists . Then Run The File
if len(sys.argv)==2:
 if os.path.exists(sys.argv[1]):
  rc(sys.argv[1])
 else:
  print("Check The File Again! , The File Not Exist.\nExiting...")
else:
 pass
