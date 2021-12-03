import os
print("Copy and paste the following SSH-Key to your GitHub-Account (https://github.com/settings/ssh/new#):")

try:
    f = open("../.ssh/id_rsa.pub", "r")
    print("%s\n" % f.read())
except OSError:
    print("--- KEY NOT FOUND, TRY TO RERUN THE APP ---")