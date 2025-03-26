#!/usr/bin/env python
# coding: utf-8

import os
import glob
from QuartoPreprocessor import *

if __name__ == "__main__":
    cwd = os.getcwd()
    
    papers_to_pubs = PapersToMarkdown(os.path.join(cwd, "research", "publications", "papers.yaml"),
                                      os.path.join(cwd, "publications.qmd"))

