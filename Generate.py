#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import yaml
from jinja2 import Environment, FileSystemLoader


# In[2]:


# Load YAML configuration data
config = {}
config_dir = os.path.join(os.getcwd(), "source/config")
config_files = glob.glob(os.path.join(config_dir, "*.yaml"))

for f in config_files:
    file = open(f, "r")
    config = config | yaml.safe_load(file)


# In[3]:


config


# In[4]:


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
        
        self.read(filename)
        self.sanity()
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


# In[5]:


# Load all markdown files to process
md_dir = os.path.join(os.getcwd(), "source/markdown")
md_files = glob.glob(os.path.join(md_dir, "*.md"))

markdown = [MarkDownFile(mdf) for mdf in md_files]


# In[7]:


# Iterate over markdown files and generate HTML using Jinja2
for md in markdown:
    j2env = Environment(loader=FileSystemLoader("source/templates"))
    j2tmp = j2env.get_template(md.yaml["template"])
    render_yaml = config | md.yaml
    j2out = j2tmp.render(render_yaml)
    output_file = os.path.join(os.getcwd(), md.htmlname)
    with open(output_file, "w") as file:
        file.write(j2out)


# In[ ]:




