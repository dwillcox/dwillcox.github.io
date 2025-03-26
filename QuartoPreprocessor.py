#!/usr/bin/env python
# coding: utf-8

import os
import yaml

class PapersToMarkdown:
    def __init__(self, paper_yaml, publications_md):
        """
        # Read paper yaml file and convert it into a Quarto publication markdown file.

        Expects to get paths to paper_yaml and publications_md as arguments.

        Will create publications_md if it does not exist.

        Can get absolute paths or paths relative to the current working directory.

        # Expected YAML format for papers file is as follows.

        papers:
          - title:
            authors:
            journal:
            year:
            link:
            figure:
            caption:

          - title:
            authors:
            journal:
            year:
            link:
            figure:
            caption:

          [...]
        """

        try:
            assert(os.path.isfile(paper_yaml)), f"Error: must specify valid file path to paper yaml file."
            self.path_paper = paper_yaml
            self.path_publist = publications_md
        except AssertionError as msg:
            print(msg)
            raise

        self.do_task()


    def do_task(self):
        papers = None

        with open(self.path_paper) as paper_yaml:
            papers = yaml.safe_load(paper_yaml)

        with open(self.path_publist, "w") as pubfile:
            # define helper lambda wl to Write a Line
            wl = lambda s="": pubfile.write(f"{s}\n")
            wl(r"---")
            wl(r"title: Publications")
            wl(r"lightbox: true")
            wl(r"---")
            wl()
            wl(r"# Publications")
            wl()
            wl(r"As my publication record illustrates, I research best by collaborating with other scientists.")
            wl()
            wl(r"## Publication Listings")
            wl()
            wl(r"[Publications (PDF)](research/willcox_publications.pdf)")
            wl()
            wl(r"[Google Scholar Page](https://scholar.google.com/citations?hl=en&user=5Ns_t38AAAAJ)")
            wl()
            wl(r"[Publications on NASA ADS](https://ui.adsabs.harvard.edu/search/fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=(database%3Aastronomy%20OR%20database%3Aphysics)&p_=0&q=author%3A%22willcox%2C%20d.%20e.%22%20year%3A2016-&sort=date%20desc%2C%20bibcode%20desc)")
            wl()
            wl(r"[Preprints on the arXiv](https://arxiv.org/search/astro-ph?searchtype=author&query=Willcox,+D+E)")
            wl()
            wl()
            
            # apply reverse 1-indexed numbering to the paper entries
            npapers = len(papers["papers"])

            for idx, paper in enumerate(papers["papers"]):
                title = paper["title"]
                figure_src = paper["figure"]
                caption = paper["caption"]
                authors = paper["authors"]
                year = paper["year"]
                journal = paper["journal"]
                link = paper["link"]
                
                # recalculate the relative link for the figure source
                # so we write the relative link relative to the location of
                # the markdown file we are writing
                paper_yaml_dir = os.path.dirname(self.path_paper)
                publist_md_dir = os.path.dirname(self.path_publist)
                figure_relpath = os.path.relpath(os.path.join(paper_yaml_dir, figure_src), start=publist_md_dir)

                wl(f"## {npapers-idx}. {title}")
                wl()
                line = f"![{caption}\nDOI: [{link}]({link})]({figure_relpath} \"{caption}\")" + r"{group=\"pub-gallery\"}"
                wl(line)
                wl()
                wl(f"{authors}")
                wl()
                wl(f"{year}, {journal}")
                wl()
                wl(f"[{link}]({link})")
                wl()

