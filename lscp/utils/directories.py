import os
from pathlib import Path


def get_custom_path(*paths: str) -> str:
    return os.path.join(Path(__file__).resolve().parent.parent.parent, "custom", *paths)


def get_data_path(*paths: str) -> str:
    return os.path.join(Path(__file__).resolve().parent.parent, "data", *paths)


def get_build_path(name: str) -> str:
    path = Path(
        os.path.join(Path(__file__).resolve().parent.parent.parent, "build", name)
    )

    path.mkdir(parents=True, exist_ok=True)
    return str(path.resolve())
