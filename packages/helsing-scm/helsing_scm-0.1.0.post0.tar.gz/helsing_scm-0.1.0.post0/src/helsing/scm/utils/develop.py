from pathlib import Path


def get_develop_root() -> Path:
    """
    Returns the path to the root directory of the SCM repository. If SCM is installed as a package instead of in
    develop mode, this function will raise a #ValueError exception.

    The function uses the resolved path of the `helsing.scm` module and checks if it lives in a directory that
    corresponds to the structure of the SCM Git repository.
    """

    from helsing import scm

    source_root = Path(scm.__file__).resolve().parent.parent.parent
    if source_root.name != "src":
        raise ValueError(f"SCM is not installed in develop mode: {source_root}")

    readme = source_root.parent / "README.md"
    if not readme.is_file():
        raise ValueError(f"SCM is not installed in develop mode: {source_root}")

    return source_root.parent


if __name__ == "__main__":
    print(get_develop_root())
