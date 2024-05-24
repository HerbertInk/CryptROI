import subprocess

def merge_branches():
    # Checkout to the ink branch
    subprocess.run(["git", "checkout", "ink"])
    
    # Pull latest changes from main
    subprocess.run(["git", "pull", "origin", "main"])
    
    # Merge main into ink
    subprocess.run(["git", "merge", "main"])
    
    # Push changes to the ink branch
    subprocess.run(["git", "push", "origin", "ink"])

if __name__ == "__main__":
    merge_branches()
# done