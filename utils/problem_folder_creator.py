from pathlib import Path
from sys import argv


def _create_solution_file(path: Path) -> None:
    """Creates a solution file with the name solution.py"""
    solution_file = path / "solution.py"
    solution_file.touch()


def _create_test_file(path: Path) -> None:
    """Creates a test file with the name test.py"""
    test_file = path / "test_solution.py"
    test_file.touch()


def _create_readme_file(path: Path) -> None:
    """Creates a readme file with the name README.md"""
    readme_file = path / "README.md"
    readme_file.touch()


def create_problem_folder(difficulty: str, problem_name: str) -> None:
    """Creates a folder with the name of the problem and creates a solution file, a test file and a readme file"""
    difficulty_dir = Path(difficulty).absolute()
    problem_dir = Path(f"{difficulty_dir}/{problem_name}").absolute()

    if not difficulty_dir.exists():
        difficulty_dir.mkdir()

    if not problem_dir.exists():
        problem_dir.mkdir()

    _create_solution_file(problem_dir)
    _create_test_file(problem_dir)
    _create_readme_file(problem_dir)
    print("")
    print(f"Created problem folder for {problem_name} in {difficulty}")


if __name__ == "__main__":
    args = argv

    difficulty = argv[1]
    problem_name = argv[2]

    create_problem_folder(difficulty, problem_name)
