<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="lscp/data/images/lscp_readme_banner_dark.png">
    <source media="(prefers-color-scheme: light)" srcset="lscp/data/images/lscp_readme_banner.png">
    <img src="lscp/data/images/lscp_readme_banner.png" alt="Linux Security Compliance" width="550">
  </picture>
</p>

<p align="center">
  <a href="https://ubuntu.com/"><img src="https://badgen.net/badge/Ubuntu/22.04%20%26%2024.04%20LTS/orange" alt="Ubuntu"></a>
  <a href="https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux"><img src="https://badgen.net/badge/Red%20Hat/Enterprise%20Linux/red" alt="Red Hat Enterprise Linux"></a>
  <a href="LICENSE"><img src="https://badgen.net/badge/license/NIST/green" alt="License"></a>
  <a href="https://github.com/usnistgov/linux_security/stargazers"><img src="https://badgen.net/github/stars/usnistgov/linux_security" alt="Stars"></a>
</p>

**Supported platforms:** Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, and Red Hat
Enterprise Linux.

The Linux Security Compliance Project (LSCP) is an [open-source](LICENSE)
project that helps organizations secure their Linux systems. You choose the
security rules to enforce, and LSCP generates everything you need:

- **Compliance scripts** to audit a system against the rules in a baseline
- **Fix scripts** to remediate the findings those audits report
- **Documentation** to explain the setup
- **Baselines** that collect rules into a single, reviewable definition of
  "compliant"

Beyond the built-in frameworks, organizations can build customized baselines to
meet their specific cybersecurity needs. Vendors can also use LSCP as a source
to build manifests, datapoints, and other compliance content for their
products.

Every rule is a single YAML file carrying its own check, its own fix, and its
mappings back to the frameworks that require it — so a rule is written and
reviewed once, then reused by every baseline that needs it.

LSCP applies the approach proven by the [macOS Security Compliance
Project](https://github.com/usnistgov/macos_security) (mSCP) — the technical
implementation of NIST SP 800-219 (Rev. 2), [_Automated Secure Configuration
Guidance from the macOS Security Compliance
Project_](https://csrc.nist.gov/pubs/sp/800/219/r2/final) — to the Linux
distributions used across the federal enterprise.

If you would like to contribute, see the [contributor guidance](CONTRIBUTING.md).

> [!NOTE]
> This branch (`rewrite-drafts/stigs`) is an active rewrite. The rule set under
> `drafts/` is being validated distribution by distribution, and both the rule
> schema and the generated output are still subject to change.

## Supported Frameworks

|Country of Origin|Framework Name|OS Supported|
|--------------------|---------------------|--------------------------|
|<a href="https://disa.mil"><img src="https://badgen.net/badge/US/Origin?icon=https%3A%2F%2Fraw.githubusercontent.com%2Flipis%2Fflag-icons%2F086f7e97d657358203916dbe84f61c2bccaa81eb%2Fflags%2F1x1%2Fus.svg" alt="DISA"></a>|DISA STIG|<a href="https://ubuntu.com/"><img src="https://badgen.net/badge/icon/Ubuntu/orange?label" alt="Ubuntu"></a><a href="https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux"><img src="https://badgen.net/badge/icon/Red%20Hat/red?label" alt="Red Hat"></a>|

Don't see your framework listed? Reach out through the [contributor
guidance](CONTRIBUTING.md) or open an
[issue](https://github.com/usnistgov/linux_security/issues/new) to find out how
we can get it included.

## Usage

Civilian agencies are to use the National Checklist Program as required by
[NIST 800-70](https://csrc.nist.gov/pubs/sp/800/70/r5/final).

> [!NOTE]
> Part 39 of the Federal Acquisition Regulations, section 39.101 paragraph (c)
> states, “In acquiring information technology, agencies shall include the
> appropriate information technology security policies and requirements,
> including use of common security configurations available from the National
> Institute of Standards and Technology’s website at https://checklists.nist.gov.
> Agency contracting officers should consult with the requiring official to
> ensure the appropriate standards are incorporated.”

## Authors

| Name | Organization |
|------|--------------|
| Amy Colvin | NIST |
| Bob Gendler | NIST |
| R. Allen Wilkinson | NIST |
| Zachary Amoss | NIST |

## NIST Disclaimer

Any identification of commercial or open-source software in this document is
done so purely in order to specify the methodology adequately. Such
identification is not intended to imply recommendation or endorsement by the
National Institute of Standards and Technology, nor is it intended to imply that
the software identified are necessarily the best available for the purpose.
