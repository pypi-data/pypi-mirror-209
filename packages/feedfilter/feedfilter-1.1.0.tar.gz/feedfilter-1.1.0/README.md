# feed-filter

Filter for modifying feed data.  By default, reads feed from stdin and writes a
modified feed to stdout in either Atom (default) or RSS format.

feed-filter can modify the titles of entries via a regular expression
(python re syntax) and also add the entry's date to the far end of the
title as an aid to sorting for feed readers that cannot have both a
primary sort and secondary sort fields.

feed-filter can also optionaly make some modification to the content
such as converting URLs into links.

## Options

### --config-file

Override the default location of the config file.  Because the config file
if optional, if the specified files does not exits, it will be silently ignored.

### --name (-n)

Section name in config file to use.  If not specified, only the [DEFAULT]
section will apply.  See Configuration File.

### --title-re and --title-sub

The --title-re option specifies a regular expression.  And the --title-sub option can use backrefferences to the RE in --title-re.

So for example, if you have the following options
> --title-re='([^•]+ • )?(Re: )?(.*)' --title-sub='\3'

It will make the following modification to the title

Original title:
> Tutorials and videos • Re: Part design Tutorials and much more ...

Modified title:
> Part design Tutorials and much more ...

That change did 2 things.  It removed a common prefix (forum title) that all entries have, and also removed the 'Re: ' that is added to replies.

If you wanted to keep the prefix, but just remove the 'Re: ', then
change the second option like the example below:

> --title-re='([^•]+ • )?(Re: )?(.*)' --title-sub='\1\3'

And the modified title will now be

Modified title:
> Tutorials and videos • Part design Tutorials and much more ...

Either of the above two examples can be helpfull for modifying a feed
for a forum so that you can sort the entries by title (headline) so
all posts and their responses are groups together.

The regular expression systax used is that of python's regular expressions.

### --add-date-to-title (--no-add-date-to-title)

Just grouping all related posts together is helpfull, but you probably
want to display them in the order they were created.  If you happen to
have a feed reader that can sort on titles with a secondary sort on
the date, then you are all set.  But if you can only do one sort
(title), the posts may be in the wrong order.  This is where the
--add-date-to-title option comes in.

It does pretty much what it says.  It appends the posting's date to
the end of the title after a bunch of spaces.  All the spaces are just
to hide the date string.  The date aids in sorting.  Now when you sort
on the title, the entries will implicitly have a secondary sort on the
date due to its inclusion in the titles.

### --add-posts (--no-add-posts)

For each entry, it attempts to download a topic-specific rss or atom
feed and adds each entry in place of the original entry.  This is
usefull for sites whos forum feed only shows the topics (first post)
and not any replies.  Note that this option won't work on many sites
due to having to parse web pages.  Raise issue for any site that
doesn't seem to work.  Titles on additional posts fetched will all
be taken from the original entry.

### --auto-links (--no-auto-links)

In the content sections, anything that looks like a URL but is not already
an HTML link, will be made into a link.

### --output-fmt

Value can be either 'atom' (default), 'rss', or 'summary'.  The
'summary' options just prints out a few fields in plain text format.
Used primary for debugging.

### Others

Run feed-filter with the --help option to see what other options
are available.


## Configuration File

This program can optionally use a configuration file so you don't have
to specify lots of options on the command line.  The default location
for the configuration files is _${XDG_CONFIG_HOME}/feed-filter.conf_.
If _${XDG_CONFIG_HOME}_ is not set, the default value as specified in
the [XDG Base Directory Specification will be used](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).

The configuration file is an INI style file.  The section to use is
specified via the --name option.  This can ge used to group options
for specific feeds or groups of feed (perhaps from a common site)
together.  If there is a [DEFAULT] section, any value in that section
will be used as a default value for whatever named section is actually
specified (--name).  If --name is not specified, only the [DEFAULT]
section will be used.

For supported options (see --help output) just use the long option
name without the '--' prefix, an '=' and then the value.  For boolean
type options, use True or False as the options value.  e.g.

```
   [DEFAULT]
   auto-links = True

   [mysection]
   date-spaces = 220
   auto-links = False
```

Caution, there is only limited checking for valid values.  Specifying
an invalid option will be silently ignored.


# Installation

This [package](https://pypi.org/project/feedfilter/) is on
[PyPI.org](https://pypi.org/), so just install with pip or pipx like

```
pipx install feedfilter
```

# Development setup

It is recommended that you do any development in a virtual
environment.  If you use direnv, a .envrc file is provided.  You
should always look it over before allowing it to be used.

poetry is required.  You can install it in your virtual enviroment
for this project via ```pip install poetry``` or alternatively via

```
pipx install poetry
```

Once that is installed, just run
```
make install-requirements
  or
poetry install
```

To run feed-filter in development, you should be able to just run

```
feed-filter <args>
```

## Building

To create a build (sdist, wheel) run the following

```
make build
```

Results will be in the dist/ directory.

# Licensing

This project is licensed under the GNU GPL version 3 or later.  See the
LICENSE file in the top-level directory.
