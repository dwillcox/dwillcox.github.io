#!/usr/bin/env python
# coding: utf-8

import os
import glob
from Publisher.Publisher import *

if __name__ == "__main__":
    # About directories, this is intended to be executed from the root
    # website directory where the Makefile lives.
    #
    # The directory where the Makefile lives is the current working directory.
    #
    # Get current working directory
    cwd = os.getcwd()

    # Make a YAML Reader to help us read website source files.
    reader = ReaderYAML()

    # Get Webpage configuration data from all YAML files in source directory
    config = reader.glob(os.path.join(cwd, "source"))

    # Read Webpage Sequence specification from YAML file in content directory
    sequence_path = os.path.join(cwd, "source", "webpage.yaml")

    # Construct Sequence
    sequence = Sequence.from_path(sequence_path)

    # Identify HTML template(s) for the website
    templates = glob.glob(os.path.join(cwd, "source", "*.j2"))

    # Render Webpages from Sequence
    with Webpage(sequence) as webpage:
        with webpage.using_sequence(sequence) as webpage:
            with webpage.using_config(config) as webpage:
                for template in templates:
                    with webpage.using_template(template) as webpage:
                        webpage.render_html()

