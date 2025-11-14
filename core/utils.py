import secrets
import string

def generate_unique_access_code():
  alphabet = string.ascii_uppercase + string.digits

  basic_secret = secrets.token_hex(6)
  rice_secret = ''.join(secrets.choice(alphabet) for _ in range(8))

  full_secret = basic_secret + rice_secret

  return full_secret
