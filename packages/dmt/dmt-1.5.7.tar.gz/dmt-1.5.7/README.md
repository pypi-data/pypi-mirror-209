# Domain Management Tool

DMT (for short) is a collection of tools to manage your [RASA domains](https://rasa.com/docs/rasa/domain/) like if they were packages not unlike pip with python but with YAML for RASA.

## Installation

```zsh
pip install dmt
# Or using
#pip install git+https://gitlab.com/waser-technologies/technologies/dmt.git
```

## Usage

Use the `dmt` shortcut command.

```zsh
❯ dmt --help
usage: dmt [-h] [-v] [-l] [-c] [-a ADD] [-s] [-V] [-T] [-S]

Domain Management Tool

optional arguments:
  -h, --help         show this help message and exit
  -v, --version      output version information and exit
  -l, --list         list installed domains
  -c, --create       Create a new domain from template
  -a ADD, --add ADD  git repository hosting a domain to add
  -s, --sync         Synchronize all installed domains
  -V, --validate     Validate all installed domains
  -T, --train        Train new model from all installed domains
  -S, --serve        Serve the lastest model
  -L LANG, --lang LANG  language to work with (defaults to your system preference: $LANG)
```

Find a domain using the tag [#NLP Domains](https://gitlab.com/explore/projects/topics/NLP%20Domains).

And add it.

```zsh
dmt --add $domain_git_url
```

Now validate the domain's data with the installed ones.

```zsh
dmt --validate
```

This will generate some warnings but that is ok most of the time. Unless you made the domain, in which case you should act upon them.

As long as there is not any error you can train a new model using your data. This will take time and computing resourses.

```zsh
dmt --train
```

Or you could add, validate and train with a new domain in one line.

```zsh
dmt -V -T -a $domain_git_url
```

Once trained, you should be able to serve the latest model using the `dmt`.

```zsh
dmt --serve
```

Or by enabling its service.

```zsh
cp ./dmt.service.example /usr/lib/systemd/user/dmt.service
systemctl --user enable --now dmt.service
```

You can also import those tools from `python`.

```python
#!/usr/bin/env python3

from domain.management import tools as dmt
# Where are your domains installed?
INSTALL_PATH="/usr/share/assistant"

# install a new domain from a local repo
path_to_new_domain = "smalltalk" # git clone https://gitlab.com/waser-technologies/data/nlu/en/smalltalk.git ./smalltalk
domains_path = f"{INSTALL_PATH}/domains/en"
dmt.install_domain(tmp_domain, domains_path)

# Get list of installed domains
list_installed_domains = dmt.get_list_installed_domains(domains_path)

# Validate all domains combined
dmt.validate_data(INSTALL_PATH, domains="domains/en", data="data/en", config="configs/en/config.yml")

# Train new model on all domains
dmt.train_lm(INSTALL_PATH, domains="domains/en", data="data/en", config="configs/en/config.yml", models="models/en/NLU")

# Serve the new model
dmt.models_as_service()
```

## Creating your own domains

DMT allows you to quickly start a new domain from a template.

```zsh
dmt --create
```

Once hosted, you can use the `--add` flag to install your domain.

With python.

```python
from domain.management import tools as dmt

dmt.bake_cookie_domain(recipe_url="https://gitlab.com/waser-technologies/cookiecutters/nlu-domain-template")
```