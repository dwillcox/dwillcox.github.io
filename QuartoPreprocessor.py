#!/usr/bin/env python
# coding: utf-8

import os
import yaml

class TalksToMarkdown:
    def __init__(self, talks_yaml, talks_md):
        """
        # Read talks yaml file and convert it into a Quarto markdown file

        Expects paths to talks_yaml and talks_md as arguments, will create the latter.
        """

        try:
            assert(os.path.isfile(talks_yaml)), f"Error: must specify valid file path to talks yaml file."
            self.path_yaml = talks_yaml
            self.path_md = talks_md
        except AssertionError as msg:
            print(msg)
            raise
          
        self.do_task()

    def do_task(self):
        yaml_data = {}

        with open(self.path_yaml) as file_yaml:
            yaml_data = yaml.safe_load(file_yaml)
            
        with open(self.path_md, "w") as file_md:
            wl = lambda s="": file_md.write(f"{s}\n")
            
            wl("# Talks")  
            wl()
            
            text = yaml_data["Talks"]["Introduction"]
            wl(f"{text}")
            wl()
            
            wl("## Recorded Talks")
            wl()
            recorded = yaml_data["Talks"]["Recorded"]
            for entry in recorded["entries"]:
                title = entry["title"]
                year = entry["year"]
                location = entry["location"]
                link = entry["link"]
                video = entry["video"]
                
                try:
                    assert video.strip() != "None", f"Error: cannot list a recorded talk without a video embed link."
                except AssertionError as msg:
                    print(msg)
                    raise

                wl(f"### {location}: **{title}**")
                wl()
                video_embed = r"{{< video " + f"{video}" + r" >}}"
                wl(video_embed)
                wl()
            wl()

            wl("## Complete List of Talks")
            wl()

            wl("### Conference Talks / Invited Talks / Seminars")
            wl()
            research = yaml_data["Talks"]["Research"]
            for entry in research["entries"]:
                title = entry["title"]
                year = entry["year"]
                location = entry["location"]
                link = entry["link"]
                video = entry["video"]
                
                wl(f"* {year}: **{title}**")
                wl(f"    + {location}")
            wl()

            wl("### Public Talks")
            wl()
            public = yaml_data["Talks"]["Public"]
            for entry in public["entries"]:
                title = entry["title"]
                year = entry["year"]
                location = entry["location"]
                link = entry["link"]
                video = entry["video"]
                
                wl(f"* {year}: **{title}**")
                wl(f"    + {location}")
            wl()
            
class CVToMarkdown:
    def __init__(self, cv_yaml, cv_md):
        """
        # Read cv yaml file and convert it into a Quarto markdown file

        Expects paths to cv_yaml and cv_md as arguments, will create the latter.
        """

        try:
            assert(os.path.isfile(cv_yaml)), f"Error: must specify valid file path to cv yaml file."
            self.path_yaml = cv_yaml
            self.path_md = cv_md
        except AssertionError as msg:
            print(msg)
            raise
          
        self.do_task()

    def do_task(self):
        yaml_data = {}

        with open(self.path_yaml) as file_yaml:
            yaml_data = yaml.safe_load(file_yaml)
            
        with open(self.path_md, "w") as file_md:
            wl = lambda s="": file_md.write(f"{s}\n")
            
            wl("# CV")  
            wl()
            
            text = yaml_data["CV"]["Introduction"]
            wl(f"{text}")

            wl()
            
            wl("## Most Recent Position")
            wl()
            recent_position = yaml_data["CV"]["Employment"]["MostRecentPosition"]
            for position in recent_position["positions"]:
                ystart = position["ystart"]
                yend = position["yend"]
                title = position["title"]
                division = position["division"]
                location = position["location"]
                wl(f"* {ystart}-{yend}: **{title}**, {division}")
            wl()
            
            division = recent_position["division"]
            location = recent_position["location"]
            address  = recent_position["address"]
            city_state_zip = recent_position["city_state_zip"]

            wl(f"{division}")
            wl()
            wl(f"{location}")
            wl()
            wl(f"{address}")
            wl()
            wl(f"{city_state_zip}")
            wl()
            
            wl("## Academics")

            wl("### Education")
            wl()
            edu = yaml_data["CV"]["Academics"]["Education"]
            for entry in edu["entries"]:
                institution = entry["institution"]
                location = entry["location"]
                wl(f"* {institution} - {location}")
                for achievement in entry["achievements"]:
                    title = achievement["title"]
                    wl(f"    + **{title}**")
            wl()

            wl("### Fellowships")
            wl()
            fls = yaml_data["CV"]["Academics"]["Fellowships"]
            for entry in fls["entries"]:
                ystart = entry["ystart"]
                yend = entry["yend"]
                title = entry["title"]
                institution = entry["institution"]
                wl(f"* {ystart} - {yend}: **{title}**, {institution}")
            wl()

            wl("### Professional Development")
            wl()
            prof_dev = yaml_data["CV"]["Research"]["ProfessionalDevelopment"]
            for entry in prof_dev["entries"]:
                year = entry["year"]
                task = entry["task"]
                wl(f"* {year}: {task}")
            wl()
            
            wl("## Research")
            
            wl("### Funding Proposals")
            wl()
            funding = yaml_data["CV"]["Research"]["FundingProposals"]
            for entry in funding["entries"]:
                year = entry["year"]
                status = entry["status"]
                authorship = entry["authorship"]
                institution = entry["institution"]
                coauthors = entry["coauthors"]
                name = entry["name"]
                wl(f"* {year}: *({status})* **{name}**")
                wl(f"    + role: {authorship}")
                if coauthors.strip() != "":
                    wl(f"    + collaborators: {coauthors}")
                wl(f"    + institution: {institution}")
            wl()

            wl("### Computing Time Awards")
            wl()
            cta = yaml_data["CV"]["Research"]["ComputingTimeAwards"]
            for entry in cta["entries"]:
                year = entry["year"]
                authorship = entry["authorship"]
                institution = entry["institution"]
                name = entry["name"]
                status = entry["status"]
                wl(f"* {year}: {authorship}, {institution}, *{name}* (**{status}**)")
            wl()

            wl("### Scientific Software")
            wl()
            scisw = yaml_data["CV"]["Research"]["ScientificSoftware"]
            for entry in scisw["entries"]:
                year = entry["year"]
                desc = entry["description"]
                link = entry["link"]
                wl(f"* {year}: {desc}")
                wl(f"    + [{link}]({link})")
            wl()

            wl("### Research Advising")
            wl()
            adv = yaml_data["CV"]["Research"]["ResearchAdvising"]
            for entry in adv["entries"]:
                year = entry["year"]
                name = entry["name"]
                role = entry["role"]
                wl(f"* {year}: {name}")
                wl(f"    + {role}")
            wl()

            wl("### Professional Service")
            wl()
            serv = yaml_data["CV"]["Research"]["ProfessionalService"]
            for entry in serv["entries"]:
                year = entry["year"]
                task = entry["task"]
                wl(f"* {year}: {task}")
            wl()
            
            wl("## Outreach and Teaching")

            wl("### Community Outreach")
            wl()
            prof_dev = yaml_data["CV"]["TeachingAndOutreach"]["CommunityOutreach"]
            for entry in prof_dev["entries"]:
                year = entry["year"]
                task = entry["task"]
                wl(f"* {year}: {task}")
            wl()
            
            wl("### Teaching Experience")
            wl()
            teaching = yaml_data["CV"]["TeachingAndOutreach"]["TeachingExperience"]
            for entry in teaching["entries"]:
                institution = entry["institution"]
                courses = entry["courses"]
                wl(f"* *{institution}*")
                for course in courses:
                    year = course["year"]
                    name = course["name"]
                    description = course["description"]
                    wl(f"    + {year}: **{name}**")
                    wl(f"        - {description}")
            wl()
      

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
            wl(r"lightbox: true")
            wl(r"---")
            wl()
            wl(r"# Publications")
            wl()
            wl(r"As my publication record illustrates, I prefer to research by collaborating with other scientists.")
            wl()
            wl(r"## Publication Listings")
            wl()
            wl(r"[Publications (PDF)](research/publications/willcox_publications.pdf)")
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
                curly_contents = r"group=\"pub-gallery\""
                if "JOSS" in figure_relpath:
                    curly_contents += r" width=50%"
                line = f"![{caption}\nDOI: [{link}]({link})]({figure_relpath} \"{caption}\")" + r"{" + f"{curly_contents}" + r"}"
                wl(line)
                wl()
                wl(f"{authors}")
                wl()
                wl(f"{year}, {journal}")
                wl()
                wl(f"[{link}]({link})")
                wl()

