import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#store API in variable
response_dict = r.json()

cnt = response_dict["total_count"]

#print(fTotal Repositories: " {cnt}")

repo_dict = response_dict["items"]

#print(f"Repositories Returned: {repo_dict}")

for key in response_dict[]:
    print()
    print(f"Name: {response_dict["name"]}")
    print(f"Login: {response_dict["owner"],["login"]}")
    print(f"Login: {response_dict["starsgazers_count"]}")
    print(f"URL: {response_dict["html_url"]}")
    print(f"Created At: {response_dict["created_at"]}")
    print(f"Updated At: {response_dict["updated_at"]}")
    print(f"Description: {response_dict["description"]}")
    print()
