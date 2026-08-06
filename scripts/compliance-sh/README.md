# compliance-sh

This script is designed to generate a basic BASH script for the purposes of
checking and fixing compliance violations. It utilizes jinja2 for script
generation so all rules can be contained in a single script file.

**Warning!! This script and its associated elements are in development, and
should not be used in any production/sensitive environment!**

## Usage

The following utilities are required for basic script utilization:

- `bash`
- `coreutils`
- `findutils`
- `bc`
- `whiptail` - [Optional] Required if using interactive mode

...and any other commands expected by rules and their checks.

## Support

The script is best tested on Ubuntu, followed by Red Hat Enterprise Linux. Other
Linux distributions should also work, provided the rule files exist for it, but
they are not as thoroughly tested.
