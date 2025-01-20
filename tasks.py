# -*- coding: utf-8 -*-

import datetime
import os
import shlex
import shutil

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS |= DEFAULT_CONFIG
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    "github_pages_branch": "master",
    "username": "girisagar46",
    "blog_repo": "girisagar46.github.io.git",
    "commit_message": f"'Publish site on {datetime.date.today().isoformat()}'",
    "host": "localhost",
    "port": 8000,
    "GH_TOKEN": os.getenv("GH_TOKEN"),
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
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def serve(ctx):
    """`build`, then `serve`"""
    ctx.run("pelican -r -s {settings_base} --listen".format(**CONFIG))


@task
def publish(c):
    """Publish to production via rsync"""
    pelican_run("-s {settings_publish}".format(**CONFIG))
    print("Invoking gph-import.")
    c.run(
        "ghp-import -m {commit_message} -b {github_pages_branch} {deploy_path}".format(
            **CONFIG
        )
    )
    print("Pushing to master...")
    c.run(
        "git push -fq https://{username}:{GH_TOKEN}@github.com/{username}/{blog_repo} {github_pages_branch}".format(
            **CONFIG
        )
    )


@task
def publish_locally(c):
    """Publish to GitHub Pages"""
    clean(c)
    pelican_run("-s {settings_publish}".format(**CONFIG))
    c.run(
        "ghp-import -m {commit_message} -b {github_pages_branch} {deploy_path}".format(
            **CONFIG
        )
    )
    c.run("git push -u origin {github_pages_branch}".format(**CONFIG))


@task
def gh_pages(c):
    """Publish to GitHub Pages"""
    c.run(
        "ghp-import -b {github_pages_branch} "
        "-m {commit_message} "
        "{deploy_path} -p".format(**CONFIG)
    )


def pelican_run(cmd):
    cmd += f" {program.core.remainder}"
    pelican_main(shlex.split(cmd))


@task
def new_post(c, title):
    """
    creates new post
    Usage: $ invoke new-post title="My Brand New Awesome Post"
    :param title: Title of the blog post
    :return:
    """
    today = datetime.datetime.now()
    post_title = title.split("=")[1]
    slug = post_title.lower().strip().replace(" ", "-")
    file_location = f"content/articles/{slug}.md"
    template = TEMPLATE.strip().format(
        title=post_title,
        year=today.year,
        month=today.month,
        day=today.day,
        hour=today.hour,
        minute=today.minute,
        slug=slug,
    )

    with open(file_location, "w") as output_article:
        output_article.write(template)
