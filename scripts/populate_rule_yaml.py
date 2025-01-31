#
# YAML Rule Producer Script
#
# This script automatically creates and populates yaml files with the requisite data from OpenSCAP reports.
# Create check filename based off of OpenSCAP rule name + category, check if exists, if not, create yaml file in proper folder.
# Add new rule to the rules directory, if the ID exists in the Excel sheet and it has a defined filename.
# Find relevant rule by ID in the CIS or STIG OpenSCAP HTML pages (Pages have a naming convention, this could be a future fix)
# Extract the Rule name, use this for title
# Extract the Rationale, use this for the discussion 
# Extract CCE from References section if existant
# Extract CCIs, 800-53's, SRGs, DISA-STIG, from References section
# Extract severity from Severity section
# Populate tags for 800-53 based off of 800-53 baselines file from mac repo
# Create spaces for OS
# Fill in OS-specific fixes if they exist for shell 

#!/usr/bin/env python3
import openpyxl
import os
import glob
import argparse
import sys
import re
# See comment above line 323 on why I switched from pyyaml
# TODO: ruamel.yaml has switched away from mimicking pyyaml syntax, meaning 0.18 and above break this code.
# It would be nice to make the code work with 0.18, but since I wrote it all for pyyaml and am last-min changing, no time now
import yaml
#import ruamel.yaml as yaml
import time
from pathlib import Path
from bs4 import BeautifulSoup

# Thanks to Reorx Xiao for this code that helps nicely format the yaml dumps!
# I had to get this working with ruamel.yaml but still super handy to have a base
class IndentDumper(yaml.Dumper):
    def increase_indent(self, sequence=True, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

# Compile the provided regex
# Then match it with the target string, and return the first match
# Just a simple helper function
def compile_and_return_first_match(regex,targetstring):
    compiled = re.compile(regex)
    match = compiled.search(targetstring)
    if match is not None:
        return match.group(0)
    else:
        return None
    
# Check if the provided value already exists in the list
# If not, append the value to the list
# Otherwise, do nothing
def unique_append(list,value):
    if list is None:
        list = []
    if value not in list:
        list.append(value)
    # TODO: There are so many wasted cycles on re-sorting here, either do inline sort or one sort at the end
    # Sorting here is super wasteful since we could totally do it at the end, or inline
    # But for now, it doesn't matter
    sort_nicely(list)

# Shamelessly borrowing this function from Bob Gendler :)
# Sort the given list in the way that humans expect.
# Accepts a single list parameter which will be sorted
def sort_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

class multiline(str): pass

# Adopted from this stackoverflow:
# https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data/8641732#8641732
def str_presenter(dumper, data):
    # This is the fix to get rid of block chomping, e.g |- instead of |
    data = data + "\n"
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="|")

def represent_none(self, _):
    return self.represent_sequence('tag:yaml.org,2002:seq', ["N/A"])

yaml.add_representer(type(None), represent_none)

def represent_list(self, data):
    if len(data) < 1:
        return self.represent_sequence('tag:yaml.org,2002:seq', ["N/A"])
    return self.represent_sequence('tag:yaml.org,2002:seq', data)

yaml.add_representer(list, represent_list)

yaml.add_representer(multiline, str_presenter)
# TODO: Is this line needed?
yaml.representer.Representer.add_representer(str, str_presenter)

def main():

    # Get the root directory of the git repo we should be inside of
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Create arguments parser
    parser = argparse.ArgumentParser(description='Use an XLSX file of desired rules from CIS and STIG to create and populate the equivalent yaml files')
    parser.add_argument("--spreadsheet", default=None, help="A full file path to an Excel spreadsheet containing desired rules and names for STIGs and CIS")
    parser.add_argument("--mappings", default=None, help="The local directory in this repo to search for relevant OS mapping guides, in the form of ssg-OS-guide-cis and ssg-OS-guide-stig")
    parser.add_argument("--outputdir", default="/testrules", help="The directory this script will create populated rule files in. It should not overwrite existing rules, but use caution anyways.")

    try:
        # Parse our arguments 
        results = parser.parse_args()
        print("Using the spreadsheet at this path: " + results.spreadsheet)
        print("Loading SSG guide files from this directory: " + str(results.mappings))
        print(f"Using {results.outputdir} as the output directory for newly generated yaml files")
    except IOError as msg:
        # TODO: This really should be cleaner error handling
        parser.error(str(msg))

    # Attempt to load the working XLSX spreadsheet which we've specified the path to in args
    # Load the workbook
    try:
        workbook = openpyxl.load_workbook(results.spreadsheet)
    except FileNotFoundError as err:
        # TODO: Does this cover other exceptions besides just the file not existing?
        # TODO: Make this error handling better and more verbose for end users
        print("Error loading the spreadsheet. Exiting...")
        sys.exit(-1)

    # Select the active sheet
    sheet = workbook.active

    # Load OpenSCAP files in mappings directory
    # The filename pattern is ssg-(osname)(osmajorversion)-guide-(stig or cis)-(variants).html
    # We can infer the relevant OS info for the yaml file from this
    # Thanks Bob for writing the yaml os versions to be raw nums, the same as the SSG format :)
    # The main reason I'm using a dictionary here is just so that I can associate each HTML's content with the OS name and guide type,
    # Rather than having to do some beautifulsoup magic to pull it out or something like that.
    # Not the most efficient way of doing it.. maybe a future TODO!
    ssg_controls_dictionary = {}

    # Defining resources path
    resources_path = root_dir + "/resources"

    # Starting a timer to see how long it takes to generate all these rules (could definitely be made more efficient)
    # One big improvement, initializing BeautifulSoup for each site only once, and then storing it in the dict
    start_time = time.time()

    # TODO: Didn't realize this but when I changed this to glob so that it wouldn't grab random non HTML files, it made the 
    # ssg_control_file not just the filename, but the path. Should fix later when doing refactor
    for ssg_control_file in glob.iglob(f"{resources_path}/*.html"):
        # Determine all OS variants in play, by listing all files and doing prefix comparisons
        # Essentially, we need to look through the files, find every rhel8, rhel9, ubuntu2204, etc guide
        # Then, we need to pick out the one we'd like to use, and load that one into the dictionary.
        # The question becomes, how do we decide which one to use? 
        # For STIG, there are only two variants, STIG and STIG_GUI. STIG_GUI primarily removes controls relating to the X windowing system.
        # For CIS, there are a few variants, Level 1 and Level 2, of both workstation and server. 
        # For now, we'll make the decision to follow the mac security way of doing it.
        # We will add every rule we can, and tag them according to the following:
        # - If the rule exists in STIG_GUI or a CIS Workstation, we will tag it client (consider changing this to workstation?).
        # - If the rule exists in STIG or a CIS Server, we will tag it server.
        # - If a rule exists in any of the STIGs, we will tag it stig.
        # - If the rule exists in CIS Level 1, we will tag it cis_lvl1
        # - If the rule exists in CIS Level 2, we will tag it cis_lvl2.
        # - If the rule exists in any of the CIS, we will tag it cis.
        # In theory, this could result in dictionary collisions if we did normal prefix comparisons.
        # To resolve this, we will use the second split and the last split, concatenated together. 
        ssg_file_path = os.path.join(resources_path,ssg_control_file)
        try:
            with open(ssg_file_path, 'r', encoding='utf-8') as file:
                print(f"Saving into SSG dictionary with the key {os.path.basename(ssg_file_path)}") 
                ssg_controls_dictionary[os.path.basename(ssg_file_path)] = BeautifulSoup(file.read(),"lxml")
                print(f"Successfully found and loaded SSG HTML file: {ssg_file_path}")
        except Exception:
            # TODO: More advanced error reporting
            print(f"Unable to load SSG HTML file: {ssg_file_path}")


    # Change to rules dir to begin creating test rules
    os.chdir(root_dir)

    # Load NIST 800-53 yaml
    with open(root_dir + "/includes/800-53_baselines.yaml",'r') as file:
        nist_yaml = yaml.safe_load(file)

    # Iterate through each row in our spreadsheet
    valid_rules=0
    # Count successful populations
    populated_rules = 0
    # Skip the first row as this is the column titles
    for row in sheet.iter_rows(min_row=2,values_only=True):
        # Look for rows with a valid name set AND a valid CIS or STIG rule
        if row[0] and (row[2] or row[4]):
            # In our sheet, column 1 is the full file name, column 2 is the type (os, audit, etc), and column 3 and 5 are the relevant CIS and STIG IDs. 
            filepath=Path(os.getcwd() + "/rules/" + row[1] + "/" + row[0])
            yaml_dict=dict(
                id = "",
                title = "",
                discussion = "",
                check = multiline("$OS_VALUE"),
                result = {"integer":1},
                fix = multiline("$OS_VALUE"),
                references={
                    "cce":multiline("$OS_VALUE"),
                    "cci":[],
                    "800-53r5":[],
                    "srg":[],
                    "disa_stig":multiline("$OS_VALUE"),
                    "cis":{
                        "benchmark":multiline("$OS_VALUE")
                    },
                },
                tags = [],
                severity = "",
                os_specifics = {},
            )
            if not filepath.is_file():
                print(f"{row[0]} does not exist.")
                # Grab the data from the HTML file dictionary for each, and propogate it into the yaml file we need to create
                # TODO: at some point down the road might be nice to not have to search the entire file each time, maybe preload it into a data structure
                # TODO: this thing is slow!! (but, it's searching through n number of html files, not a huge surprise)
                # This sets the control ID to be the CIS one, if no CIS one, set to STIG, since one must exist
                # (In our schema, both columns contain SSG-type rules, so defaulting to CIS is fine if both exist)
                control_id = row[2] if row[2] else row[4]
                for name, ssg_html in ssg_controls_dictionary.items():
                    # Try and find the tr item in each based off the ID we want.
                    soup = ssg_html
                    # TODO: This is all repetitive data grabbing that probably doesn't need to happen. 
                    # TODO: In theory, all the files should have the same CCI's etc as well. 
                    control = soup.find("tr", {"data-tt-id":control_id})
                    if control:
                        # Define the os specifics category here, since we don't care if it doesn't have the control :)
                        os_blob = name.split("-")[1]
                        os_title = compile_and_return_first_match(r"[a-z]+",os_blob)
                        os_version = compile_and_return_first_match(r"\d+",os_blob)
                        cis_level = compile_and_return_first_match(r"level\d{1}",name)
                        cis_type = compile_and_return_first_match(r"(server|workstation){1}",name)
                        stig_type = compile_and_return_first_match(r"(stig_gui|stig){1}",name)
                        if os_title not in yaml_dict["os_specifics"].keys():
                            yaml_dict["os_specifics"][os_title] = {}
                        if os_version not in yaml_dict["os_specifics"][os_title].keys():
                            yaml_dict["os_specifics"][os_title][os_version] = {}
                        yaml_dict["os_specifics"][os_title][os_version] = {"references":{"cce":[],"disa_stig":[]},"check":None,"fix":None}
                        yaml_dict["id"] = row[0].split(".")[0]
                        # In theory, all of these values should be the same for every rule. If they are not, we will let the user know.
                        print(f"{control_id} is defined in SSG {name}.")
                        # Now we need to extract relevant information from it.
                        # Let's start with the title, as the id is already defined
                        title = control.find("h4")
                        if title:
                            yaml_dict["title"] = title.get_text().split("\n")[1].strip()
                            #print(f"Control Title is {title.get_text().split("\n")[1].strip()}")
                        #Now let's grab the discussion (labeled as rationale)
                        discussion = control.find(class_="rationale")
                        if discussion:
                            yaml_dict["discussion"] = multiline(discussion.get_text(strip=False))
                            #print(f"Control Discussion field is {discussion.get_text(strip=True)}")
                        # And the severity
                        severity = control.find(class_="severity")
                        if severity:
                            yaml_dict["severity"] = severity.get_text(strip=True)
                            #print(f"Control Severity field is {severity.get_text(strip=True)}")
                        # Let's add tags based on the kind of SSG this is
                        # TODO: This maybe could/should be done with the content, rather than the title, as the title can be changed
                        if cis_level:
                            if cis_level == "level1":
                                unique_append(yaml_dict["tags"],"cis_lvl1")
                            elif cis_level == "level2":
                                unique_append(yaml_dict["tags"], "cis_lvl2")
                            else:
                                print("WARNING: THIS STATEMENT SHOULD NOT BE REACHED WITH ACCURATE PARSING.")
                        if cis_type:
                            if cis_type == "server":
                                unique_append(yaml_dict["tags"],"server")
                            elif cis_type == "workstation":
                                unique_append(yaml_dict["tags"],"client")
                        if stig_type:
                            unique_append(yaml_dict["tags"],"stig")
                            if stig_type == "stig":
                                unique_append(yaml_dict["tags"],"server")
                            elif stig_type == "stig_gui":
                                unique_append(yaml_dict["tags"], "client")
                        # Now for the fun part! Grabbing the various CCIs, STIGs, and 800-53's from identifiers
                        identifiers = control.find(class_="identifiers")
                        if identifiers:
                            # We'll need to process this, split out the right ones, and place them into the file
                            # You might be wondering why I'm using re.compile rather than just the letter a.
                            # This is because in SSG files, specifically RHEL ones, the CCE field is an "addr" tag, not an "a" tag.
                            # But guess what letter both start with? :)
                            for identifier in identifiers.find_all(re.compile("^a")):
                                # Let's get the actual text, without the tags and such
                                # Technically, if we wanted to be really sure that each match was right, we could check the HREFs of the a tags instea
                                # Since every single CCI should go to the CCI site, 800-53r5 to NIST, et cetera
                                # But I've taken a look at the current dataset and am making the execute decision that this isn't necessary at this time.
                                # TODO: Maybe a future idea?
                                raw_identifier = identifier.get_text(strip=True)
                                yaml_references = yaml_dict["references"]
                                yaml_os_specificrefs = yaml_dict["os_specifics"][os_title][os_version]["references"]
                                ccematch = compile_and_return_first_match(r"CCE\-\d{5}\-\d{1}", raw_identifier)
                                if ccematch:
                                    # We have a CCE match!
                                    # Since these are OS-specific, let's place them in the specific subsection for the OS this guide references from
                                    unique_append(yaml_os_specificrefs["cce"],ccematch)
                                    continue
                                srgmatch = compile_and_return_first_match(r"SRG\-OS\-\d{6}\-GPOS\-\d{5}", raw_identifier)
                                if srgmatch:
                                    # We have an SRG match!
                                    unique_append(yaml_references["srg"],srgmatch)
                                    continue
                                # Turns out there are a LOT of items that look weirdly similar to the 800-53s... such as DE.AE-2
                                nistmatch = compile_and_return_first_match(r"^[A-Z]{2}\-\d{1,2}(?:\.\d{1,2})?(?:\(\w{1,3}\))?$", raw_identifier)
                                if nistmatch:
                                    # We have an 800-53 match!
                                    unique_append(yaml_references["800-53r5"],nistmatch)
                                    # For these, since we have 800-53r5 scorings as well, we'll want to calculate those here as well.
                                    if nistmatch in nist_yaml["low"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_low")
                                    if nistmatch in nist_yaml["moderate"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_moderate")
                                    if nistmatch in nist_yaml["high"]:
                                        unique_append(yaml_dict["tags"],"800-53r5_high")
                                    continue
                                ccimatch = compile_and_return_first_match(r"CCI\-\d{6}", raw_identifier)
                                if ccimatch:
                                    # We have a CCI match!
                                    unique_append(yaml_references["cci"],ccimatch)
                                    continue
                                stigmatch = compile_and_return_first_match(r"[A-Z]{4}\-\d{1,2}\-\d{6}",raw_identifier)
                                if stigmatch:
                                    # We have a STIG match!
                                    # Since these are OS-specific, let's place them in the specific subsection for the OS this guide references from
                                    unique_append(yaml_os_specificrefs["disa_stig"],stigmatch)
                                    continue
                                #print(f"CCE Match: {compile_and_return_first_match(r"CCE\-\d{5}\-\d{1}", raw_identifier)}")
                                #print(f"SRG Match: {compile_and_return_first_match(r"SRG\-OS\-\d{6}\-GPOS\-\d{5}", raw_identifier)}")
                                #print(f"CCI Match: {compile_and_return_first_match(r"CCI\-\d{6}", raw_identifier)}")
                                #print(f"800-53r5 Match: {compile_and_return_first_match(r"[A-Z]{2}\-\d{1,2}\({0,1}\d{0,2}\){0,1}", raw_identifier)}")
                                #print(identifier.get_text())
                        # Finally, we just need to grab the Remediation shell script, and paste it into the OS-specific fix section
                        shellbutton = control.find(string="Remediation Shell script ⇲")
                        if shellbutton:
                            # The array indexing at 1 is to remove the # prefixing the ID
                            remediation = "[source,bash]\n---\n" + control.find(id=shellbutton.parent["data-target"][1:]).get_text() + "\n---"
                            yaml_dict["os_specifics"][os_title][os_version]["fix"] = multiline(remediation)
                #print(yaml_dict)
                try:
                    with open(Path(os.getcwd() + "/" + results.outputdir + "/" + row[1] + "/" + row[0]), 'w') as file:
                        # Apparently custom dumpers don't work with safe_dump. Not awesome
                        # Another really frustrating behavior is that pyyaml handles multi lines like below weird:
                        # A multiline string SHOULD look like this:
                        # key: |
                        #    value value value
                        #    value value value
                        # But pyyaml writes below, no matter what you do (see issue #411 on their github, unresolved since 2022)
                        # key: "value\\\
                        # \\ value \\ \n value \\ value"
                        # Nearly gotten it working using a custom parser further up, except for a frustrating issue! Instead of:
                        # |
                        # text 
                        # text
                        # We instead get 
                        # |-
                        # text 
                        # text
                        # Thanks to this amazing article https://joekiller.com/2023/10/21/yaml-pipe-dash-what/ I've learned block chomping!
                        yaml.dump(yaml_dict, file, default_style=False, sort_keys=False, allow_unicode=True, Dumper=IndentDumper)
                    print(f"Successfully populated and wrote {row[0]}!")
                except Exception as error:
                    print(f"Error: Unable to produce the file {row[0]}! The specific error is {error}.")
                    sys.exit(-1)
                populated_rules += 1
            else:
                print(f"{row[0]} already exists.")
            valid_rules += 1
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Rule Populator Execution time: {execution_time} seconds.")
    print(f"Successfully populated {populated_rules} rules.")
    # TODO: This number is under 1, over 1 rule population per second would be awesome!
    # At current RPS (~0.39), this means that this script can populate all 444 rules in 174 seconds, or a little under 3 minutes.
    print(f"Calculated RPS (rule populations per second) is {execution_time / populated_rules}.")
    print(f"Successfully processed {valid_rules} rules.")

main()
