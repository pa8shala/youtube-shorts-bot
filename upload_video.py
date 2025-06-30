import os
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

# YouTube scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video(video_file, title, description, tags):
    # OAuth 2.0 authentication
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    credentials = flow.run_console()

    youtube = build("youtube", "v3", credentials=credentials)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"  # People & Blogs
        },
        "status": {
            "privacyStatus": "public",  # You can change to "private" or "unlisted"
        }
    }

    media = MediaFileUpload(video_file)

    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    print("✅ Video uploaded successfully! Video ID:", response["id"])

if __name__ == "_main_":
    today = datetime.date.today().strftime('%Y%m%d')
    video_path = f"videos/final_short_{today}.mp4"

    upload_video(
        video_file=video_path,
        title="🌟 Daily Motivation #Shorts",
        description="Start your day with positive energy! 💪",
        tags=["motivation", "shorts", "daily inspiration"]
    )
