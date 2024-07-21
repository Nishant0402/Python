import http.client

conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "53414ae2c0mshbe86007245869e6p19bbe8jsn9a3fd9dd3217",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
}

conn.request("GET", "/current.json?q=53.1%2C-0.13", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))