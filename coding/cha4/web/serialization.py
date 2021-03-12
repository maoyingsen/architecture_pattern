import requests

resp = requests.get("https://blog.csdn.net/xiaohuo0930/article/details/90373181")

print(resp.ok)           # => True
print(resp.status_code)  # => 200
print(resp.headers['content-type'])   # => "text/html"
print(resp.headers) 