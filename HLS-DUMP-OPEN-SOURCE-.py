
#!/usr/bin/env python3
import requests, json, os, re, time
from requests.exceptions import ConnectionError

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""" 
$$$$$$$\  $$\   $$\ $$\      $$\ $$$$$$$\  
$$  $$\ $$ |  $$ |$$$\    $$$ |$$  $$\ 
$$ |  $$ |$$ |  $$ |$$$$\  $$$$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |$$$$$$$  |
$$ |  $$ |$$ |  $$ |$$ \$$$  $$ |$$  ____/ 
$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |      
$$$$$$$  |\$$$$$$  |$$ | \_/ $$ |$$ |      
\_/  \__/ \|     \|\|  """) # CODE BY HLS
    try:
        if os.path.exists('Data') == False:
            os.mkdir('Data')
        cookies, token_eaag, token_eaab = json.loads(open('Data/Akun.json', 'r').read())['Cookie'], json.loads(open('Data/Akun.json', 'r').read())['EAAG'], json.loads(open('Data/Akun.json', 'r').read())['EAAB']
        name = requests.get('https://graph.facebook.com/v16.0/me/?fields=name&access_token={}'.format(token_eaag), cookies = {'cookie': cookies}).json()['name']
    except (KeyError, IOError):
        cookies = input("\n[*] Cookies : ")
        with requests.Session() as r:
            r.headers.update({
                'cookie': cookies,
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            })
            response = r.get('https://business.facebook.com/business_locations').text
            token_eaag = re.search('(EAAG\w+)', str(response)).group(1)
            with requests.Session() as r:
                r.headers.update({
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                })
                response2 = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', cookies = {'cookie': cookies})
                response3 = r.get('https://web.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(re.findall('act=(.*?)&nav_source', response2.text)[0]), cookies = {'cookie': cookies})
                token_eaab = re.search('(EAAB\w+)', response3.text).group(1)
            open('Data/Akun.json', 'w').write(json.dumps({
                'EAAB': token_eaab,
                'EAAG': token_eaag,
                'Cookie': cookies
            }));time.sleep(2.5);continue
    print(f"""
[+] Welcome : {name}

[1] Dump From Public Id
[2] Dump From Follower Id
[3] Remove Cookies
    """)
    choose = input("[?] Choose : ")
    if choose == '1' or choose == '01':
        users = input("[?] User : ")
        file = input("[?] Save File : ")
        for uid in users.split(','):
            try:
                if uid.isnumeric() == True:
                    for z in json.loads(requests.get('https://graph.facebook.com/v1.0/{}/?fields=friends.fields(id,name).limit(5000)&access_token={}'.format(uid, token_eaab), cookies = {'cookie': cookies}).text)['friends']['data']:
                        id, name = z['id'], z['name']
                        open(file, 'a+').write(f'{id}|{name}\n')
                        print(f"[*] Dump {id}/{str(len(open(file, 'r').readlines()))}          ", end='\r')
                else:
                    continue
            except (KeyError, ConnectionError):
                continue
            except (KeyboardInterrupt):
                break
        print(f"[*] Jumlah User : {str(len(open(file, 'r').readlines()))}") # ADD NEW LINE AFTER PRINT STATEMENT
        break
    elif choose == '2' or choose == '02':
        users = input("[?] User : ")
        file = input("[?] Save File : ")
        if os.path.exists(file):
            open(file, 'w').close()
        for uid in users.split(','):
            try:

if uid.isnumeric() == True:
                    for z in json.loads(requests.get('https://graph.facebook.com/v1.0/{}/?fields=username,followers.limit(5000)&access_token={}'.format(uid, token_eaab), cookies = {'cookie': cookies}).text)['followers']['data']:
                        username = z['username']
                        if ' ' in username:
                            username = f'"{username}"'
                        open(file, 'a+').write(f'{username}\n')
                        print(f"[*] Dump {username}/{str(len(open(file, 'r').readlines()))}          ", end='\r')
                else:
                    continue
            except (KeyError, ConnectionError):
                continue
            except (KeyboardInterrupt):
                break
        print(f"[*] Jumlah User : {str(len(open(file, 'r').readlines()))}") # ADD NEW LINE AFTER PRINT STATEMENT
        break
    elif choose == '3' or choose == '03':
        if os.path.exists('Data') == True:
            os.system('rm -rf Data')
            print("[+] Cookies Removed")
            time.sleep(2.5)
        else:
            print("[!] Cookies Not Found")
            time.sleep(2.5)
            continue
    else:
        print("[!] Invalid Menu")
        time.sleep(2.5)
        continue
