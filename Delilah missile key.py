Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Delilah missile')
m.hexdigest()
'0a74d89f51db67b784e240d3cf7d188d2c0ea9cda19c3d053368c4bf7b3a810f'
