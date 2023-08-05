from pathlib import Path


def get_project_path():
    """
    获取当前项目根路径
    :return: 根路径
    """

    current_path = Path.cwd()
    while True:
        if (current_path / 'requirements.txt').exists():
            return current_path
        parent_path = current_path.parent
        if parent_path == current_path:
            raise Exception("项目根目录未找到")
        current_path = parent_path
    return current_path
