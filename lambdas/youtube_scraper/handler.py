import os
import requests
from dotenv import load_dotenv

# Load env from local .env file when running manually
if __name__ == "__main__":
    load_dotenv()

def handler(event, context):
    api_key = os.getenv("YOUTUBE_API_KEY")
    query = event.get("query", "브랜드필름")
    region_code = event.get("regionCode", "KR")

    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&type=video&maxResults=5&q={query}&regionCode={region_code}&key={api_key}"
    )

    response = requests.get(url)
    print("🔍 YouTube API Response:", response.status_code)
    print(response.json())

    return {
        "statusCode": response.status_code,
        "body": response.json()
    }

# For local test
if __name__ == "__main__":
    import os
    import json

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "sample_event.json")

    with open(file_path) as f:
        event = json.load(f)

    handler(event, None)