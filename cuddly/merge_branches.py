import subprocess

def merge_branches():
    # Fetch the latest changes from the remote repository
    subprocess.run(["git", "fetch", "origin"])
    
    # Checkout to the Ink branch
    subprocess.run(["git", "checkout", "Ink"])
    
    # Pull latest changes from main
    subprocess.run(["git", "pull", "origin", "main"])
    
    # Merge main into Ink
    subprocess.run(["git", "merge", "main"])
    
    # Push changes to the Ink branch
    subprocess.run(["git", "push", "origin", "Ink"])

if __name__ == "__main__":
    merge_branches()
# done git fetch origin