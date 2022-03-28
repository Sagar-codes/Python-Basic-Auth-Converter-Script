import base64

message = "yooo@appycodes.com:abcd1234@12321"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
print(base64_message)

base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(message)

# yooo@appycodes.com:abcd1234@12321

# eW9vb0BhcHB5Y29kZXMuY29tOmFiY2QxMjM0QDEyMzIx #Site Result

# eW9vb0BhcHB5Y29kZXMuY29tOmFiY2QxMjM0QDEyMzIx  #Script Result