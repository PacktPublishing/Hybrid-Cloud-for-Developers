# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def download_image(conn):
    # Find the image that you want to download
    image = conn.image.find_image("cirros-0.3.5-x86_64-disk")

    # Open a file to write to in the local system
    with open("local_image.qcow2", "w") as local_file:
        response = conn.image.download_image(image)

        # Write to the local file.
        local_file.write(response)

download_image(conn)
