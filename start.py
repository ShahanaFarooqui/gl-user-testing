from glclient import TlsConfig, Signer, Scheduler

network = 'testnet'
node_id = bytes.fromhex('node_id')
device_cert="-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----\n\n\n"
device_key="-----BEGIN PRIVATE KEY-----\r\n\r\n-----END PRIVATE KEY-----\r\n"

tls = TlsConfig().identity(device_cert, device_key)

scheduler = Scheduler(node_id, network, tls)
print(f'SCHEDULER: {scheduler}\n\n')

node = scheduler.node()
print(f'NODE: {node}\n\n')
print(f'NODE INFO: {node.get_info()}\n\n')
