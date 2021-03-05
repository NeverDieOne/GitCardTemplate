from jinja2 import Environment, FileSystemLoader


def get_commits(commits):
    commit_template = env.get_template('commits/commit.html')
    commits_list_template = env.get_template('commits/commits_list.html')

    commits_html = [commit_template.render({'text': commit}) for commit in commits]

    with open('commits.html', 'w') as f:
        f.write(commits_list_template.render({'commits': commits_html}))


def get_files(files):
    file_template = env.get_template('files/file.html')
    files_list_template = env.get_template('files/files_list.html')

    files_html = [file_template.render({'filename': filename, 'commit': commit}) for filename, commit in files]

    with open('files.html', 'w') as f:
        f.write(files_list_template.render({'files': files_html}))


if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('templates')
    )

    # Здесь просто список из коммитов
    commits = ['Шаг 5 - выполнено', 'Init commit', 'Add function to calculate salary']

    # Здесь файл + коммит к нему (можно в будущем сделать рандом для коммитов чтоб не париться)
    default_commit = 'Init commit'
    files = [('main.py', default_commit), ('.gitignore', default_commit), ('.env', default_commit)]

    get_commits(commits)
    get_files(files)
