import base64

flagEncoded = "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"

flag = base64.b64decode(flagEncoded).decode()

print(flag)