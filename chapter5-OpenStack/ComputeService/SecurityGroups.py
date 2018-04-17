# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")



def assign_security_group_to_vm(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    security_group_id="d2e47c84-1d31-4008-8192-29cc207338b9"
    conn.compute.add_security_group_to_server(server_id, security_group_id)

def remove_security_group_from_vm(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    security_group_id="d2e47c84-1d31-4008-8192-29cc207338b9"
    conn.compute.remove_security_group_from_server(server_id, security_group_id)

def security_groups(conn):
    for port in conn.network.security_groups():
        print(port)

#assign_security_group_to_vm(conn)

#remove_security_group_from_vm(conn)

security_groups(conn)
