from os import environ

from git import Repo
from github import Github

with open("README.md", "a") as f:
    f.write("test\n")

builds = "builds_for_skipfile_runs.txt"

repo_path = "."
local_repo = Repo(repo_path)

local_repo.git.add(u=True)
api_key_name = "TEST_REPO_ACCESS_TOKEN"
my_api_key = environ.get(api_key_name)
g = Github(my_api_key)
username = "katieworton"
github_repo = g.get_repo(f"{username}/test-repo")

local_repo.git.commit(
    "-m",
    "Test update.",
)

if "test" not in [ref.name for ref in local_repo.branches]:
    new_branch = local_repo.create_head("test")

local_repo.git.checkout("test")

local_repo.git.push(
    f"https://{username}:{my_api_key}@github.com/{username}/test-repo", f"test", "-f"
)
