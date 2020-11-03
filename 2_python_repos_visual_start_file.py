import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict["items"]
repo_links, stars, labels = [], [], []

for repo_dict in response_dict[:10]:
    name = (response_dict["name"])
    url = (response_dict["html_url"])

    repo_link = f"<a href='{url}'>{name}</a>"

    owner = (response_dict["owner"]["login"])
    d = (response_dict["description"])
    s = (response_dict["starsgazers_count"])

    label = f"{owner}<br />{d}"

    labels.append(label)
    repo_links.append(repo_link)
    stars.append(s)

# Make visualization.
data = [{
    'type': 'bar',
    'x': ,
    'y': ,
    'hovertext': ,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')