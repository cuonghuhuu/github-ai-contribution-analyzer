def generate_summary(author, stats):
    commits = stats["commits"]
    additions = stats["additions"]
    deletions = stats["deletions"]
    files = stats["files_changed"]

    summary = (
        f"{author} đã thực hiện {commits} commit, tác động tới {files} file, "
        f"với {additions} dòng thêm và {deletions} dòng xóa."
    )

    if commits > 5:
        summary += " Contributor này có mức độ hoạt động nổi bật và đóng góp khá đều."
    else:
        summary += " Contributor này hiện có mức độ hoạt động còn khá hạn chế."

    return summary
