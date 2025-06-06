import pytest
from repo_organizer import categorize_files, rename_files, generate_report

def test_categorize_files():
    files = ["script.py", "index.html", "data.csv", "README.md"]
    result = categorize_files(files)
    assert result["Python"] == ["script.py"]
    assert result["HTML"] == ["index.html"]
    assert result["CSV"] == ["data.csv"]
    assert result["Other"] == ["README.md"]

def test_rename_files():
    files = {"Python": ["script.py"], "CSV": ["data.csv"]}
    result = rename_files(files, "new")
    assert result["Python"] == ["new_0.py"]
    assert result["CSV"] == ["new_0.csv"]

def test_generate_report():
    files = {"Python": ["script.py"], "CSV": ["data.csv"]}
    result = generate_report(files)
    assert "Python: 1 files" in result
    assert "CSV: 1 files" in result