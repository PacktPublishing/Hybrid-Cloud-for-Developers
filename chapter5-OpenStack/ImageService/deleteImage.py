# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def delete_image(conn):
    image = conn.image.find_image("cirros-0.3.5-x86_64-disk")
    conn.image.delete_image(image, ignore_missing=False)

delete_image(conn)
