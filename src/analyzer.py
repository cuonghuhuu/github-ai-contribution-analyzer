from src.github_client import get_commit_detail


def create_empty_stats():
    return {
        "commits": 0,
        "additions": 0,
        "deletions": 0,
        "files_changed": 0,
        "score": 0
    }


def is_bot_account(author_name, commit_data):
    github_author = commit_data.get("author") or {}
    github_login = github_author.get("login", "")

    author_name_text = (author_name or "").lower()
    github_login_text = github_login.lower()

    return "[bot]" in author_name_text or "[bot]" in github_login_text


def calculate_contribution_score(stats):
    score = (
        stats["commits"] * 1
        + stats["additions"] * 0.02
        + stats["deletions"] * 0.01
        + stats["files_changed"] * 0.5
    )
    return round(score, 2)


def analyze_contributors(owner, repo, commits, commit_limit=10):
    author_stats = {}

    for commit_data in commits[:commit_limit]:
        commit_author = commit_data.get("commit", {}).get("author") or {}
        author_name = commit_author.get("name", "Unknown")
        sha = commit_data.get("sha")

        if is_bot_account(author_name, commit_data):
            continue

        if not sha:
            continue

        if author_name not in author_stats:
            author_stats[author_name] = create_empty_stats()

        author_stats[author_name]["commits"] += 1

        commit_detail = get_commit_detail(owner, repo, sha)

        if not commit_detail:
            continue

        detail_stats = commit_detail.get("stats", {})
        changed_files = commit_detail.get("files", [])

        author_stats[author_name]["additions"] += detail_stats.get("additions", 0)
        author_stats[author_name]["deletions"] += detail_stats.get("deletions", 0)
        author_stats[author_name]["files_changed"] += len(changed_files)

    for stats in author_stats.values():
        stats["score"] = calculate_contribution_score(stats)

    ranked_authors = sorted(
        author_stats.items(),
        key=lambda item: item[1]["score"],
        reverse=True
    )

    return ranked_authors
