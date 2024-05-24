import subprocess
import time

def merge_branches():
    # Fetch the latest changes from the remote repository
    subprocess.run(["git", "fetch", "origin"])

    # Checkout to the Ink branch
    subprocess.run(["git", "checkout", "Ink"])

    # Get the latest commit hashes for main and Ink branches
    main_hash = subprocess.check_output(["git", "rev-parse", "origin/main"]).strip()
    ink_hash = subprocess.check_output(["git", "rev-parse", "origin/Ink"]).strip()

    # Check if the main branch has new commits compared to Ink branch
    if main_hash != ink_hash:
    
        # Pull latest changes from main
        subprocess.run(["git", "pull", "origin", "main"])
        
        # Merge main into Ink
        subprocess.run(["git", "merge", "main"])
        
        # Push changes to the Ink branch
        subprocess.run(["git", "push", "origin", "Ink"])
        print("Merged changes from main into Ink branch.")
    else:
        print("No new changes in main branch.")

if __name__ == "__main__":
    while True:
        merge_branches()
        # Sleep for 5 minutes before checking for updates again
        time.sleep(300)  # 5 minutes in seconds
# done