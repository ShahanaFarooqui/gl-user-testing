import bip39
import secrets
from glclient import TlsConfig, Signer, Scheduler

network='testnet'
rand = secrets.randbits(256).to_bytes(32, 'big')
phrase = bip39.encode_bytes(rand)
print (f'PHRASE: {phrase}\n\n')
seed = bip39.phrase_to_seed(phrase)[:32]
print (f'SEED: {seed.hex()}\n\n')

security_key = {
    'device_cert': '~/gl-certs/client.crt',
    'device_key': '~/gl-certs/client-key.pem'
}

with open(security_key['device_cert'], 'rb') as f:
    cert = f.read()

with open(security_key['device_key'], 'rb') as f:
    key = f.read()

print (f'CERT: {cert}\n\n')
print (f'KEY: {key}\n\n')

tls = TlsConfig().identity(cert, key)

signer = Signer(seed, network=network, tls=tls)
print(f'SIGNER NODE ID: {signer.node_id().hex()}\n\n')

scheduler = Scheduler(node_id=signer.node_id(), network=network, tls=tls)
print(f'SCHEDULER: {scheduler}\n\n')

response = scheduler.register(signer)
print(f'REGISTER: {response}\n\n')

tls = TlsConfig().identity(response.device_cert, response.device_key)

signer = Signer(seed, network=network, tls=tls)
print(f'SIGNER NODE ID: {signer.node_id().hex()}\n\n')

node = Scheduler(node_id=signer.node_id(), network=network, tls=tls).node()
print(f'NODE: {node}\n\n')
print(f'NODE INFO: {node.get_info()}\n\n')
