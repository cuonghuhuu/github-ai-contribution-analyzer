from src.ai_summary import generate_summary


def save_report_to_markdown(owner, repo, ranked_authors):
    file_name = "report.md"

    with open(file_name, "w", encoding="utf-8") as report_file:
        report_file.write("# Báo cáo đóng góp GitHub\n\n")
        report_file.write("## Repo\n")
        report_file.write(f"{owner}/{repo}\n\n")
        report_file.write("## Xếp hạng contributor\n\n")

        for index, (author, stats) in enumerate(ranked_authors, start=1):
            report_file.write(f"### {index}. {author}\n")
            report_file.write(f"- Số commit: {stats['commits']}\n")
            report_file.write(f"- Số dòng thêm: {stats['additions']}\n")
            report_file.write(f"- Số dòng xóa: {stats['deletions']}\n")
            report_file.write(f"- Số file đã thay đổi: {stats['files_changed']}\n")
            report_file.write(f"- Điểm đóng góp: {stats['score']}\n\n")

            summary = generate_summary(author, stats)
            report_file.write(f"- Nhận xét AI: {summary}\n\n")

    print(f"Đã lưu report vào file {file_name}")
