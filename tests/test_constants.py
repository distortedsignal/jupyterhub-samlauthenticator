


sample_metadata_xml = '''<?xml version="1.0"?><EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://app.onelogin.com/saml/metadata/719630"><IDPSSODescriptor xmlns:ds="http://www.w3.org/2000/09/xmldsig#" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"><KeyDescriptor use="signing"><ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEF
BQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxP
bmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4X
DTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAP
BgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMM
F09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJ
Cy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bk
sRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b
+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmO
nhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm
7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQC
MAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuA
FLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UE
CgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25l
TG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1Ud
DwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskh
OBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3O
u6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270p
Mtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3Tnhxlg
iEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16H
m76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></KeyDescriptor><SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/slo/719630"/><NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-post/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/soap/sso/719630"/></IDPSSODescriptor></EntityDescriptor>
'''

sample_metadata_tampered_entity = '''<?xml version="1.0"?><EntityDescriptor entityID="https://app.onelogin.com/saml/metadata/719630123" xmlns="urn:oasis:names:tc:SAML:2.0:metadata"><IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><KeyDescriptor use="signing"><ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEF
BQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxP
bmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4X
DTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAP
BgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMM
F09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJ
Cy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bk
sRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b
+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmO
nhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm
7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQC
MAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuA
FLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UE
CgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25l
TG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1Ud
DwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskh
OBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3O
u6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270p
Mtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3Tnhxlg
iEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16H
m76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></KeyDescriptor><SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/slo/719630"/><NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-post/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/soap/sso/719630"/></IDPSSODescriptor></EntityDescriptor>
'''

sample_metadata_no_entity = '''<?xml version="1.0"?><EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata"><IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><KeyDescriptor use="signing"><ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:X509Data><ds:X509Certificate>MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEF
BQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxP
bmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4X
DTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAP
BgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMM
F09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJ
Cy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bk
sRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b
+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmO
nhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm
7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQC
MAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuA
FLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UE
CgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25l
TG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1Ud
DwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskh
OBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3O
u6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270p
Mtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3Tnhxlg
iEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16H
m76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></KeyDescriptor><SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/slo/719630"/><NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-post/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/soap/sso/719630"/></IDPSSODescriptor></EntityDescriptor>
'''

sample_metadata_no_cert_xml = '''<?xml version="1.0"?><EntityDescriptor entityID="https://app.onelogin.com/saml/metadata/719630" xmlns="urn:oasis:names:tc:SAML:2.0:metadata"><IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol"><SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/slo/719630"/><NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-redirect/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/http-post/sso/719630"/><SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="https://bluedata-test-before-deploy.onelogin.com/trust/saml2/soap/sso/719630"/></IDPSSODescriptor></EntityDescriptor>'''

x509_cert = '''MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEF
BQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxP
bmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4X
DTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAP
BgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMM
F09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJ
Cy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bk
sRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b
+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmO
nhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm
7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQC
MAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuA
FLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UE
CgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25l
TG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1Ud
DwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskh
OBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3O
u6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270p
Mtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3Tnhxlg
iEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16H
m76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==
'''

b64encoded_response_xml = bytearray('''PHNhbWxwOlJlc3BvbnNlIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0
YzpTQU1MOjIuMDphc3NlcnRpb24iIHhtbG5zOnNhbWxwPSJ1cm46b2FzaXM6
bmFtZXM6dGM6U0FNTDoyLjA6cHJvdG9jb2wiIElEPSJSZWRlYjlmMGIzZmJi
NTBkZmJlNDM1NDFiMzI1M2IyNGM5OTViZTMzOSIgVmVyc2lvbj0iMi4wIiBJ
c3N1ZUluc3RhbnQ9IjIwMTktMDQtMDlUMjE6MzQ6NTJaIiBEZXN0aW5hdGlv
bj0ie3JlY2lwaWVudH0iPjxzYW1sOklzc3Vlcj5odHRwczovL2FwcC5vbmVs
b2dpbi5jb20vc2FtbC9tZXRhZGF0YS83MTk2MzA8L3NhbWw6SXNzdWVyPjxz
YW1scDpTdGF0dXM+PHNhbWxwOlN0YXR1c0NvZGUgVmFsdWU9InVybjpvYXNp
czpuYW1lczp0YzpTQU1MOjIuMDpzdGF0dXM6U3VjY2VzcyIvPjwvc2FtbHA6
U3RhdHVzPjxzYW1sOkFzc2VydGlvbiB4bWxuczpzYW1sPSJ1cm46b2FzaXM6
bmFtZXM6dGM6U0FNTDoyLjA6YXNzZXJ0aW9uIiB4bWxuczp4cz0iaHR0cDov
L3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEiIHhtbG5zOnhzaT0iaHR0cDov
L3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIFZlcnNpb249
IjIuMCIgSUQ9InBmeDlhM2ExNTQ2LTJiN2QtYWI5ZS04N2IxLTJkY2RiMWI3
Yzc3ZCIgSXNzdWVJbnN0YW50PSIyMDE5LTA0LTA5VDIxOjM0OjUyWiI+PHNh
bWw6SXNzdWVyPmh0dHBzOi8vYXBwLm9uZWxvZ2luLmNvbS9zYW1sL21ldGFk
YXRhLzcxOTYzMDwvc2FtbDpJc3N1ZXI+PGRzOlNpZ25hdHVyZSB4bWxuczpk
cz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PGRzOlNp
Z25lZEluZm8+PGRzOkNhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGht
PSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiLz48
ZHM6U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5v
cmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIi8+PGRzOlJlZmVyZW5jZSBV
Ukk9IiNwZng5YTNhMTU0Ni0yYjdkLWFiOWUtODdiMS0yZGNkYjFiN2M3N2Qi
PjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRw
Oi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25h
dHVyZSIvPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3Lncz
Lm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiLz48L2RzOlRyYW5zZm9ybXM+
PGRzOkRpZ2VzdE1ldGhvZCBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3Jn
LzIwMDAvMDkveG1sZHNpZyNzaGExIi8+PGRzOkRpZ2VzdFZhbHVlPnQzVEp4
TmZLeEdLU1RSNmVCSDRsb2VhTyt3RT08L2RzOkRpZ2VzdFZhbHVlPjwvZHM6
UmVmZXJlbmNlPjwvZHM6U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU+
Z0kwRldlRFJaZVNDdWZRazdJS1doY0xKMG9RU0RwM3Y1TnlIeVcxandwK1BV
cXNWRlZEdnV3RDFRVlU1QmZzM054aDg4OG5IL2RoZ0RGT1NaR0RWWmtwZTZR
dThwMzZxLzlNT0JEOEMvN3ZqVmVNaVBmdmg2bXJpWFJSSmpnbis5dU5kelBT
bG5pNXpHdHpRaGszZ0J2MHA3VkRiTzdaclBBbjdkM2hhbUw5WVRUenBrOUt6
ZW5HQkZzRGVwWDR2T3ZudGVzZWpyRFdCcnF0ckRPa2szTGJFTnA4VFVHM1Rn
cXVCdTRBcUpqRmsrZUxjOE1KVndHY2JaQWZTdTFzQ3BRbTRaNmpSblVjVUVI
d2lXYkpwTHJqb3VFT1dBSjloN040c1U0Z0QycnRvZzBYZ3ZMN250enNuMjl1
VmM0dVVJQTMwOFRuemt2dHo0dE4rZ284UEtnPT08L2RzOlNpZ25hdHVyZVZh
bHVlPjxkczpLZXlJbmZvPjxkczpYNTA5RGF0YT48ZHM6WDUwOUNlcnRpZmlj
YXRlPk1JSUVHakNDQXdLZ0F3SUJBZ0lVUWR3RzVtdDQybTNQeXVhTjFaOHlP
Sis3dC9rd0RRWUpLb1pJaHZjTkFRRUZCUUF3V1RFTE1Ba0dBMVVFQmhNQ1ZW
TXhFVEFQQmdOVkJBb01DRUpzZFdWa1lYUmhNUlV3RXdZRFZRUUxEQXhQYm1W
TWIyZHBiaUJKWkZBeElEQWVCZ05WQkFNTUYwOXVaVXh2WjJsdUlFRmpZMjkx
Ym5RZ01URXpPVFkxTUI0WERURTNNRGt4TURJeE1qSXdOMW9YRFRJeU1Ea3hN
VEl4TWpJd04xb3dXVEVMTUFrR0ExVUVCaE1DVlZNeEVUQVBCZ05WQkFvTUNF
SnNkV1ZrWVhSaE1SVXdFd1lEVlFRTERBeFBibVZNYjJkcGJpQkpaRkF4SURB
ZUJnTlZCQU1NRjA5dVpVeHZaMmx1SUVGalkyOTFiblFnTVRFek9UWTFNSUlC
SWpBTkJna3Foa2lHOXcwQkFRRUZBQU9DQVE4QU1JSUJDZ0tDQVFFQTNuai9J
M0dJUm1INjM5OTZFNlJkU21aZDk2bTZBK3NaVllNNnBXb2FydytWUVdwMkNs
Z0pDeTc1b1JCMS9PcjRGdDlVOExpd1IwUjdRYWU1SWw3ZHg2bUNmZTcyeVVa
QXJja04rWFBUN0twRVkxYTVXMWJrc1JKb0ZWT3E4MS9xZStZK2huYlpSVXc0
dGtrcmMyVGE5T0dLSHdaWWp3cC9oRjJBeVpBV2NjZVpJOEhWaFE5YitjOWJE
QUQrOC8rL05xa1gyeUlPMUt4RG1aK2tFODVmMDdwRFRsbHdFNC9MRllzQmxJ
dVZwOERpeHoxeExGbU9uaFJ6OWNyUC95YWl5OUcremFZZGgvNXlPSElXQ2FP
MzFTdW1oZjRrNDdUUGJ5R1ZRNUJZRkdXR2JLa3gzM2ptN0Z2RURONTVwOCtH
KytzQXhkVmk1L09oZ3E1QlNnakpXUUlEQVFBQm80SFpNSUhXTUF3R0ExVWRF
d0VCL3dRQ01BQXdIUVlEVlIwT0JCWUVGTEZjdDJyUlZZUGt3YlUyS3o3YVQy
clhMaE1CTUlHV0JnTlZIU01FZ1k0d2dZdUFGTEZjdDJyUlZZUGt3YlUyS3o3
YVQyclhMaE1Cb1Yya1d6QlpNUXN3Q1FZRFZRUUdFd0pWVXpFUk1BOEdBMVVF
Q2d3SVFteDFaV1JoZEdFeEZUQVRCZ05WQkFzTURFOXVaVXh2WjJsdUlFbGtV
REVnTUI0R0ExVUVBd3dYVDI1bFRHOW5hVzRnUVdOamIzVnVkQ0F4TVRNNU5q
V0NGRUhjQnVacmVOcHR6OHJtamRXZk1qaWZ1N2Y1TUE0R0ExVWREd0VCL3dR
RUF3SUhnREFOQmdrcWhraUc5dzBCQVFVRkFBT0NBUUVBdHZTVHArSXpFUmFP
TXg3T0RLSldNc2toT0JLbDM5cjVSWWUrQlgyLzZ2dWI3clRsRWJHR2VHYm9p
RHFYM3lDYUR4d0s0UUkyRTNRNUJXZUNqcUxxSUYzT3U2RkxENUJjNnNOTmhs
dXdqS1lhaktyUDVib3phaWd1Q0N1aHFTV0tlQ1E3L2hSMkNRRUhQSEJOS1hY
czI3MHBNdG00R1Q2ZEduN2Izd3FJbUJjQktiVlZqSkNTYWxXYUkyd1VaVnMr
MlVQMnBlbzhEbUNYZHhUcU4zVG5oeGxnaUVFSDdjYzh1Qk1KaFpUUlF5TjFT
VktQWUovb1A1QWdOb1NiRXVBYWVBMlJBS1BLY05jU2tEdmhJRzY4YzE2SG03
Nis4Z2V6VmNJUXpwL3g1Ly9TcnBwMVkxVUVkRi94YzlGT1ROcXB3alB6ZDJa
UE5MZlZXendhMUdvYjVRPT08L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1
MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48c2FtbDpTdWJq
ZWN0PjxzYW1sOk5hbWVJRCBGb3JtYXQ9InVybjpvYXNpczpuYW1lczp0YzpT
QU1MOjEuMTpuYW1laWQtZm9ybWF0OmVtYWlsQWRkcmVzcyI+Qmx1ZWRhdGE8
L3NhbWw6TmFtZUlEPjxzYW1sOlN1YmplY3RDb25maXJtYXRpb24gTWV0aG9k
PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6Y206YmVhcmVyIj48c2Ft
bDpTdWJqZWN0Q29uZmlybWF0aW9uRGF0YSBOb3RPbk9yQWZ0ZXI9IjIwMTkt
MDQtMDlUMjE6Mzc6NTJaIiBSZWNpcGllbnQ9IntyZWNpcGllbnR9Ii8+PC9z
YW1sOlN1YmplY3RDb25maXJtYXRpb24+PC9zYW1sOlN1YmplY3Q+PHNhbWw6
Q29uZGl0aW9ucyBOb3RCZWZvcmU9IjIwMTktMDQtMDlUMjE6MzE6NTJaIiBO
b3RPbk9yQWZ0ZXI9IjIwMTktMDQtMDlUMjE6Mzc6NTJaIj48c2FtbDpBdWRp
ZW5jZVJlc3RyaWN0aW9uPjxzYW1sOkF1ZGllbmNlPnthdWRpZW5jZX08L3Nh
bWw6QXVkaWVuY2U+PC9zYW1sOkF1ZGllbmNlUmVzdHJpY3Rpb24+PC9zYW1s
OkNvbmRpdGlvbnM+PHNhbWw6QXV0aG5TdGF0ZW1lbnQgQXV0aG5JbnN0YW50
PSIyMDE5LTA0LTA5VDIxOjM0OjUxWiIgU2Vzc2lvbk5vdE9uT3JBZnRlcj0i
MjAxOS0wNC0xMFQyMTozNDo1MloiIFNlc3Npb25JbmRleD0iX2E5NjI4Zjkw
LTNkMTktMDEzNy1iMmU0LTAyOWMwYmYwNjdmNiI+PHNhbWw6QXV0aG5Db250
ZXh0PjxzYW1sOkF1dGhuQ29udGV4dENsYXNzUmVmPnVybjpvYXNpczpuYW1l
czp0YzpTQU1MOjIuMDphYzpjbGFzc2VzOlBhc3N3b3JkUHJvdGVjdGVkVHJh
bnNwb3J0PC9zYW1sOkF1dGhuQ29udGV4dENsYXNzUmVmPjwvc2FtbDpBdXRo
bkNvbnRleHQ+PC9zYW1sOkF1dGhuU3RhdGVtZW50PjxzYW1sOkF0dHJpYnV0
ZVN0YXRlbWVudD48c2FtbDpBdHRyaWJ1dGUgTmFtZUZvcm1hdD0idXJuOm9h
c2lzOm5hbWVzOnRjOlNBTUw6Mi4wOmF0dHJuYW1lLWZvcm1hdDpiYXNpYyIg
TmFtZT0ibWVtYmVyT2YiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlIHhtbG5zOnhz
aT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2Ui
IHhzaTp0eXBlPSJ4czpzdHJpbmciLz48L3NhbWw6QXR0cmlidXRlPjxzYW1s
OkF0dHJpYnV0ZSBOYW1lRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FN
TDoyLjA6YXR0cm5hbWUtZm9ybWF0OmJhc2ljIiBOYW1lPSJVc2VyLkZpcnN0
TmFtZSI+PHNhbWw6QXR0cmlidXRlVmFsdWUgeG1sbnM6eHNpPSJodHRwOi8v
d3d3LnczLm9yZy8yMDAxL1hNTFNjaGVtYS1pbnN0YW5jZSIgeHNpOnR5cGU9
InhzOnN0cmluZyI+VG9tPC9zYW1sOkF0dHJpYnV0ZVZhbHVlPjwvc2FtbDpB
dHRyaWJ1dGU+PHNhbWw6QXR0cmlidXRlIE5hbWVGb3JtYXQ9InVybjpvYXNp
czpuYW1lczp0YzpTQU1MOjIuMDphdHRybmFtZS1mb3JtYXQ6YmFzaWMiIE5h
bWU9IlBlcnNvbkltbXV0YWJsZUlEIj48c2FtbDpBdHRyaWJ1dGVWYWx1ZSB4
bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWlu
c3RhbmNlIiB4c2k6dHlwZT0ieHM6c3RyaW5nIj5qb2VsPC9zYW1sOkF0dHJp
YnV0ZVZhbHVlPjwvc2FtbDpBdHRyaWJ1dGU+PHNhbWw6QXR0cmlidXRlIE5h
bWVGb3JtYXQ9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphdHRybmFt
ZS1mb3JtYXQ6YmFzaWMiIE5hbWU9IlVzZXIuTGFzdE5hbWUiPjxzYW1sOkF0
dHJpYnV0ZVZhbHVlIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAw
MS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhzaTp0eXBlPSJ4czpzdHJpbmciPkJs
dWVkYXRhPC9zYW1sOkF0dHJpYnV0ZVZhbHVlPjwvc2FtbDpBdHRyaWJ1dGU+
PHNhbWw6QXR0cmlidXRlIE5hbWVGb3JtYXQ9InVybjpvYXNpczpuYW1lczp0
YzpTQU1MOjIuMDphdHRybmFtZS1mb3JtYXQ6YmFzaWMiIE5hbWU9IlVzZXIu
ZW1haWwiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlIHhtbG5zOnhzaT0iaHR0cDov
L3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhzaTp0eXBl
PSJ4czpzdHJpbmciPnRrZWxsZXlAYmx1ZWRhdGEuY29tPC9zYW1sOkF0dHJp
YnV0ZVZhbHVlPjwvc2FtbDpBdHRyaWJ1dGU+PC9zYW1sOkF0dHJpYnV0ZVN0
YXRlbWVudD48L3NhbWw6QXNzZXJ0aW9uPjwvc2FtbHA6UmVzcG9uc2U+Cgo=''', encoding='utf-8')

sample_response_xml               = '''<samlp:Response xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="Redeb9f0b3fbb50dfbe43541b3253b24c995be339" Version="2.0" IssueInstant="2019-04-09T21:34:52Z" Destination="{recipient}"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><samlp:Status><samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/></samlp:Status><saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Version="2.0" ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><ds:Reference URI="#pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>t3TJxNfKxGKSTR6eBH4loeaO+wE=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>gI0FWeDRZeSCufQk7IKWhcLJ0oQSDp3v5NyHyW1jwp+PUqsVFVDvuwD1QVU5Bfs3Nxh888nH/dhgDFOSZGDVZkpe6Qu8p36q/9MOBD8C/7vjVeMiPfvh6mriXRRJjgn+9uNdzPSlni5zGtzQhk3gBv0p7VDbO7ZrPAn7d3hamL9YTTzpk9KzenGBFsDepX4vOvntesejrDWBrqtrDOkk3LbENp8TUG3TgquBu4AqJjFk+eLc8MJVwGcbZAfSu1sCpQm4Z6jRnUcUEHwiWbJpLrjouEOWAJ9h7N4sU4gD2rtog0XgvL7ntzsn29uVc4uUIA308Tnzkvtz4tN+go8PKg==</ds:SignatureValue><ds:KeyInfo><ds:X509Data><ds:X509Certificate>MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEFBQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4XDTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJCy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bksRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmOnhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuAFLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UECgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25lTG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1UdDwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskhOBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3Ou6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270pMtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3TnhxlgiEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16Hm76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></ds:Signature><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z" NotOnOrAfter="2019-04-09T21:37:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionNotOnOrAfter="2019-04-10T21:34:52Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="memberOf"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.FirstName"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="PersonImmutableID"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.LastName"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.email"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion></samlp:Response>'''
tampered_sample_response_xml      = '''<samlp:Response xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="Redeb9f0b3fbb50dfbe43541b3253b24c995be339" Version="2.0" IssueInstant="2019-04-09T21:34:52Z" Destination="{recipient}"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><samlp:Status><samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/></samlp:Status><saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" Version="2.0" ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"><ds:SignedInfo><ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/><ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/><ds:Reference URI="#pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d"><ds:Transforms><ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/><ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/></ds:Transforms><ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/><ds:DigestValue>t3TJxNfKxGKSTR6eBH4loeaO+wE=</ds:DigestValue></ds:Reference></ds:SignedInfo><ds:SignatureValue>gI0FWeDRZeSCufQk7IKWhcLJ0oQSDp3v5NyHyW1jwp+PUqsVFVDvuwD1QVU5Bfs3Nxh888nH/dhgDFOSZGDVZkpe6Qu8p36q/9MOBD8C/7vjVeMiPfvh6mriXRRJjgn+9uNdzPSlni5zGtzQhk3gBv0p7VDbO7ZrPAn7d3hamL9YTTzpk9KzenGBFsDepX4vOvntesejrDWBrqtrDOkk3LbENp8TUG3TgquBu4AqJjFk+eLc8MJVwGcbZAfSu1sCpQm4Z6jRnUcUEHwiWbJpLrjouEOWAJ9h7N4sU4gD2rtog0XgvL7ntzsn29uVc4uUIA308Tnzkvtz4tN+go8PKg==</ds:SignatureValue><ds:KeyInfo><ds:X509Data><ds:X509Certificate>MIIEGjCCAwKgAwIBAgIUQdwG5mt42m3PyuaN1Z8yOJ+7t/kwDQYJKoZIhvcNAQEFBQAwWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MB4XDTE3MDkxMDIxMjIwN1oXDTIyMDkxMTIxMjIwN1owWTELMAkGA1UEBhMCVVMxETAPBgNVBAoMCEJsdWVkYXRhMRUwEwYDVQQLDAxPbmVMb2dpbiBJZFAxIDAeBgNVBAMMF09uZUxvZ2luIEFjY291bnQgMTEzOTY1MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3nj/I3GIRmH63996E6RdSmZd96m6A+sZVYM6pWoarw+VQWp2ClgJCy75oRB1/Or4Ft9U8LiwR0R7Qae5Il7dx6mCfe72yUZArckN+XPT7KpEY1a5W1bksRJoFVOq81/qe+Y+hnbZRUw4tkkrc2Ta9OGKHwZYjwp/hF2AyZAWcceZI8HVhQ9b+c9bDAD+8/+/NqkX2yIO1KxDmZ+kE85f07pDTllwE4/LFYsBlIuVp8Dixz1xLFmOnhRz9crP/yaiy9G+zaYdh/5yOHIWCaO31Sumhf4k47TPbyGVQ5BYFGWGbKkx33jm7FvEDN55p8+G++sAxdVi5/Ohgq5BSgjJWQIDAQABo4HZMIHWMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFLFct2rRVYPkwbU2Kz7aT2rXLhMBMIGWBgNVHSMEgY4wgYuAFLFct2rRVYPkwbU2Kz7aT2rXLhMBoV2kWzBZMQswCQYDVQQGEwJVUzERMA8GA1UECgwIQmx1ZWRhdGExFTATBgNVBAsMDE9uZUxvZ2luIElkUDEgMB4GA1UEAwwXT25lTG9naW4gQWNjb3VudCAxMTM5NjWCFEHcBuZreNptz8rmjdWfMjifu7f5MA4GA1UdDwEB/wQEAwIHgDANBgkqhkiG9w0BAQUFAAOCAQEAtvSTp+IzERaOMx7ODKJWMskhOBKl39r5RYe+BX2/6vub7rTlEbGGeGboiDqX3yCaDxwK4QI2E3Q5BWeCjqLqIF3Ou6FLD5Bc6sNNhluwjKYajKrP5bozaiguCCuhqSWKeCQ7/hR2CQEHPHBNKXXs270pMtm4GT6dGn7b3wqImBcBKbVVjJCSalWaI2wUZVs+2UP2peo8DmCXdxTqN3TnhxlgiEEH7cc8uBMJhZTRQyN1SVKPYJ/oP5AgNoSbEuAaeA2RAKPKcNcSkDvhIG68c16Hm76+8gezVcIQzp/x5//Srpp1Y1UEdF/xc9FOTNqpwjPzd2ZPNLfVWzwa1Gob5Q==</ds:X509Certificate></ds:X509Data></ds:KeyInfo></ds:Signature><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2219-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z" NotOnOrAfter="2219-04-09T21:37:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionNotOnOrAfter="2219-04-10T21:34:52Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="memberOf"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.FirstName"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="PersonImmutableID"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.LastName"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic" Name="User.email"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion></samlp:Response>'''
tampered_assertion_no_audience    = '''<saml:Assertion ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z" NotOnOrAfter="2019-04-09T21:37:52Z"></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6" SessionNotOnOrAfter="2019-04-10T21:34:52Z"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute Name="memberOf" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute Name="User.FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute Name="PersonImmutableID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion>'''
tampered_assertion_no_issuer      = '''<saml:Assertion ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z" NotOnOrAfter="2019-04-09T21:37:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6" SessionNotOnOrAfter="2019-04-10T21:34:52Z"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute Name="memberOf" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute Name="User.FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute Name="PersonImmutableID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion>'''
tampered_assertion_no_recipient   = '''<saml:Assertion ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z" NotOnOrAfter="2019-04-09T21:37:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6" SessionNotOnOrAfter="2019-04-10T21:34:52Z"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute Name="memberOf" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute Name="User.FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute Name="PersonImmutableID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion>'''
tampered_assertion_no_on_or_after = '''<saml:Assertion ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotBefore="2019-04-09T21:31:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6" SessionNotOnOrAfter="2019-04-10T21:34:52Z"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute Name="memberOf" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute Name="User.FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute Name="PersonImmutableID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion>'''
tampered_assertion_no_not_before  = '''<saml:Assertion ID="pfx9a3a1546-2b7d-ab9e-87b1-2dcdb1b7c77d" IssueInstant="2019-04-09T21:34:52Z" Version="2.0" xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"><saml:Issuer>https://app.onelogin.com/saml/metadata/719630</saml:Issuer><saml:Subject><saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">Bluedata</saml:NameID><saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"><saml:SubjectConfirmationData NotOnOrAfter="2019-04-09T21:37:52Z" Recipient="{recipient}"/></saml:SubjectConfirmation></saml:Subject><saml:Conditions NotOnOrAfter="2019-04-09T21:37:52Z"><saml:AudienceRestriction><saml:Audience>{audience}</saml:Audience></saml:AudienceRestriction></saml:Conditions><saml:AuthnStatement AuthnInstant="2019-04-09T21:34:51Z" SessionIndex="_a9628f90-3d19-0137-b2e4-029c0bf067f6" SessionNotOnOrAfter="2019-04-10T21:34:52Z"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement><saml:AttributeStatement><saml:Attribute Name="memberOf" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string"/></saml:Attribute><saml:Attribute Name="User.FirstName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Tom</saml:AttributeValue></saml:Attribute><saml:Attribute Name="PersonImmutableID" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">joel</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.LastName" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Bluedata</saml:AttributeValue></saml:Attribute><saml:Attribute Name="User.email" NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"><saml:AttributeValue xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">tkelley@bluedata.com</saml:AttributeValue></saml:Attribute></saml:AttributeStatement></saml:Assertion>'''