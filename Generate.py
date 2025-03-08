#!/usr/bin/env python
# coding: utf-8

import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader


# We will need a class to hold info for each markdown file
class MarkDownFile:
    def __init__(self, filename):
        """
        Initialize class data from filename.
        
        Each markdown file gets to declare local
        YAML data in addition to any global config.
        """
        self.yaml = {}
        self.content = ""
        
        # get the file's basename (no directories)
        self.basename = os.path.basename(filename)
        
        # strip the .md extension
        self.name, extension = os.path.splitext(self.basename)
        assert extension == ".md", f"Error: file {filename} lacks a .md extension!"
        
        # make the html target file basename
        self.htmlname = f"{self.name}.html"
        
        # read the markdown file contents
        self.read(filename)

        # sanity-check the markdown file
        self.sanity()

        # finish packaging the data we have read into class data
        self.package()
    
    def read(self, filename):
        """
        open the filename specified and read data
        allowing for YAML definitions delimited by a
        #yaml pragma in a code block like so:
        
        ```#yaml
        [yaml definitions here]
        ```
        
        Note this is distinct from a code block we consider
        simply part of the markdown like so:
        
        ```yaml
        [example yaml syntax here]
        ```
        
        In the second case, because we do not find the pragma,
        we do not interpret the code block to contain
        YAML definitions for the preprocessor.
        """
        yaml_str = ""
        reading_yaml = False
        
        file = open(filename, "r")
        for line in file:
            if not reading_yaml and line.strip() == "```#yaml":
                reading_yaml = True
            elif reading_yaml and line.strip() == "```":
                reading_yaml = False
            elif reading_yaml:
                yaml_str = yaml_str + line
            else:
                # we are simply reading markdown
                self.content = self.content + line
        file.close()
        
        self.yaml = yaml.safe_load(yaml_str)
        # print(f"File {self.basename} has the following YAML content:")
        # print(self.yaml)
        
    def sanity(self):
        """
        Perform input sanity-checking to verify the markdown file
        specifies everything we will later need.
        """
        assert self.yaml["template"], f"Error: Markdown file {self.basename} did not specify a Jinja2 template in its YAML data."
        
    def package(self):
        """
        Store the markdown within the local YAML dictionary as
        self.yaml["content"].
        """
        self.yaml["content"] = self.content


def get_YAML(yaml_abs_path):
    """
    Get a specific file referenced with an absolute path to a .yaml file.
    """
    data = {}
    with open(yaml_abs_path, "r") as file:
        data = data | yaml.safe_load(file)
    return data


def get_YAML_glob(yaml_rel_path):
    """
    Loops through all *.yaml files in the relative path
    provided as an argument. Returns the database of YAML
    entries as a single Python dictionary.
    """
    # Load YAML data into a Python dictionary
    data_dir = os.path.join(os.getcwd(), yaml_rel_path)
    data_files = glob.glob(os.path.join(data_dir, "*.yaml"))

    data = {}

    # Loop through Configuration files and Read YAML
    for f in data_files:
        data = data | get_YAML(f)

    # Return Dictionary of YAML Data
    return data


def get_mds(md_rel_path):
    """
    Loops through all *.md files in the relative path
    provided as an argument. Returns a list of MarkDownFile
    objects, one object per discovered *.md file.
    """
    # Load all markdown files to process
    md_dir = os.path.join(os.getcwd(), md_rel_path)
    md_files = glob.glob(os.path.join(md_dir, "*.md"))

    # Loop through markdown files and create a list of MarkDownFile objects
    markdown = [MarkDownFile(mdf) for mdf in md_files]

    # Return List of MarkDownFile objects
    return markdown


def j2_md_to_html(global_config_dict, md_list, template_rel_path):
    """
    Loops through MarkDown objects in md_list, converting each
    to an HTML file using Jinja2 to process the corresponding template
    found in template_rel_path based on the global configuration dictionary
    and the individual configuration dictionary associated with each MarkDown object.
    """
    # Uses Jinja2 to process each markdown object in the list
    for md in md_list:
        # Load template file specified by the markdown file's YAML entry
        j2env = Environment(loader=FileSystemLoader(template_rel_path))
        j2tmp = j2env.get_template(md.yaml["template"])

        # Define configuration dictionary for the Jinja2 template rendering
        render_config = global_config_dict | md.yaml

        # Use Jinja2 to render the template and create output HTML data
        j2out = j2tmp.render(render_config)

        # Write output HTML data to an HTML file
        output_file = os.path.join(os.getcwd(), md.htmlname)
        with open(output_file, "w") as file:
            file.write(j2out)


if __name__ == "__main__":
    # Get Global YAML configuration from all YAML files in config directory
    global_data = get_YAML_glob("source/config")

    # Add specific dependencies
    global_data = global_data | get_YAML(os.path.join(os.getcwd(), "files", "papers.yaml"))

    # Get Markdown objects to process into HTML
    markdown = get_mds("source/markdown")

    # Iterate over markdown files and generate HTML using Jinja2
    j2_md_to_html(global_data, markdown, "source/templates")
