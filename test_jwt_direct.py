import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import jwt
from datetime import datetime, timedelta
from backend.auth.jwt_handler import verify_token, TokenData

# Set a test secret for testing purposes
os.environ["BETTER_AUTH_SECRET"] = "test_secret_for_validation"

# Create a test token
payload = {
    "sub": "test_user_123",
    "email": "test@example.com",
    "exp": datetime.utcnow() + timedelta(hours=1)
}
test_token = jwt.encode(payload, "test_secret_for_validation", algorithm="HS256")

print("Test token:", test_token)

# Verify the token
try:
    token_data = verify_token(test_token)
    print("Token verification successful!")
    print(f"User ID: {token_data.user_id}")
    print(f"Email: {token_data.email}")
    print(f"Expiration: {token_data.exp}")
except Exception as e:
    print(f"Token verification failed: {e}")

# Test with invalid token
try:
    invalid_token_data = verify_token("invalid.token.here")
    print("Invalid token verification should have failed!")
except Exception as e:
    print(f"Invalid token correctly rejected: {e}")