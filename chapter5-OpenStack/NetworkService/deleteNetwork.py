#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def delete_network(conn):
    network = conn.network.find_network('packtpub-network')

    # Delete all subnets in the network
    for subnet in network.subnet_ids:
        conn.network.delete_subnet(subnet, ignore_missing=False)

    # Delete the network
    conn.network.delete_network(network, ignore_missing=False)

delete_network(conn)
