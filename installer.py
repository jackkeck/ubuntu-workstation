import ConfigParser
import os


############################
############################
## USER DEFINED SETTINGS  ##
############################
############################

print "..."
print "..."
print "GRABBING USER SETTINGS"
print "..."

config = ConfigParser.ConfigParser()
config.read("configurations/user.configuration")

gitEmailAddress = config.get('GitHub','gitEmailAddress')
print "gitEmailAddress: "+gitEmailAddress

gitUserName = config.get('GitHub','gitUserName')
print "gitUserName: "+gitUserName

sublimeLicense = config.get('SublimeText','sublimeLicense')
if sublimeLicense == "licensed": 
	print "Sublime license found and will install registered version"
else:
	print "No sublime license found and free, Unregistered version will be installed. cheap bastard"

############################
############################
## GIT INSTALL AND CONFIG ##
############################
############################

print "..."
print "..."
print "INSTALLING GIT"
print "..."

print os.system("sudo apt-get update")
print os.system("sudo apt-get install git")

gitEmailReturn = os.system("git config --global user.email "+gitEmailAddress)
if gitEmailReturn == 0:
	print "Configured git with email: "+gitEmailAddress
else:
	print "Failed to configure git email"

gitUSerReturn = os.system("git config --global user.name "+gitUserName)

if gitUSerReturn == 0:
	print "Configured git with user: "+gitUserName
else:
	print "Failed to configure git user"

############################
############################
## SUBLIME INSTALL #########
############################
############################

print "..."
print "..."
print "INSTALLING SUBLIME TEXT 3"
print os.system("sudo add-apt-repository ppa:webupd8team/sublime-text-3")
print os.system("sudo apt-get update")
print os.system("sudo apt-get install sublime-text-installer")
if sublimeLicense == "licensed":
	os.system("cp -u configurations/License.sublime_license ~/.config/sublime-text-3/Local")
	print "Added license for sublime text"
else:
	print "Installed your free copy of Sublime, you thieving scallywag"

print "..."
print "..."
print"Installer completed"



