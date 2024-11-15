from google_auth_oauthlib.flow import InstalledAppFlow
import base64

def get_refresh_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        ['https://www.googleapis.com/auth/calendar.readonly']
    )
    credentials = flow.run_local_server(port=0)
    print(base64.b64encode(credentials.refresh_token.encode()).decode())

if __name__ == "__main__":
    get_refresh_token()

