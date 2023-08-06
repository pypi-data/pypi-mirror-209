import pandas as pd
from github import Github, GithubException


def store_metric(ghClient: Github, dataframe: pd.DataFrame, filepath: str):
    repo_orga, repo_name, file_path = filepath.split('/', 2)

    repo = ghClient.get_repo(repo_orga + "/" + repo_name)
    branch = "production"
    contents = repo.get_contents(file_path, ref=branch)
    assert not isinstance(contents, list), "contents is an array"

    new_contents = dataframe.to_csv(index=False)
    if contents.decoded_content.decode('utf-8') != new_contents:
        commit_message = "Update file :" + file_path
        repo.update_file(contents.path, commit_message,
                         new_contents, contents.sha, branch)

        try:
            repo.create_pull(title="title", body="body",
                             head=branch, base=repo.default_branch)
        except GithubException as e:
            if e.status == 422 and "A pull request already exists" in e.data["message"]:
                print("Pull request already exists, skipping...")
            else:
                raise e
    pass
