import subprocess

def git_automation():
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
