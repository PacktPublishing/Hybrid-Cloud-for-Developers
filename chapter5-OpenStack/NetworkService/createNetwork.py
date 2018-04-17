#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def create_network(conn):
   network = conn.network.create_network(name='packtpub-network')
   print(network)

   subnet = conn.network.create_subnet(
        name='packtpub-subnet',
        network_id=network.id,
        ip_version='4',
        cidr='192.168.0.0/24',
        gateway_ip='192.168.0.1')

   print(subnet)

create_network(conn)
