import os
import subprocess

def count_files_in_directory(directory):
    """Count the total number of files in the directory."""
    total_files = sum(len(files) for _, _, files in os.walk(directory))
    return total_files - 2

def git_automation():
    """Automate git commands and print file count."""
    # Get the current directory
    current_directory = os.getcwd()

    # Count total files in the directory
    total_files = count_files_in_directory(current_directory)
    print(f"Total files in the directory - 2: {total_files}")

    # Execute git commands
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Daily Practice"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Git commands executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git commands: {e}")

if __name__ == "__main__":
    git_automation()
