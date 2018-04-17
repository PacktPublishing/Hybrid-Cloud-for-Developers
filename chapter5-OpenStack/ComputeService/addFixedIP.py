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
    server_id="7cdaa375-f1b5-40ab-81bd-7e3d052f370d"
    network_id="60bf3c33-dc83-4251-8024-f2781e34321d"
    conn.compute.add_fixed_ip_to_server(server_id,network_id)

add_fixed_ip(conn);
