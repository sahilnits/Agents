import requests

class GitHubOAuthAdapter:
    def get_user(self, token: str) -> dict:
        resp = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": f"token {token}"},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()