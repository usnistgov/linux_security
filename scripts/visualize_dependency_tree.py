#
# Dependency Visualizer for SCAP DataStreams
#
# This script is designed to produce a human-readable OVAL dependency tree from a provided SCAP DataStream file.
# This information is useful for visualizing the cyclical nature of SCAP code, particularly OVAL references.
# Since we ideally want to essentially create a compiler that converts our SCAP DataStream program representation
# Into a bash or ansible script which in-order loads the required references to minimize execution lag
# And maximize productive results, we need to understand how the various data ingestion interacts.
# What variables are used in what objects, what states are used in what tests, what variables are ODVs, et cetera.
# The end goal of the populate_rule_yaml script is to automatically ingest DataStreams and compile their checks and fixes
# Into ansible or any other declarative language, generating a final playbook or script which contains only the 
# Rules that the organization wants enforced, and any required source variables, states, et cetera. 
# Previously, I had been thinking of each rule as an atomic state, and while they are atomic to a degree (the yaml),
# When the final ansible playbook or whatnot is created, if the variable naming is done intelligently, this can be 
# Greatly consolidated down.

# TODO: Parse refs, currently this does not parse the obj_refs, var_refs, etc
# TODO: Try and make this more readable, lots of arrows everywhere! 

#!/usr/bin/env python3
import os
import argparse
import sys
import lxml
import re
import lxml.etree as etree
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from graphviz import Digraph
from scap import *

xmlparser = XmlParser(handler=LxmlEventHandler)

def main():
    
    # Create arguments parser
    parser = argparse.ArgumentParser(description='Visualizes the reference tree of a provided SCAP DataStream file.')
    parser.add_argument("--datastream", default="../resources/xml/ssg-rhel8-ds.xml", help="A local or full file path to an SSG/SCAP DataStream XML file.")\
    
    try:
        # Parse our arguments 
        parsedargs = parser.parse_args()
        datastreamfile = os.path.basename(parsedargs.datastream).split(".")[0]
        print(f"Using the datastream {datastreamfile} at this path: {parsedargs.datastream}")
    except IOError as msg:
        # TODO: Improve the error handling on this.
        parser.error(str(msg))
        sys.exit(-1)

    # First, we'll need to parse the XML as a tree. We should be able to use ETree for this
    tree = lxml.etree.parse(parsedargs.datastream)
    root = tree.getroot()

    # Then, we'll need to grab the definitions. I've tried graphing an entire datastream and it looks like some sort of abstract art...
    # Or crashes your browser! 
    definitions = tree.find(".//oval-def:definitions",namespaces=root.nsmap)

    # Now, we'll visualize.
    # Create a new directed graph
    dot = Digraph(strict=True)
    
    # Recursive function to add nodes and edges
    def add_nodes_edges(node, parent=None, depth=0):
        #if depth > 0:
        #    parsednode = xmlparser.parse(node)
        #    #print(f"Parsed:{parsednode}")
        #    cleanname = re.sub(r'[^a-zA-Z]', '', parsednode.id).replace("ovalssg","")
        #else:
        qname = etree.QName(node).localname
        cleanname = re.sub(r'[^a-zA-Z_]', '', qname)
        #print(f"parent: {parent} tag: {node.getchildren()}")
        dot.node(cleanname,cleanname)
        if depth == 15:
            return
        if parent:
            #print(f"edge creation for {parent} > {cleanname}")
            dot.edge(parent, cleanname)
        for child in node:
            #print(f"child tag {child.tag}")
            add_nodes_edges(child, cleanname, depth=depth+1)
    
    # Start the recursion from the definitions group
    add_nodes_edges(root)
    
    # Render the graph
    output_name = f"{datastreamfile}_graph"
    dot.unflatten(stagger=3)  
    dot.render(output_name, format='svg', cleanup=True)
    print(f"XML tree visualization saved as '{output_name}.svg'")

main()