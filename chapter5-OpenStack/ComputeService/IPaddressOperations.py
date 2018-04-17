# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def add_fixed_ip(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    network_id="41e2d44f-70c0-4343-9d9e-7923ee6021e4"
    conn.compute.add_fixed_ip_to_server(server_id,network_id)

def remove_fixed_ip(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.remove_fixed_ip_from_server(server_id,"10.0.0.5")

def add_floating_ip(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.add_floating_ip_to_server(server_id,"172.24.4.1",fixed_address=None)

def remove_floating_ip(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.remove_floating_ip_from_server(server_id,"172.24.4.1")



remove_floating_ip(conn)

