import secrets

# Generate a random key
secret_key = secrets.token_hex(16)  # 16 bytes, which results in a 32-character hexadecimal string

print(secret_key)
