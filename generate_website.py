#!/usr/bin/env python
# coding: utf-8

import os
import glob
from Publisher.Publisher import *
from Publisher.Preprocessor import *

if __name__ == "__main__":
    # About directories, this is intended to be executed from the root
    # website directory where the Makefile lives.
    #
    # The directory where the Makefile lives is the current working directory.
    
    # PRELIMINARIES

    ## Get current working directory
    cwd = os.getcwd()
    
    # CREATE ANY DEPENDENCIES FOR THE WEBSITE SEQUENCE SPECIFICATION

    ## Create publications list markdown file from paper YAML database
    papers_to_pubs = PapersToPubList(os.path.join(cwd, "research", "publications", "papers.yaml"),
                                     os.path.join(cwd, "source", "publications.md"))

    # READ WEBSITE SOURCE FILES

    ## Make a YAML Reader to help us read website source files.
    reader = ReaderYAML()

    ## Get Webpage configuration data from all YAML files in source directory
    config = reader.read(os.path.join(cwd, "source", "contact.yaml"))

    # BUILD SEQUENCE

    ## Read Webpage Compendium specification from YAML file in content directory
    ssf = SceneSetFactory()
    compendium_path = os.path.join(cwd, "source", "webpage.yaml")

    ## Construct Content
    content = ssf.from_path(compendium_path)

    # RENDER WEBSITE

    ## Identify HTML template(s) for the website
    templates = glob.glob(os.path.join(cwd, "source", "html5up-readonly", "*.j2"))

    ## Render Webpages from Sequence
    render_log = Log("render_log.json")
    with Webpage(log=render_log) as webpage:
        with webpage.using_content(content) as webpage:
            with webpage.using_config(config) as webpage:
                for template in templates:
                    with webpage.using_template(template) as webpage:
                        webpage.render_html()
    render_log.save()
