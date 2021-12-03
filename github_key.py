import os
print("Copy and paste the following SSH-Key to your GitHub-Account (https://github.com/settings/ssh/new#):")
print(os.getenv("public_ssh_key"))