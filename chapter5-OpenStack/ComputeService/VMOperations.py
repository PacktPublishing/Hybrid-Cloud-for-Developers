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
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.start_server(server_id)

def stop_server(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.stop_server(server_id)

def pause_server(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.pause_server(server_id)

def unpause_server(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.unpause_server(server_id)

def reboot_server(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.reboot_server(server_id, "HARD")

def create_image_from_vm(conn):
    server_id="613bf835-5eb7-4a4b-ae9c-e0f6f6665f2b"
    conn.compute.create_server_image(server_id,"vm_image",metadata=None)


create_image_from_vm(conn)


