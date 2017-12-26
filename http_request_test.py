import urllib, http.client
from urllib.parse import unquote
#a = {0:["speed", "speed1234^**"], 1:["web","123455555!@#$"]};

for i in range(0,1):
    BODY = "***********HELLO***********";
    headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8","Accept":"text/plain"}
    conn = http.client.HTTPSConnection("[DOMAIN]", [PORT])
    conn.request("POST", "/", BODY, headers)
    response = conn.getresponse();
    print(i,": ", response.status, response.reason);
    print(response.info());
    #print(urllib.unquote(response.read(500).decode("utf-8", "ignore"))
    dataHeader = str(response.info())+"\r\n"
    dataBody = unquote(response.read().decode("utf-8", "ignore"));
    data = dataHeader+str(dataBody);

# source is file write for now;
f = open("./response.txt", "w")
f.write(str(data))

f.close();
