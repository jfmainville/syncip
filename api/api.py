import json
import http.client
from json import JSONEncoder


def ipify_extract_public_ip(ipify_api_url):
    # Send a GET request to receive the current public IP address information
    api_connection = http.client.HTTPSConnection(ipify_api_url)
    headers = {
        "Content-Type": "application/json"
    }
    api_connection.request(url="/?format=json",
                           method="GET", headers=headers)
    public_ip_response = api_connection.getresponse()
    public_ip_data = public_ip_response.read()
    public_ip = json.loads(public_ip_data)["ip"]
    return public_ip


def godaddy_extract_host_record(godaddy_api_url, godaddy_api_key, godaddy_api_secret, godaddy_root_domain, godaddy_host_record, public_ip):
    api_connection = http.client.HTTPSConnection(godaddy_api_url)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sso-key " + godaddy_api_key + ":" + godaddy_api_secret
    }
    api_connection.request(
        method="GET", url="/v1/domains/" + str(godaddy_root_domain) + "/records/A/" + str(godaddy_host_record), headers=headers)
    godaddy_public_ip_response = api_connection.getresponse()
    godaddy_public_ip_data = godaddy_public_ip_response.read()
    godaddy_public_ip = json.loads(godaddy_public_ip_data)[0]["data"]
    print(godaddy_public_ip)
    if godaddy_public_ip == public_ip:
        return True
    else:
        return False


def godaddy_update_host_record(godaddy_api_url, godaddy_api_key, godaddy_api_secret, godaddy_root_domain, godaddy_subdomain, public_ip):
    # Send a PUT request to update the required GoDaddy host record
    api_connection = http.client.HTTPSConnection(godaddy_api_url)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "sso-key " + godaddy_api_key + ":" + godaddy_api_secret
    }
    body = json.dumps([{
        "ttl": 600,
        "data": public_ip,
    }])
    api_connection.request(
        method="PUT", url="/v1/domains/" + str(godaddy_root_domain) + "/records/A/" + str(godaddy_subdomain), headers=headers, body=body)
    host_record_update_response = api_connection.getresponse()
    host_record_update_status = host_record_update_response.status
    print(host_record_update_status)
    return host_record_update_status
