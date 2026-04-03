from src.analyzer import analyze_contributors
from src.github_client import get_commits
from src.report_generator import save_report_to_markdown


def print_ranking(ranked_authors):
    print("\n=== Contributor Ranking ===\n")

    for index, (author, stats) in enumerate(ranked_authors, start=1):
        print(f"{index}. {author}")
        print(f"   Commits: {stats['commits']}")
        print(f"   Additions: {stats['additions']}")
        print(f"   Deletions: {stats['deletions']}")
        print(f"   Files Changed: {stats['files_changed']}")
        print(f"   Contribution Score: {stats['score']}")
        print()


def main():
    owner = input("Enter repo owner: ").strip()
    repo = input("Enter repo name: ").strip()

    commits = get_commits(owner, repo)

    if not commits:
        print("No commits found or unable to fetch commits.")
        return

    ranked_authors = analyze_contributors(owner, repo, commits)

    if not ranked_authors:
        print("No contributor data available.")
        return

    print_ranking(ranked_authors)

    save_report_to_markdown(owner, repo, ranked_authors)


if __name__ == "__main__":
    main()
