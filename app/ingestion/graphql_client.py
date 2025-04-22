import requests

def fetch_graphql_data():
    query = """
    {
        items {
            id
            value
            timestamp
        }
    }
    """
    try:
        res = requests.post("https://graphql.api/query", json={"query": query})
        res.raise_for_status()
        return res.json().get("data", {}).get("items", [])
    except Exception as e:
        logging.error(f"GraphQL fetch failed: {e}")
        return []
