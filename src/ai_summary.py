def generate_summary(author, stats):
    commits = stats["commits"]
    additions = stats["additions"]
    deletions = stats["deletions"]
    files = stats["files_changed"]

    summary = f"{author} has made {commits} commits with {additions} additions and {deletions} deletions across {files} files."

    if commits > 5:
        summary += " This contributor appears to be highly active."
    else:
        summary += " This contributor has limited activity."


    return summary