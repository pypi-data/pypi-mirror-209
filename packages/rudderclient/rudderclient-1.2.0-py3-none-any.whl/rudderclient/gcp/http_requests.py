import http


def iap_http_request(method, api_url, request_url, body, headers):
    conn = http.client.HTTPSConnection(api_url)
    conn.request(method=method, url=request_url,
                 body=body, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return data.decode("utf-8")
