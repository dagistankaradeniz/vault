from venv import create
import hvac
import json

def write_secret():

    client = hvac.Client(url='http://localhost:8200')
    create_response = client.secrets.kv.v2.create_or_update_secret(path='hello', secret=dict(walle="eve"))

    print(json.dumps(create_response, indent=4, sort_keys=True))
    

write_secret()