from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import socketserver
from datetime import datetime

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path


# Github Pages configuration
env.gp_branch = "master"
env.msg = "blog update"
SERVER = '127.0.0.1'
# Port for `serve`
PORT = 8000

TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute}
Modified: {year}-{month}-{day} {hour}:{minute}
Category:
Tags:
Slug: {slug}
Summary:
Status: draft
"""

def newpost(title):
    """creates new post
	Usage: $ fab newpost:"post title" """
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    file_location = "content/articles/{}.md".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(file_location, 'w') as output_article:
        output_article.write(t)


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

def publish(commit_message):
    env.msg = commit_message
    env.GH_TOKEN = os.getenv('GH_TOKEN')
    env.TRAVIS_REPO_SLUG = os.getenv('TRAVIS_REPO_SLUG')
    clean()
    local('pelican -s publishconf.py')
    with hide('running', 'stdout', 'stderr'):
        local("ghp-import -m '{msg}' -b {gp_branch} {deploy_path}".format(**env))
        local("git push -u origin https://{GH_TOKEN}@github.com/{TRAVIS_REPO_SLUG}.git {gp_branch}".format(**env))
