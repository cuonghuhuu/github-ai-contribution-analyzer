import os

from src.analyzer import analyze_contributors
from src.github_client import get_commits
from src.report_generator import save_report_to_markdown


def print_ranking(ranked_authors):
    print("\n=== Xếp hạng contributor ===\n")

    for index, (author, stats) in enumerate(ranked_authors, start=1):
        print(f"{index}. {author}")
        print(f"   Số commit: {stats['commits']}")
        print(f"   Số dòng thêm: {stats['additions']}")
        print(f"   Số dòng xóa: {stats['deletions']}")
        print(f"   Số file đã thay đổi: {stats['files_changed']}")
        print(f"   Điểm đóng góp: {stats['score']}")
        print()


def get_repo_info():
    repo_owner = os.getenv("REPO_OWNER", "").strip()
    repo_name = os.getenv("REPO_NAME", "").strip()

    if repo_owner and repo_name:
        print(f"Sử dụng repo từ biến môi trường: {repo_owner}/{repo_name}")
        return repo_owner, repo_name

    owner = input("Nhập owner của repo: ").strip()
    repo = input("Nhập tên repo: ").strip()
    return owner, repo


def main():
    owner, repo = get_repo_info()

    commits = get_commits(owner, repo)

    if not commits:
        print("Không tìm thấy commit hoặc không thể lấy dữ liệu commit.")
        return

    ranked_authors = analyze_contributors(owner, repo, commits)

    if not ranked_authors:
        print("Không có dữ liệu contributor khả dụng.")
        return

    print_ranking(ranked_authors)

    save_report_to_markdown(owner, repo, ranked_authors)


if __name__ == "__main__":
    main()
