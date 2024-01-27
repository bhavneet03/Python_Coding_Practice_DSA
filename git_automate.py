from github import Github
import os
from pprint import pprint

token = "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"
g = Github(token)
# get that user by username
user = g.get_user()

count = 0
for repo in user.get_repos():
    #print(repo)
    count = count + 1

print("Total " + str(count)+" Repositories")

#Getting a repository in whole Github
#for repo in g.search_repositories("LeetCode_Practice"):
#	print(repo)
repo = g.get_repo("simranjeet97/LeetCode_Practice")
contents = repo.get_contents("")
for content_file in contents:
	print(content_file)
        