# Import the OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def download_image_stream(conn):
    # Find the image you would like to download.
    image = conn.image.find_image("cirros-0.3.5-x86_64-disk")

    with open("local_image.qcow2", "wb") as local_file:
        response = conn.image.download_image(image, stream=True)

        # Read 2048 bytes per iteration until we read the entire file
        for chunk in response.iter_content(chunk_size=2048):
            local_file.write(chunk)

download_image_stream(conn)
