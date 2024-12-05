import requests

def get_client_ip(request):
    """Get the IP address of the client from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_public_ip():
    # Get the current public IP using an external api
    public_ip = None
    return public_ip


def get_user_country(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            data = response.json()
            return data.get('country', 'Unknown')
    except Exception as e:
        print(f"Error fetching country: {e}")
    return 'Unknown'