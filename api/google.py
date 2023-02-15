from social_core.backends import google

class GoogleOAuth2(google.GoogleOAuth2):
    STATE_PARAMETER = False
    
