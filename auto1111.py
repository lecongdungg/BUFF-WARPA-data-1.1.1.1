import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
os.system('cls' if os.name == 'nt' else 'clear')
print(
  '   \033[1;31m   _______ _      __________________       _______ _______ _______ _______\n'
  '     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
  '     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
  '     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
  '     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
  '     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
  '     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
  '     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n'
)

print("[+] \033[1;35m ABOUT SCRIPT:")

print(
  "[-] \033[1;36m With this script, you can getting unlimited GB on Warp+.")

print("[-] \033[1;37m Version: 4.0.0")

print(
  "------------------------------------------------------------------------")
print("[+] \033[1;37m THIS SCRIPT CODDED BY LÊ CÔNG DỤNG")

print("[-]\033[1;34m ZALO : 0819876977")

print("[-] \033[1;32m FACEBOOK:Lê Công Dụng")

print(
  "------------------------------------------------------------------------")

#thay ID vào đây

referrer = "1d4e85c0-e83a-497b-8c62-d0f11e45653c"


def genString(stringLength):
  try:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
  except Exception as error:
    print(error)


def digitString(stringLength):
  try:
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))
  except Exception as error:
    print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
  try:
    install_id = genString(22)
    body = {
      "key": "{}=".format(genString(43)),
      "install_id": install_id,
      "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
      "referrer": referrer,
      "warp_enabled": False,
      "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
      "type": "Android",
      "locale": "es_ES"
    }
    data = json.dumps(body).encode('utf8')
    headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Host': 'api.cloudflareclient.com',
      'Connection': 'Keep-Alive',
      'Accept-Encoding': 'gzip',
      'User-Agent': 'okhttp/3.12.1'
    }
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    status_code = response.getcode()
    return status_code
  except Exception as error:
    print(error)


g = 0
b = 0
while True:
  result = run()
  if result == 200:
    g = g + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")

    print(
      '   \033[1;31m   _______ _      __________________       _______ _______ _______ _______\n'
      '     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
      '     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
      '     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
      '     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
      '     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
      '     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
      '     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n'
    )

    print("  \033[1;32m                WARP-PLUS-CLOUDFLARE (script)" +
          " By Lê Công Dụng")
    print("")
    animation = [
      "[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%",
      "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%",
      "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%",
      "[■■■■■■■■■■] 100%"
    ]
    for i in range(len(animation)):
      time.sleep(0.5)
      sys.stdout.write("\r[+] Đang chuẩn bị ... ... " +
                       animation[i % len(animation)])
      sys.stdout.flush()
    print(f"\n[-] ĐANG LÀM VIỆC TRÊN  ID: {referrer}")
    print(f"[:)] {g} GB đã được thêm vào tài khoản của bạn thành công..")
    print(f"[#] Tổng số:  {g} TỐT {b} XẤU")
    print("[*] Sau 18 giây, một yêu cầu mới sẽ được gửi.")
    time.sleep(18)
  else:
    b = b + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("                  WARP-PLUS-CLOUDFLARE (script)" + " Lê Công Dụng")
    print("")
    print("[:(] Error when connecting to server.")
    print(f"[#] Total: {g} Good {b} Bad")

# key 1.1.1.1:
# 931U0hNE-gR52E4i1-9U86Dm5y