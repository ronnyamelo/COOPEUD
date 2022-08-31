curl -X POST -d "grant_type=client_credentials" -u"postman:postman_01" http://localhost:8000/o/token/

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

curl -X POST -d "grant_type=password&username=junior&password=Zorro.0709" -u"postman2:postman_02" http://localhost:8000/o/token/
