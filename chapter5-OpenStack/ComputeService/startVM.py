# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")


def start_server(conn):
    server_id="7cdaa375-f1b5-40ab-81bd-7e3d052f370d"
    conn.compute.start_server(server_id)

start_server(conn)
