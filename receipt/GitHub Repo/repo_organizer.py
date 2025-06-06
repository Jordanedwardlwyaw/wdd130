import os

def categorize_files(files_list):
    """Sort files into categories based on their extensions."""
    categories = {
        "Python": [],
        "HTML": [],
        "CSV": [],
        "Other": []
    }
    for file in files_list:
        ext = os.path.splitext(file)[1]
        if ext == ".py":
            categories["Python"].append(file)
        elif ext == ".html":
            categories["HTML"].append(file)
        elif ext == ".csv":
            categories["CSV"].append(file)
        else:
            categories["Other"].append(file)
    return categories

def rename_files(files_dict, pattern):
    """Rename files in each category based on a given pattern."""
    renamed_files = {}
    for category, files in files_dict.items():
        renamed_files[category] = [f"{pattern}_{i}{os.path.splitext(f)[1]}" for i, f in enumerate(files)]
    return renamed_files

def generate_report(files_dict):
    """Generate a summary of categorized files."""
    report = "Repository File Summary:\n"
    for category, files in files_dict.items():
        report += f"{category}: {len(files)} files\n"
    return report

def display_options():
    """Provide an interactive menu for selecting actions."""
    print("Options:")
    print("1. Categorize files")
    print("2. Rename files")
    print("3. Generate report")