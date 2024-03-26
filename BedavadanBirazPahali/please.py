import requests, time as t
cookies = {"PHPSESSID": "9m683ona3mq4k66q7qhhrl3m9o",}
counter = 81522
while True:
    counter+=1
    print(counter, end=": ")
    a = requests.get("https://ba9d8e09f7de04af.siberyildiz.com/?qq=81223:"+str(counter), cookies=cookies)
    print(a.text.split("\n")[0].replace("')</script><!DOCTYPE html>", "").replace("<script>alert('", ""))
    t.sleep(0.5)