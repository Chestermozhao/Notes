## Json Web Token
- Basic concepts
	- headers
	```javascript
		{
		    // alg means secret alg and typ means type
		    // alg default is SHA-256; typ default is JWT
		    “alg”: “HS256”,
		    “typ”: “JWT”
		}
	```
	- payload: json type datas
	- signature: likes a key to valid token
- Advantages
	- using head to deliver token: makes ajax request more safe than before
	- replace session at server side
	- reduce need of cookie, more safe while confronting CORS

## JWT in Python: pyjwt
- install: `pip install PyJWT`
```python
	jwt.encode({'some': 'payload'}, private_key, algorithm='RS256')lee
	# if verify is False means not use authorization
	jwt.decode(encoded, public_key, algorithms='RS256', verify=False)
```
- Save info in head: if multi-key exist in jwt you can add info in head
- Registered Claim Names: JWT既定可選參數
	- exp
		- timestamp or datetime(will be transferred to int): finally is int type timestamp
		- must use utc time: exp will compare with utc time of request
		- verify_expiration=False: means dont validate exp
		- leeway= (seconds): means you can tolerate the degree of disprecising
		```python
		jwt_payload = jwt.encode({
		    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
		}, 'secret')

		time.sleep(32)
		jwt.decode(jwt_payload, 'secret', leeway=10, verify_expiration=True, algorithms=['HS256'])
		```
		- jwt.ExpiredSignatureError
	- nbf: not before time
		- jwt.ImmatureSignatureError
	- iss: issuer of JWT
		- issuer=(issuer): deliver issuer to match the value of iss
		```python
		payload = {
		    'some': 'payload',
		    'iss': 'urn:foo'
		}

		token = jwt.encode(payload, 'secret')
		decoded = jwt.decode(token, 'secret', issuer='urn:foo', algorithms=['HS256'])
		```
		- jwt.InvalidIssuerError
	- aud: likes as iss but this statement is the tag of audience
		- audience=(audience): deliver audience to match the value of aud
		```python
		payload = {
		    'some': 'payload',
		    'aud': 'urn:foo'
		}

		token = jwt.encode(payload, 'secret')
		decoded = jwt.decode(token, 'secret', audience='urn:foo', algorithms=['HS256'])
		```
		- jwt.InvalidAudienceError
	- iat: issued at
		- type must int
		```python
		jwt.encode({'iat': 1371720939}, 'secret')
		jwt.encode({'iat': datetime.utcnow()}, 'secret')
		```
- Already support crypto algs
	- multi decode algs: you can assign more than one algs while decoding
	```python
	jwt.decode(encoded, 'secret', algorithms=['HS512', 'HS256'])
	```
	- algs list
	```
	HS256 - HMAC using SHA-256 hash algorithm (default)
	HS384 - HMAC using SHA-384 hash algorithm
	HS512 - HMAC using SHA-512 hash algorithm
	ES256 - ECDSA signature algorithm using SHA-256 hash algorithm
	ES384 - ECDSA signature algorithm using SHA-384 hash algorithm
	ES512 - ECDSA signature algorithm using SHA-512 hash algorithm
	RS256 - RSASSA-PKCS1-v1_5 signature algorithm using SHA-256 hash algorithm
	RS384 - RSASSA-PKCS1-v1_5 signature algorithm using SHA-384 hash algorithm
	RS512 - RSASSA-PKCS1-v1_5 signature algorithm using SHA-512 hash algorithm
	PS256 - RSASSA-PSS signature using SHA-256 and MGF1 padding with SHA-256
	PS384 - RSASSA-PSS signature using SHA-384 and MGF1 padding with SHA-384
	PS512 - RSASSA-PSS signature using SHA-512 and MGF1 padding with SHA-512
	```
- Cryptography: [other crypto algorithms](https://pypi.org/project/cryptography/)
