try:
 import random
 import time
 import os
 from creditcard import CreditCard
except:
 import os
 os.system('pip3 install creditcard')
 os.system('pip3 install setuptools')
os.system('echo "Card Checking By DoraBoot" > card.txt')
def banner():
 print("""
 ___  ___ __ _ _ __         ___ ___
/ __|/ __/ _` | '_ \ _____ / __/ __|
\__ \ (_| (_| | | | |_____| (_| (__
|___/\___\__,_|_| |_|      \___\___|
                 ©DoraSec Hackers
 Auto Scanning Credit Card Number
""")

def generator():
 banner()
 print("Examp : 402357")
 print("")
 bin = int(input("Enter BIN/IIN : "))
 n_gen = int(input("Enter Number Found (Default : 5): "))
 print("[+] Set BIN -->", bin)
 time.sleep(1)
 a = int(f"{bin}0000000000")
 b = int(f"{bin}9999999999")
 print("[+] Starting Scanner...")
 time.sleep(5)
 num_found = 0
 while True:
  random_id = random.randint(a, b)
  m = random.randint(1, 12)
  y = random.randint(2025, 2032)
  if m < 10:
   m = str(f"0{m}")
   y = str(y)
  else:
   m = str(m)
   y = str(y)
  cvv = random.randint(1, 999)
  check = CreditCard(random_id, m, y, cvv)
  if check.is_valid:
   num_found += 1
   if num_found == n_gen:
    print("[+] Scanner Done")
    exit()
   else:
    print(f"""
+-----------------------------------------------------+
| numerical order : {num_found}
| BIN/IIN Code : {bin}
| Number Card : {random_id}
| Expiration Date : {m}/{y}
| Card Security Code : {cvv}
| Brand : {check.brand}
| PIPE Text : {random_id}|{m}/{y}|{cvv}
+-----------------------------------------------------+
""")
  else:
   pass
generator()
