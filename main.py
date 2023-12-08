def convert_to_socks5(proxy_list):
    socks5_proxies = []
    for proxy in proxy_list:
        parts = proxy.split(':')
        socks5_proxies.append(f"socks5://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}")
    return socks5_proxies

def convert_to_http(proxy_list):
    http_proxies = []
    for proxy in proxy_list:
        parts = proxy.split(':')
        http_proxies.append(f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}")
    return http_proxies

def write_to_file(proxies, filename):
    with open(filename, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")

# Read proxies from file
with open("proxies_raw.txt", "r") as file:
    proxies = file.read().splitlines()

# Convert to SOCKS5 format
socks5_list = convert_to_socks5(proxies)
write_to_file(socks5_list, "proxies_ready_socks5.txt")

# Convert to HTTP format
http_list = convert_to_http(proxies)
write_to_file(http_list, "proxies_ready_http.txt")
