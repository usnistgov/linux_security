import xml.etree.ElementTree as ET

def print_tags(element, seen_tags):
    # If the tag hasn't been seen before, add it to the set
    if element.tag not in seen_tags:
        seen_tags.add(element.tag)
    
    # Recursively process child elements
    for child in element:
        print_tags(child, seen_tags)

def print_all_tags(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Set to keep track of encountered tags
    seen_tags = set()
    
    # Collect all the unique tags starting from the root element
    print_tags(root, seen_tags)
    
    # Sort the tags alphabetically and print them
    for tag in sorted(seen_tags):
        print(tag)

# Example usage
xml_file = "ssg-rhel10-ds.xml"  # Replace with your XML file path
print_all_tags(xml_file)
