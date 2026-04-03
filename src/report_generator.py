from src.ai_summary import generate_summary


def save_report_to_markdown(owner, repo, ranked_authors):
    file_name = "report.md"

    with open(file_name, "w", encoding="utf-8") as report_file:
        report_file.write("# GitHub Contribution Report\n\n")
        report_file.write("## Repository\n")
        report_file.write(f"{owner}/{repo}\n\n")
        report_file.write("## Contributor Ranking\n\n")

        for index, (author, stats) in enumerate(ranked_authors, start=1):
            report_file.write(f"### {index}. {author}\n")
            report_file.write(f"- Commits: {stats['commits']}\n")
            report_file.write(f"- Additions: {stats['additions']}\n")
            report_file.write(f"- Deletions: {stats['deletions']}\n")
            report_file.write(f"- Files Changed: {stats['files_changed']}\n")
            report_file.write(f"- Contribution Score: {stats['score']}\n\n")

            summary = generate_summary(author, stats)
            report_file.write(f"- AI Summary: {summary}\n\n")

    print(f"Report saved to {file_name}")
