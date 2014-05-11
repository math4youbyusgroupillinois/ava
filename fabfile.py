from fabric.api import local
from fabric.api import lcd, local

def deploy():
    with lcd('/home/ladynerd/deploy/ava/'):

        # With git...
        local('git pull /home/ladynerd/projects/ava/')


def prepare_deployment():
    #local('python manage.py test ava_core')
    #local('python manage.py test ava_core_people/tests')
    local('git add -p && git commit') # or local('hg add && hg commit')
