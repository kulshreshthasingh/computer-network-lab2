import requests

def http_requests():
    try:
        get_url = "https://postman-echo.com/get?message=hello"
        r1 = requests.get(get_url)
        print("GET Status:", r1.status_code)
        print("Headers:", r1.headers)
        print("Body:", r1.text[:200])

        post_url = "https://postman-echo.com/post"
        r2 = requests.post(post_url, data={"msg": "hello"})
        print("POST Status:", r2.status_code)
        print("Headers:", r2.headers)
        print("Body:", r2.text[:200])
    except Exception as e:
        print("Error:", e)

http_requests()
