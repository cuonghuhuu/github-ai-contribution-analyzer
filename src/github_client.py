import os

import requests
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

BASE_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def build_headers():
    headers = {
        "Accept": "application/vnd.github+json"
    }

    # Public repositories can still be read without a token,
    # but a token helps avoid strict rate limits.
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    return headers


def get_commits(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url, headers=build_headers(), timeout=30)
    except requests.RequestException as error:
        print(f"Không thể lấy dữ liệu commit từ GitHub API: {error}")
        return []

    if response.status_code != 200:
        print(f"Không thể lấy dữ liệu commit. Mã lỗi: {response.status_code}")
        print(f"Chi tiết từ GitHub API: {response.text}")
        return []

    return response.json()


def get_commit_detail(owner, repo, sha):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits/{sha}"

    try:
        response = requests.get(url, headers=build_headers(), timeout=30)
    except requests.RequestException as error:
        print(f"Không thể lấy chi tiết commit {sha}: {error}")
        return None

    if response.status_code != 200:
        print(f"Không thể lấy chi tiết commit {sha}. Mã lỗi: {response.status_code}")
        return None

    return response.json()
