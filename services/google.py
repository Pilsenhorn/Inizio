import requests

def get_google_results(query: str):
    response = requests.get(
        "https://serpapi.com/search.json",
        params={
            "q": query,
            "google_domain": "google.com",
            "api_key": "eaf522bbf3651d1acdc134300f8e6a36c16f9f091babbf72b0eabf05596da8cc"
        }
    )
    data = response.json()
    print(data)
    results = data.get("organic_results", [])
    clean_results = []
    for item in results[:10]: 
        clean_results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        })
    return clean_results



