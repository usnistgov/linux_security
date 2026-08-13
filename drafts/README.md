# Drafts

Currently, the rules here are based off of DISA STIGs, specifically Ubuntu 22.04
and 24.04. They were AI-generated to extract commands and other useful
information for use in our format, though need a lot of validation to ensure
quality.

## What do the directories mean?

- `0unchecked` - These are rules that have been AI-generated and seen no manual
  review. No one has gotten a chance to review or fix these rules, and they
  definitely need fixing.
- `1validated` - These are rules that have been manually reviewed and pass
  validation! No other assessment has been done to them outside of making sure
  the command "looks good", and they validate against the format the rules are
  meant to be in.
- `2working` - These are rules that have been assessed and tested on a machine
  to verify that the check, fix, and check workflow runs fine. We don't check
  against every system, but ideally 22.04 and 24.04 are checked to ensure the
  commands are working as expected. During this phase, some manual review may
  have also been done to re-categorize and determine where the rule fits.
- `3final` - This is where rules go when they are ready for publishing! All the
  rules successfully work and have been determined to contain information that
  NIST would be okay with publishing in this project. The references,
  description, ID, category, and commands have been assessed by this point, and
  the rules are good to go.

When moving rules between directories, please use `git mv` to better track the
files with Git history.

## Validation

Validation works with the `validate.py` script at the base of the repository.
This project requires PyYAML and Pydantic to be installed (ideally in a Python
virtual environment. Python 3.10+ is required), as the assessment parses the
YAML and checks it against Pydantic classes to ensure the script is usable when
put into the project. THIS MUST PASS FOR SCRIPTS TO MOVE TO `1validated`!!

Note that the rules were automatically generated without a higher-level
`enforcement_info` block. This block must exist to pass validation. This means
that, at a minimum to leave `0unchecked`, a high-level enforcement block should
be created with either a rule or "blank" as the specified type.
