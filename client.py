import requests

url = "http://server-service.default.svc.cluster.local:8000/"

response = requests.get(url)
print(response.text)
