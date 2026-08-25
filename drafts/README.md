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

Use the mSCP project to validate by putting the rules into the "custom"
directory and running `python[3] mscp.py admin validate`.

mSCP requires that "ubuntu" be added to the schema along with the addition of
an "exit_code" result. The diff of the file off of the dev_27 branch is below.

```diff
diff --git a/src/mscp/data/schema/mscp_rule.json b/src/mscp/data/schema/mscp_rule.json
index e61a04a0..2ccb49e1 100644
--- a/src/mscp/data/schema/mscp_rule.json
+++ b/src/mscp/data/schema/mscp_rule.json
@@ -318,6 +318,41 @@
                         }
                     },
                     "additionalProperties": false
+                },
+                "ubuntu": {
+                    "type": "object",
+                    "description": "Schema for identifying components to support Ubuntu",
+                    "properties": {
+                        "enforcement_info": {
+                            "$ref": "#/$defs/enforcement_infoDef"
+                        },
+                        "20.04": {
+                            "$ref": "#/$defs/osDef"
+                        },
+                        "22.04": {
+                            "$ref": "#/$defs/osDef"
+                        },
+                        "24.04": {
+                            "$ref": "#/$defs/osDef"
+                        }
+                    },
+                    "additionalProperties": false
                 }
             }
         },
@@ -512,6 +547,9 @@
                 },
                 "boolean": {
                     "type": "boolean"
+                },
+                "exit_code": {
+                    "type": "integer"
                 }
             }
         },
```
