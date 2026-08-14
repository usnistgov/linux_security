import os
from pathlib import Path


def get_data_path(*paths: str) -> str:
    return os.path.join(Path(__file__).resolve().parent.parent, "data", *paths)


def get_build_output(benchmark_name: str = "generic") -> str:
    path = Path(
        os.path.join(
            Path(__file__).resolve().parent.parent.parent, "build", benchmark_name
        )
    )

    path.mkdir(parents=True, exist_ok=True)
    return str(path.resolve())
