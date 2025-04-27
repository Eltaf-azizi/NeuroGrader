import requests


url = "https://www.googleapis.com/customsearch/v1"

params = {
    "key": "afhakjfiudfafdasfnvkh",
    "cx": "4353nvkdsg24bdaf",
    "q": "Model Context Protocol MCP"
}


response = requests.get(url, params=params)
print(response.json())