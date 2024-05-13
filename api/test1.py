import requests


def status_code(url):
    res = requests.get(url)
    status = res.status_code
    length = len(res.content)
    result = (status, length)
    return result


# Usage example:
print(status_code("https://www.example.com"))
