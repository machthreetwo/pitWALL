import importlib
import importlib.metadata
import importlib.util
import subprocess
import sys


def test_version_is_single_sourced():
    import pitwall

    # pitwall.__version__ must agree with the version in pyproject.toml
    assert pitwall.__version__ == importlib.metadata.version("pitwall")


def test_package_is_installed_not_just_on_path():
    # Run from a neutral directory: this only works if `pip install -e .` was done.
    result = subprocess.run(
        [sys.executable, "-c", "import pitwall, pathlib; print(pathlib.Path(pitwall.__file__).parent.name)"],
        capture_output=True, text=True, cwd="/" if sys.platform != "win32" else "C:\\",
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "pitwall"


def test_has_dunder_main():
    assert importlib.util.find_spec("pitwall.__main__") is not None


def test_modules_import_without_side_effects(capsys):
    for name in ("pitwall.units", "pitwall.display", "pitwall.sim", "pitwall.standings", "pitwall.storage"):
        importlib.import_module(name)
    assert capsys.readouterr().out == ""  # importing must never print
