from io import BytesIO
from requests.models import Response

def get_mock_currency_api_response():
    """
    Method to create a sample response from the currency API.
    """
    mock_api_response = Response()
    mock_api_response.status_code = 200
    mock_api_response.raw = BytesIO(b'{ "base": "THB", "result": {"KRW": 38.69}}')
    
    return mock_api_response
