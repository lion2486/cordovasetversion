  GNU nano 3.2                                       increaseVersion.py                                                 
from getVersion import getVersion
from setcordovaversion import setVersionAndBuildNumbers
import semver
import sys

def increaseVersion(filename, level):
        ver = getVersion(filename)
        sem = semver.VersionInfo.parse(ver)
        if level == 'patch':
                sem = sem.bump_patch()
        elif level == 'minor':
                sem = sem.bump_minor()
        elif level == 'major':
                sem = sem.bump_major()
        else:
                print 'The level of semver part to increase was not in (major, minor, patch)'
                exit(1)

        # TODO also cover build increase later
        setVersionAndBuildNumbers(sem.__str__(), '1', filename)

if __name__ == "__main__":
        # execute only if run as a script
        increaseVersion(sys.argv[1], sys.argv[2])
        # TODO add some CLI help text and validation
