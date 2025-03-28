#!/usr/bin/env python
# coding: utf-8

import os
import glob
from QuartoPreprocessor import *

if __name__ == "__main__":
    cwd = os.getcwd()
    
    mkpapers = PapersToMarkdown(os.path.join(cwd, "research", "publications", "papers.yaml"),
                                os.path.join(cwd, "publications.qmd"))
    
    mkcv = CVToMarkdown(os.path.join(cwd, "research", "cv", "cv.yaml"),
                        os.path.join(cwd, "cv.qmd"))

    mktalks = TalksToMarkdown(os.path.join(cwd, "research", "talks", "talks.yaml"),
                              os.path.join(cwd, "talks.qmd"))
