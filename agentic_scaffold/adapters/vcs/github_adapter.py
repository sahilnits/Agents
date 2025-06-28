import requests, os

class GitHubAdapter:
    def __init__(self, repo: str, token: str):
        self.repo = repo
        self.token = token

    def open_pr(self, title: str, body: str, head: str, base: str = "main"):
        url = f"https://api.github.com/repos/{self.repo}/pulls"
        resp = requests.post(
            url,
            json={"title": title, "body": body, "head": head, "base": base},
            headers={"Authorization": f"token {self.token}"},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()