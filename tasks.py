# -*- coding: utf-8 -*-

import datetime
import os
import shlex
import shutil
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Github Pages configuration
    'github_pages_branch': 'master',
    'username': 'girisagar46',
    'blog_repo': 'girisagar46.github.io.git',
    'commit_message': "'Publish site on {}'".format(datetime.date.today().isoformat()),
    # Host and port for `serve`
    'host': 'localhost',
    'port': 8000,
    'GH_TOKEN': os.getenv('GH_TOKEN')
}

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


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])


@task
def build(c):
    """Build local version of site"""
    pelican_run('-s {settings_base}'.format(**CONFIG))


@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run('-d -s {settings_base}'.format(**CONFIG))


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run('-r -s {settings_base}'.format(**CONFIG))


@task
def serve(c):
    """Serve site at http://$HOST:$PORT/ (default is localhost:8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        (CONFIG['host'], CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving at {host}:{port} ...\n'.format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    pelican_run('-s {settings_publish}'.format(**CONFIG))


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured host and port
    server.serve(host=CONFIG['host'], port=CONFIG['port'], root=CONFIG['deploy_path'])


@task
def publish(c):
    """Publish to production via rsync"""
    pelican_run('-s {settings_publish}'.format(**CONFIG))
    print("Invoking gph-import.")
    c.run("ghp-import -m {commit_message} -b {github_pages_branch} {deploy_path}".format(**CONFIG))
    print("Pushing to master...")
    c.run("git push -fq https://{username}:{GH_TOKEN}@github.com/{username}/{blog_repo} {github_pages_branch}".format(
        **CONFIG))


@task
def publish_locally(c):
    """Publish to GitHub Pages"""
    clean(c)
    pelican_run('-s {settings_publish}'.format(**CONFIG))
    c.run("ghp-import -m {commit_message} -b {github_pages_branch} {deploy_path}".format(**CONFIG))
    c.run("git push -u origin {github_pages_branch}".format(**CONFIG))


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    preview(c)
    c.run('ghp-import -b {github_pages_branch} '
          '-m {commit_message} '
          '{deploy_path} -p'.format(**CONFIG))


def pelican_run(cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))


@task
def new_post(c, title, *args, **kwargs):
    """
    creates new post
    Usage: $ fab new_post:"post title"
    :param title: Title of the blog post
    :return:
    """
    today = datetime.datetime.today()
    slug = title.split("=")[1].lower().strip().replace(' ', '-')
    file_location = "content/articles/{}.md".format(slug)
    template = TEMPLATE.strip().format(title=title,
                                       year=today.year,
                                       month=today.month,
                                       day=today.day,
                                       hour=today.hour,
                                       minute=today.minute,
                                       slug=slug)
    with open(file_location, 'w') as output_article:
        output_article.write(template)
