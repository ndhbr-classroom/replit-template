import os

# Write bash aliases
f = open("../.bash_aliases", "w")
f.writelines([
    "alias get='bash replit-template/get'",
    "\nalias submit='bash replit-template/submit'",
    "\nalias test='bash replit-template/test'"
])
f.close()

# Add git keys
sshPath = "../.ssh"
try:
  # Create ssh folder
  if not os.path.isdir(sshPath):
    os.mkdir(sshPath)
except OSError:
  print ("Creation of the directory %s failed" % sshPath)
else:
  # Private ssh key
  f = open("%s/id_rsa" % sshPath, "w")
  f.write(os.getenv("private_ssh_key"))
  f.close()

  # Public ssh key
  f = open("%s/id_rsa.pub" % sshPath, "w")
  f.write(os.getenv("public_ssh_key"))
  f.close()