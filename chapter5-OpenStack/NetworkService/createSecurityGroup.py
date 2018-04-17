#import OpenStack connection class from the SDK
from openstack import connection

# Create a connection object by calling the constructor and pass the security information
conn = connection.Connection(auth_url="http://192.168.0.106/identity",
project_name="demo",
username="admin",
password="manoj",
user_domain_id="default",
project_domain_id="default")

def open_port(conn):
    security_group = conn.network.create_security_group(name='packtpub-security-group')

    rule = conn.network.create_security_group_rule(
        security_group_id=security_group.id,
        direction='ingress',
        remote_ip_prefix='0.0.0.0/0',
        protocol='tcp',
        port_range_max='443',
        port_range_min='443',
        ethertype='IPv4')

open_port(conn)
