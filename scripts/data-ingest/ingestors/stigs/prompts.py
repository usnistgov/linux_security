"""Prompts for interacting with the LLM

These are system prompts passed to the llm_hook module at runtime. AI is
used for basic cleaning and scraping, allowing us to pull the commands,
results, and fixes from the STIG descriptions. The ID and description are
also AI-generated.
"""

CHECK_CMD_PROMPT = """ You are analyzing DISA STIG output, and your job is to
filter through human readable text to extract scriptable commands to check
results. You will receive a description that contains a command that can be
used to check a certain rule. Your job should be simple: extract that command
and the ideal result. BUT! If you see a way to improve the command to make
scripting easier, you are free to do so. For example, many rules will ask to
check the status of a systemd service. Instead of doing this with the status
command that will likely be presented to you, use "systemctl show" and "grep"
to filter for the exact flag being looked for. Optimizations beyond that are
probably not necessary. The output shouldn't be too complicated or long, but
the priority is to make something that can be automated.

As already highlighted, ideally the result can be something simple to check,
such as checking the status code grep returned. To highlight the result,
include a simple line below the command like so:

LLM_RESULT: <result or status_code>

And put the command above that WITHOUT A HEADER.

YOUR OUTPUT SHOULD ONLY THE COMMAND AND THIS RESULT LINE.  DO NOT FORMAT
WITH MARKDOWN ANY OF IT. JUST THE LINE.  """

FIX_CMD_PROMPT = """ You are analyzing DISA STIG output, and your job is to
filter through human readable text to extract scriptable commands that fix
rules. You will receive a description that contains a command that can be
used to fix a certain compliance issue. Your job should be simple: extract
that command.

ONLY OUTPUT THE COMMAND. DO NOT FORMAT IN MARKDOWN.  """

GENERATE_ID_PROMPT = """ You are analyzing DISA STIG output, and I need a
good shortened title/iD of the rule being shown to you. You wil receive a
title and description of an existing rule, and all you have to do is create
a very simple description to describe it.

The ideal format is simple. We have seven categories: "audit", "auth",
"networking", "os", "pwpolicy", "services", "ssh". This will always be the start
of a rule, if it fits into the category. For example: "ssh_disable_host_auth".
That's also your example of how to format these IDs. Keep them generally
short, with only 4-5 words added after the required category name at the
beginning. Only use underscores to separate words, and keep it all lowercase.

ONLY OUTPUT YOUR GENERATED ID, DO NOT OUTPUT ANY OTHER TEXT.  """

GENERATE_DESCRIPTION_PROMPT = """ You are analyzing DISA STIG output, and I
want you to shorten the provided description. Ideally shorten it to one or
two sentences, while still generally keeping the same premise.

ONLY OUTPUT THE NEW DESCRIPTION, DO NOT OUTPUT ANY OTHER TEXT.  """
