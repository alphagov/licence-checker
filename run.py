#!/usr/bin/env python
import sys

from github import Github
from github.GithubException import UnknownObjectException


def get_repos(client, org):
    repos = client.get_organization(org).get_repos()
    for repo in repos:
        if not repo.archived and not repo.fork and not repo.private:
            yield repo


def check_if_repo_has_license(client, repo):
    repo.get_license()


github_access_key = sys.argv[1]
organisation = sys.argv[2]

client = Github(github_access_key)

repos_count = 0
without_licence_count = 0
for repo in get_repos(client, organisation):
    repos_count += 1
    try:
        check_if_repo_has_license(client, repo)
    except UnknownObjectException:
        without_licence_count += 1
        print("No licence found for {}".format(repo.name))

print("found {} repos".format(repos_count))
print("found {} repos without licences".format(without_licence_count))
