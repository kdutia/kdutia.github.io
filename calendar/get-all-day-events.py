import os
import base64
import datetime
import re
import sys
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from dotenv import load_dotenv
load_dotenv()

def get_calendar_service():
    """Set up and return Google Calendar service using GitHub Secrets."""
    # Get credentials from environment variables
    client_id = os.environ['GOOGLE_CLIENT_ID']
    client_secret = os.environ['GOOGLE_CLIENT_SECRET']
    # Decode stored refresh token from base64
    refresh_token = base64.b64decode(os.environ['GOOGLE_REFRESH_TOKEN']).decode('utf-8')
    
    creds = Credentials(
        None,  # No access token needed initially
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )
    
    # Refresh the credentials
    creds.refresh(Request())
    
    return build('calendar', 'v3', credentials=creds)

def get_matching_all_day_events(pattern, days_to_fetch, calendar_id='primary'):
    """
    Fetch all-day events matching the given regex pattern.
    
    Args:
        pattern (str): Regex pattern to match against event summary
        days_to_fetch (int): Number of days to look to the past
        calendar_id (str): Calendar ID to fetch events from (default is primary calendar)
    
    Returns:
        list: List of matching events with their dates
    """
    service = get_calendar_service()
    
    now = datetime.datetime.now(datetime.timezone.utc)
    matching_events = []
    
    for offset in range(0, days_to_fetch, 30):
        chunk_days = min(30, days_to_fetch - offset)
        time_max = (now - datetime.timedelta(days=offset)).date().isoformat() + 'T00:00:00Z'
        time_min = (now - datetime.timedelta(days=offset + chunk_days)).date().isoformat() + 'T00:00:00Z'
        
        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        for event in events:
            start = event.get('start', {})
            if 'date' in start:  # all-day event
                summary = event.get('summary', '')
                if re.search(pattern, summary, re.IGNORECASE):
                    matching_events.append({
                        'summary': summary,
                        'date': start['date'],
                        'id': event['id']
                    })
                    
    matching_events.sort(key=lambda x: x['date'])
    
    return matching_events

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python get-calendar-events.py <event_regex>")
        sys.exit(1)
    
    _input = sys.argv[1]
    
    matching_events = get_matching_all_day_events(
        rf".*{_input}.*",
        days_to_fetch=365*10
    )
    
    if matching_events:
        print(f"Found {len(matching_events)} matching all-day events:")
        # Format events for GitHub Actions output
        events_output = "\n".join([
            f"{event['date']}\t{event['summary']}" 
            for event in matching_events]
        )
        
        Path("events.txt").write_text(events_output)
        
        # Also print for logs
        for event in matching_events:
            print(f"{event['date']}\t{event['summary']}")
    else:
        print("No matching all-day events found.")
        