## SAML SSO
 ![
](https://developers.onelogin.com/assets/img/pages/saml/sso-diagram.svg)
- What is SAML?
	- SAML就是客戶向伺服器發送SAML 請求，然後伺服器返回SAML響應。數據的傳輸符合SAML規範的XML格式表示。  
	- Security Assertion Markup Language
	- For untrusted mutual
	- Base on XML standard
	- The protocol or framework to delivering secure assert
	- Concepts Introduction
		- `IDP`: Third party to arbitration, identity provider
		- `SP`: Server Side, service provider
		- `Subject`: Client Side, service consumer
- Where can use it?
	- User Authentication: usually for user auth(SSO)
	- Attribute Assertion: usually confirm subject
	- Decision Assertion: the result of concrete request
- SAML flow
	- SAML binding
	- SAML Prototol
	- SAML Assertion
- Auth ways
	- SP pull
![SAML: SP pull](https://i2.kknews.cc/SIG=2d2neea/28o000031380o3nnp25p.jpg)
		- Subject get token form IDP and take it to request SP
		- SP take token to request IDP to confirm token valid or not
	- IDP push
	![SAML: IDP push](https://i2.kknews.cc/SIG=2bjvhd6/28nq000n05ss8qp860o9.jpg)
		- Subject request SP
		- SP redirect to IDP to get assert
		- IDP need Subject provide pwd or certificate to do assertion
		- IDP redirect to SP
		- SP check the assertion of IDP
	- Flask-Demo
		- login onelogin(sign up)
		- git clone https://github.com/onelogin/python3-saml.git
		- pip install -r requirements.txt
		- revise settings.json(consistence with onelogin info)
		- `python index.py`
	- [More Information](https://developers.onelogin.com/python-saml-master/docs/saml2/index.html)
