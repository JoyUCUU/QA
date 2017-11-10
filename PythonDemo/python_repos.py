import  requests
import requests
import pygal
from pygal.style import  LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储相应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: " ,r.status_code)

#将API的响应存储到一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = dict(value=repo_dict['stargazers_count'], xlink=repo_dict['html_url'], label=repo_dict['description'])
    plot_dicts.append(plot_dict)

# names,stars = [],[]
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style = my_style,x_label_rotation = 45,show_legend = False)
chart.title = "Most-starred Python Project on GitHub"
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos1.svg')

#研究第一个仓库
#repo_dict = repo_dicts[0]
# for repo_dict in  repo_dicts:
#     print('\nName:',repo_dict['name'])
#     print('Owner:',repo_dict['owner']['login'])
#     print('Stars:',repo_dict['stargazers_count'])
#     print('Repository',repo_dict['html_url'])
#     print('Description',repo_dict['description'])


