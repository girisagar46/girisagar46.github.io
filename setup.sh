#!/usr/bin/env bash

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

git clone https://github.com/girisagar46/girisagar46.github.io-theme.git themes/girisagar46.github.io-theme

git clone --recursive https://github.com/getpelican/pelican-plugins
