import os
from api import ipify_extract_public_ip, godaddy_extract_host_record, godaddy_update_host_record


# Environment variables
ipify_api_url = os.environ.get("IPIFY_API_URL")
godaddy_api_url = os.environ.get("GODADDY_API_URL")
godaddy_api_key = os.environ.get("GODADDY_API_KEY")
godaddy_api_secret = os.environ.get("GODADDY_API_SECRET")
godaddy_root_domains = os.environ.get("GODADDY_ROOT_DOMAINS")
godaddy_root_subdomains = os.environ.get("GODADDY_ROOT_SUBDOMAINS")

# Extract the current local public IP address
ipify_public_ip = ipify_extract_public_ip(ipify_api_url=ipify_api_url)

# Extract the list of all the GoDaddy root domains
godaddy_root_host_records = godaddy_root_domains.split(",")

# Extract the list of all the GoDaddy host records
godaddy_host_records = godaddy_root_subdomains.split(",")

# Compare the current local public IP address with the GoDaddy host records
for godaddy_root_host_record in godaddy_root_host_records:
    for godaddy_host_record in godaddy_host_records:
        godaddy_host_record_status = godaddy_extract_host_record(
            godaddy_api_url=godaddy_api_url, godaddy_api_key=godaddy_api_key, godaddy_api_secret=godaddy_api_secret, godaddy_root_domain=godaddy_root_host_record, godaddy_host_record=godaddy_host_record, public_ip=ipify_public_ip)

        # Update the GoDaddy host records
        if godaddy_host_record_status is False:
            godaddy_update_host_record(
                godaddy_api_url=godaddy_api_url, godaddy_api_key=godaddy_api_key, godaddy_api_secret=godaddy_api_secret, godaddy_root_domain=godaddy_root_host_record, godaddy_host_record=godaddy_host_record, public_ip=ipify_public_ip)
