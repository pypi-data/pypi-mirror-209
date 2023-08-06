#!/usr/bin/python3.8

import os, sys
import shutil
import glob
import yaml
import subprocess
import requests
from rich.markdown import Markdown
from rich.console import Console, JustifyMethod
from multiprocessing import Process
from tqdm import tqdm
from time import sleep

from pathlib import Path
from halo import Halo

import domain as D

console = Console()

def ps(cmd: list, stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd=None, env=None, un=True):
    p = subprocess.Popen(cmd, stdin=stdin, stdout=stdout, cwd=cwd, env=env, universal_newlines=un)
    output, errors = p.communicate()
    return output, errors

def _print(text: str, md=False) -> str:
    if md:
        _md = Markdown(text)
        console.print(_md)
    else:
        console.print(text)
    return text

def __print(print_list: list):
    console.print(print_list)

def _pp(text: str) -> str:
    return _print(f"# {text}", md=True)

def get_rasa():
    return shutil.which('rasa')

def get_rasa_version(rasa):
    version_info = {}
    output, errors = ps([rasa, "--version"])
    if not errors and output:
        for line in output.split('\n'):
            l = line.split(":")
            if len(l) == 2:
                k, v = l
                #key
                while k.endswith(" "):
                    k = k[:-1]
                #value
                while v.startswith(" "):
                    v = v[1:]
                version_info[k] = v
    else:
        _print("[bold red]Error while checking rasa version information[/]")
        _print(f"[red]{errors}[/]")
    
    return version_info

def get_rasa_python(rasa):
    rasa_version_info = get_rasa_version(rasa)
    return rasa_version_info.get("Python Path", None)

def read_yaml(yaml_filepath):
    with open(yaml_filepath, 'r') as yf:
        yml = yaml.load(yf, Loader=yaml.SafeLoader)
        yf.close()
        return yml
    return None

def get_domain_metadata(domain):
    return domain.get('metadata')

def get_list_installed_domains(domains_path: str):
    domain_files = glob.glob(domains_path + "/*.yml")
    list_installed_domains = []
    for d in domain_files:
        domain = read_yaml(d)
        if domain:
            domain_metadata = get_domain_metadata(domain)
            list_installed_domains.append(domain_metadata)
    return list_installed_domains

def mktemp(name: str):
    tmp_path = "/tmp"
    tmp_dir_path = f"{tmp_path}/{name}"
    Path(tmp_dir_path).mkdir(parents=True, exist_ok=True)
    return tmp_dir_path

def git_clone(repository_url, working_dir):
    os.system("git lfs install")
    clone = f"git clone '{repository_url}' '{working_dir}'"
    os.system(clone)
    return

def rmdir(remove_path):
    shutil.rmtree(remove_path)

def copy_actions(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/actions", f"{domain_path}/actions/{domain_lang}/{domain_slug}", dirs_exist_ok=True)
        if not Path(f"{domain_path}/actions/{domain_lang}/__init__.py").exists():
            os.mknod(f"{domain_path}/actions/{domain_lang}/__init__.py")
        return 1
    except FileNotFoundError:
        return 0

def copy_forms(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/data/forms", f"{domain_path}/data/{domain_lang}/NLU/forms/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
    
def copy_stories(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/data/stories", f"{domain_path}/data/{domain_lang}/NLU/stories/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
 
def copy_nlu(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/data/nlu", f"{domain_path}/data/{domain_lang}/NLU/nlu/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
 
def copy_rules(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/data/rules", f"{domain_path}/data/{domain_lang}/NLU/rules/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
 
def copy_responses(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/data/responses", f"{domain_path}/data/{domain_lang}/NLU/responses/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
 
def copy_tests(tmp_domain, domain_path, domain_slug, domain_lang):
    try:
        shutil.copytree(f"{tmp_domain}/tests", f"{domain_path}/tests/{domain_lang}/{domain_slug}", dirs_exist_ok=True)
        return 1
    except FileNotFoundError:
        return 0
 
def copy_domain(tmp_domain, domain_path, domain_slug, domain_lang):
    Path(f'{domain_path}/domains/{domain_lang}').mkdir(parents=True, exist_ok=True)
    try:
        shutil.copyfile(f"{tmp_domain}/domain.yml", f"{domain_path}/domains/{domain_lang}/{domain_slug}.yml")
        return 1
    except FileNotFoundError:
        return 0

def copy_models(tmp_models, models_path, models_lang):
    try:
        shutil.copytree(f"{tmp_models}/models", f"{models_path}/{models_lang}/NLU")
        return 1
    except FileExistsError:
        shutil.copyfile(f"{tmp_models}/models/*.tar.gz", f"{models_path}/{models_lang}/NLU")
    except FileNotFoundError:
        return 0

def copy_config(tmp_config, config_path, config_lang):
    config_dest = f"{config_path}/configs/{config_lang}/config.yml"
    if not Path(config_dest).exists():
        print(f"No config found @{config_dest}. Trying to create it.")
        Path(f"{config_path}/configs/{config_lang}").mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(f"{tmp_config}/config.yml", config_dest)
            return 1
        except FileNotFoundError:
            print(f"Couldn't find {tmp_config}/config.yml")
            raise FileNotFoundError(f"{tmp_config}/config.yml")
            return 0
    else:
        print(f"Found config @{config_dest}.")
        return 1

def copy_endpoints(tmp_domain, domain_path):
    endpoint_dest = f"{domain_path}/endpoints.yml"
    if not Path(endpoint_dest).exists():
        print(f"No endpoint found @{endpoint_dest}. Trying to create it.")
        Path(f"{domain_path}").mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(f"{tmp_domain}/endpoints.yml", endpoint_dest)
            return 1
        except FileNotFoundError:
            print(f"Couldn't find {tmp_domain}/endpoints.yml")
            raise FileNotFoundError(f"{tmp_domain}/endpoints.yml")
            return 0
    else:
        print(f"Found endpoint @{endpoint_dest}.")
        return 1

def copy_credentials(tmp_domain, domain_path):
    cred_dest = f"{domain_path}/credentials.yml"
    if not Path(cred_dest).exists():
        print(f"No credentials found @{cred_dest}. Trying to create it.")
        Path(f"{domain_path}").mkdir(parents=True, exist_ok=True)
        try:
            shutil.copyfile(f"{tmp_domain}/credentials.yml", cred_dest)
            return 1
        except FileNotFoundError:
            print(f"Couldn't find {tmp_domain}/credentials.yml")
            raise FileNotFoundError(f"{tmp_domain}/credentials.yml")
            return 0
    else:
        print(f"Found credentials @{cred_dest}.")
        return 1

def mk_models_dir(models_path):
    Path(models_path).mkdir(parents=True, exist_ok=True)

def mk_assistant_dir(assistant_path):
    domains_path = f"{D.ASSISTANT_PATH}/domains/{D.I18N}"
    actions_path = f"{D.ASSISTANT_PATH}/actions/{D.I18N}"
    actions_init_modules = [
        f"{D.ASSISTANT_PATH}/actions/__init__.py",
        f"{D.ASSISTANT_PATH}/actions/{D.I18N}/__init__.py"
    ]
    #configs_path = f"{D.ASSISTANT_PATH}/configs/{D.I18N}"
    data_path = f"{D.ASSISTANT_PATH}/data/{D.I18N}/NLU"
    forms_path = f"{data_path}/forms"
    stories_path = f"{data_path}/stories"
    nlu_path = f"{data_path}/nlu"
    responses_path = f"{data_path}/responses"
    rules_path = f"{data_path}/rules"
    tests_path = f"{D.ASSISTANT_PATH}/tests/{D.I18N}"
    Path(actions_path).mkdir(parents=True, exist_ok=True)
    for module in actions_init_modules:
        if not Path(module).exists():
            os.mknod(module)
    #Path(configs_path).mkdir(parents=True, exist_ok=True)
    Path(data_path).mkdir(parents=True, exist_ok=True)
    #Path(forms_path).mkdir(parents=True, exist_ok=True)
    Path(stories_path).mkdir(parents=True, exist_ok=True)
    Path(nlu_path).mkdir(parents=True, exist_ok=True)
    Path(responses_path).mkdir(parents=True, exist_ok=True)
    Path(rules_path).mkdir(parents=True, exist_ok=True)
    Path(tests_path).mkdir(parents=True, exist_ok=True)
    Path(domains_path).mkdir(parents=True, exist_ok=True)

def install_domain_requirements(requirements_path):
    rasa = get_rasa()
    python = get_rasa_python(rasa) or "/usr/bin/python"   
    pip = f"{python} -m pip"
    p = Path(requirements_path)
    if p.exists():
        r = p.absolute().as_posix()
        install_requirements = f"{pip} install -r '{r}'"
        if os.system(f"{install_requirements}") != 0:
            _print("[red]:warning: Could not install as user. Need administration privileges to install domain dependencies.[/]")
            assert os.system(f"sudo {install_requirements}") == 0, f"Failed to install domain requirements.\n(#|$) {install_requirements}"
    else:
        _print(f"Requirement file `{p}` not found.", md=True)
        _print("This means the domain has no requirements for actions. Probably even no action at all.")
        _print("Install any missing python dependency for actions manually using:")
        _print(f"(#|$) ```{pip} install $missing_dependency```", md=True)

def install_domain(tmp_domain, domain_path):
    mk_assistant_dir(domain_path)
    domain = read_yaml(f"{tmp_domain}/domain.yml")
    domain_metadata = get_domain_metadata(domain)
    domain_name = domain_metadata.get('name', 'Unamed domain')
    domain_lang = domain_metadata.get('lang', 'en')
    _pp(f"Installing {domain_name} for {domain_lang.upper()}")
    copy_actions(tmp_domain, domain_path, domain_name, domain_lang)
    #copy_forms(tmp_domain, domain_path, domain_name)
    copy_stories(tmp_domain, domain_path, domain_name, domain_lang)
    copy_nlu(tmp_domain, domain_path, domain_name, domain_lang)
    copy_rules(tmp_domain, domain_path, domain_name, domain_lang)
    copy_responses(tmp_domain, domain_path, domain_name, domain_lang)
    copy_tests(tmp_domain, domain_path, domain_name, domain_lang)
    copy_config(tmp_domain, domain_path, domain_lang)
    copy_endpoints(tmp_domain, domain_path)
    copy_credentials(tmp_domain, domain_path)
    install_domain_requirements(f"{tmp_domain}/requirements.txt")
    dc = copy_domain(tmp_domain, domain_path, domain_name, domain_lang)
    if dc < 1:
        raise Exception("Unable to copy domain file.")
    rmdir(tmp_domain)
    return domain_metadata

def install_domain_from_url(domain_url):
    tmp_domain = mktemp(f"dmt") + "/add_domain"
    _pp("Cloning Domain")
    git_clone(domain_url, tmp_domain)
    # Install domain
    _pp("Installing Domain")
    install_domain(tmp_domain, D.ASSISTANT_PATH)

def install_required_domains():
    requirements = [
        f"https://gitlab.com/waser-technologies/data/nlu/{D.I18N}/smalltalk.git",
        f"https://gitlab.com/waser-technologies/data/nlu/{D.I18N}/system.git",
    ]
    for url in requirements:
        install_domain_from_url(url)

def install_pretrained_models(tmp_models, models_path, models_lang):
    install_required_domains()
    copy_models(tmp_models, f"{models_path}/models", models_lang)
    copy_config(tmp_models, models_path, models_lang)
    rmdir(tmp_models)
    print("If this model contains custom actions responses, you need to serve them manually.")
    return models_path

def validate_data(data_path, data=None, domains=None, config=None):
    rasa = get_rasa()
    if rasa:
        stdout_path = f"{data_path}/validation.stdout.txt"
        stdOut = open(stdout_path, 'w+')
        
        cmd = [
            rasa,
            "data",
            "validate",
            "--data" if data else "",
            f"{data}" if data else "",
            "-d" if domains else "",
            f"{domains}" if domains else "",
            "-c" if config else "",
            f"{config}" if config else "",
            "--quiet"
        ]
        output, errors = ps(cmd, stdin=stdOut, stdout=stdOut, cwd=data_path)
        stdOut.close()
        _print(f"See logs @`{data_path}/validation.*.txt`", md=True)
    else:
        _print(":warning: Cannot validate the data without RASA installed inside the `$PATH`.", md=True)
        _print("```pip install -U rasa```", md=True)
    return

def train_lm(data_path, data=None, domains=None, config=None, models=None):
    rasa = get_rasa()
    if rasa:
        stdout_path = f"{data_path}/training.stdout.txt"
        stdOut = open(stdout_path, 'w+')
        cmd = [
            rasa,
            "train",
            "--data" if data else "",
            f"{data}" if data else "",
            "-d" if domains else "",
            f"{domains}" if domains else "",
            "-c" if config else "",
            f"{config}" if config else "",
            "--out" if models else "",
            f"{models}" if models else "",
            "--quiet"
        ]
        output, errors = ps(cmd, stdin=stdOut, stdout=stdOut, cwd=data_path)
        stdOut.close()
        _print(f"See logs @`{data_path}/training.*.txt`", md=True)
    else:
        _print(":warning: Cannot train the language model without RASA installed inside the `$PATH`.", md=True)
        _print("```pip install -U rasa```", md=True)
    return

def add_evaluate_domain_and_train_models(domain_repo):
    tmp_domain = mktemp(f"dmt") + "/add_domain"
    _pp("Cloning Domain")
    git_clone(domain_repo, tmp_domain)
    # Install domain
    _pp("Installing Domain")
    domain = install_domain(tmp_domain, D.ASSISTANT_PATH)
    domain_lang = domain.get('lang', 'en')
    rmdir(tmp_domain)
    validate_data(D.ASSISTANT_PATH, domains=f"domains/{domain_lang}", data=f"data/{domain_lang}", config=f"configs/{domain_lang}/config.yml")
    train_lm(D.ASSISTANT_PATH, domains=f"domains/{domain_lang}", data=f"data/{domain_lang}", config=f"configs/{domain_lang}/config.yml", models=f"models/{domain_lang}/NLU")
    _print(f"Use `dmt -S -L {domain_lang}` to serve this model.", md=True)
    return f"models/{domain_lang}/NLU"

def serve_lm(data_path, models, endpoints, credentials):
    rasa = get_rasa()
    if rasa:
        cmd = [
            rasa,
            "run",
            "-m",
            f"{models}",
            "--enable-api",
            "--endpoints",
            f"{endpoints}",
            "--credentials",
            f"{credentials}"
        ]
        output, errors = ps(cmd, cwd=data_path)
    else:
        _print(":warning: Cannot serve language model without RASA installed inside the `$PATH`.", md=True)
        _print("```pip install -U rasa```", md=True)
    return

def serve_actions(data_path, module_name, lang):
    rasa = get_rasa()
    if rasa:
        cmd = [
            rasa,
            "run",
            'actions',
            '--actions',
            f"{module_name}.{lang}"
        ]
        output, errors = ps(cmd, cwd=data_path)
    else:
        _print(":warning: Cannot serve action without the RASA Action Server installed inside the `$PATH`.", md=True)
        _print("```pip install -U rasa rasa-sdk```", md=True)
    return

def ping(link):
	try:
		#Get Url
		get = requests.get(link)
		# if the request succeeds 
		if get.status_code == 200:
			return True
		else:
			return False
	except requests.exceptions.RequestException:
		return False

def models_as_service(data_path=D.ASSISTANT_PATH, models=f"models/{D.I18N}/NLU", endpoints="endpoints.yml", credentials="credentials.yml", module_name="actions", lang=D.I18N):
    """
    Loads the NLP models and sets up actions.
    """
    # Check models exists

    try:
        assert models == f"models/{lang}/NLU"
    except Exception:
        raise RuntimeError(f"{models} is not models/{lang}/NLU")

    if not Path(f"{data_path}/{models}").exists() or not glob.glob(f"{data_path}/{models}/*.tar.gz"):
    ##  if not:
    ##  Check if any model is installed
        gm = glob.glob(f"models/{lang}/NLU/*.tar.gz")
        if not gm:
    ###     if not:
    ###     Checks if lang has pre-trained model
            if not ping(f"{D.REPO_MODELS}/{lang}/{D.REPO_BASE_MODELS_NAME}"):
    ####        if not:
    ####        Checks if smalltalk domain is avalible for lang
                if not ping(f"{D.REPO_DOMAINS}/{lang}/{D.REPO_BASE_DOMAIN_NAME}"):
    #####           if not:
    #####           Sets lang to english
                    models="models/en/NLU"
                    lang="en"
    #####           Checks if english has pre-trained models
                    if not ping(f"{D.REPO_MODELS}/en/{D.REPO_BASE_MODELS_NAME}"):
    ######              if not:
    ######              Check if smalltalk is avalible in english
                        if not ping(f"{D.REPO_DOMAINS}/en/{D.REPO_BASE_DOMAIN_NAME}"):
    #######                 if not:
    #######                 Raises NotImplementedError
                            raise NotImplementedError(f"Languages: [{lang}, en]; not found")
                        else:
                            _print(":warning: No english models found but SmallTalk exists.")
                            _print("Using domain SmallTalk to build a model for `EN`.", md=True)
                            # Add and evaluate SmallTalk and train a new model for english
                            add_evaluate_domain_and_train_models(f"{D.REPO_DOMAINS}/en/{D.REPO_BASE_DOMAIN_NAME}.git")
                    else:
                        _print(f"No domain for `{lang}` found.", md=True)
                        print("Using english as backup language.")
                        print("Found pre-trained models for `EN`.", md=True)
                        # download and install pre-trained models for english
                        # Clone models
                        tmp_models = mktemp(f"dmt") + "/add_models"
                        _pp("Cloning Models")
                        git_clone(f"{D.REPO_MODELS}/en/{D.REPO_BASE_MODELS_NAME}.git", tmp_models)
                        # Install models
                        _pp("Installing Models")
                        install_pretrained_models(tmp_models, D.ASSISTANT_PATH, "en")
                else:
                    _print(f"No models for `{lang}` but SmallTalk exists.", md=True)
                    _print(f"Using domain SmallTalk to build a model for `{lang.upper()}`.", md=True)
                    # Add and evaluate SmallTalk and train a new model for {D.I18N}
                    add_evaluate_domain_and_train_models(f"{D.REPO_DOMAINS}/{lang}/{D.REPO_BASE_DOMAIN_NAME}.git")
            else:
                _print(f"Found pre-trained models for `{lang.upper()}`.", md=True)
                # download and install pre-trained models for {D.I18N}
                # Clone models
                tmp_models = mktemp(f"dmt") + "/add_models"
                _pp("Cloning Models")
                git_clone(f"{D.REPO_MODELS}/{lang}/{D.REPO_BASE_MODELS_NAME}.git", tmp_models)
                # Install models
                _pp("Installing Models")
                install_pretrained_models(tmp_models, D.ASSISTANT_PATH, lang)
        else:
            m = gm[0] # Take the first model here but we'll let rasa choose the best (inside the same dir)
            models = Path(m).parent # Take the parent dir
            _print(f"Found models at `{models}`.", md=True)
    else:
        _print(f"Found local models at `{models}`.", md=True)
    
    nlp_server_proc = Process(target=serve_lm, args=(data_path, models, endpoints, credentials))
    actions_server_proc = Process(target=serve_actions, args=(data_path, module_name, lang))
    actions_server_proc.start()
    sleep(10)
    nlp_server_proc.start()
    return nlp_server_proc.join(), actions_server_proc.join()

def check_cookiecutter():
    fp = shutil.which('cookiecutter')
    if not fp:
        _print("You must install `cookiecutter` somewhere inside your `$PATH`.", md=True)
        _print("```pip install -U cookiecutter```", md=True)
    return fp

def bake_cookie_domain(recipe_url=D.REPO_BASE_COOKIECUTTER_URL):
    cc = check_cookiecutter()
    if not cc:
        return 1
    else:
        bake_recipe = [
            f"{cc}",
            f"{recipe_url}"
        ]
        p = subprocess.Popen(bake_recipe, universal_newlines=True)
        output, errors = p.communicate()
        if errors:
            print(errors)
            return 1
        else:
            _print("[green]Your domain was successfully created here.[/]")
            _print("Use `git init; git remote add origin $url` inside the domain to initialize the repository.", md=True)
            _print("and `git add .; git commit -m 'initial release'; git push --set-upstream origin main` to upload it.", md=True)
            return 0

def print_paths(domains_path=None, data_path=None, config_path=None, models_path=None, quiet=False):
    results = ()
    if domains_path:
        results += (domains_path,)
        if not quiet:
            _print(f"Domains Path: `{domains_path}`", md=True)
    if data_path:
        results += (data_path,)
        if not quiet:
            _print(f"Data Path: `{data_path}`", md=True)
    if config_path:
        results += (config_path,)
        if not quiet:
            _print(f"Config Path: `{config_path}`", md=True)
    if models_path:
        results += (models_path,)
        if not quiet:
            _print(f"Models Path: `{models_path}`", md=True)
    if len(results) == 1:
        return results[0]
    return results

def first_run_switch_optin_rasa_telemetry():
    models_path = print_paths(models_path=f"models/{D.I18N}/NLU", quiet=True)
    if not Path(f"{D.ASSISTANT_PATH}/{models_path}").exists() or not glob.glob(f"{D.ASSISTANT_PATH}/{models_path}/*.tar.gz"):
        print("First run detected. Opting out of telemetry schemes.")
        assert os.system("rasa telemetry disable") == 0, "Failed to disable rasa telemetry."
        print("Rasa Telemetry has been disabled.")
        print("To opt-in type:")
        _print("```rasa telemetry enable```", md=True)

def main(ARGS):

    import domain

    first_run_switch_optin_rasa_telemetry()

    if not ARGS.version and not ARGS.list and not ARGS.create and not ARGS.add and not ARGS.sync and not ARGS.validate and not ARGS.train and not ARGS.serve:
        _pp("Domain Management Tool")
        _print(f"Version: `{str(D.__version__)}`", md=True)
        rasa = get_rasa()
        if rasa:
            _print(f"RASA Version: `{get_rasa_version(rasa).get('Rasa Version', 'N/A')}`", md=True)
        print()
        _print("[Tip]: Type `dmt --help` for help.", md=True)
    
    if ARGS.version:
        _pp("Domain Management Tool")
        _print(f"Version: `{str(D.__version__)}`", md=True)
        rasa = get_rasa()
        if rasa:
            _print(f"RASA Version: `{get_rasa_version(rasa).get('Rasa Version', 'N/A')}`", md=True)
        return

    if ARGS.list and ARGS.lang:
        _pp(f"{ARGS.lang.upper()}: List of installed domains")
        spinner = Halo(text="Fetching Installed Domains", spinner='dots')
        spinner.start()
        # Checking domains directory exists
        mk_assistant_dir(D.ASSISTANT_PATH)
        print()
        domains_path = print_paths(domains_path=f"{D.ASSISTANT_PATH}/domains/{ARGS.lang}")
        # for each domain
        list_installed_domains = get_list_installed_domains(domains_path)
        ## get metadata.name
        ## get metadata.url
        spinner.stop()
        for domain in list_installed_domains:
            _print(f" - __{domain.get('name')}__: [{domain.get('url')}]({domain.get('url')})", md=True)
        return
    
    if ARGS.create:
        # Create new domain from cookiecutter template repo
        _pp("Creating new domain")
        _print("Looking for template...")
        sys.exit(bake_cookie_domain())
    
    if ARGS.add:
        #spinner = Halo(text="Cloning Domain", spinner='dots')
        _pp("Adding new domain")
        #spinner.start()
        print(f"GitURL: {ARGS.add}")
        # Clone domain
        tmp_domain = mktemp(f"dmt") + "/add_domain"
        _pp("Cloning Domain")
        git_clone(ARGS.add, tmp_domain)
        # Install domain
        _pp("Installing Domain")
        install_domain(tmp_domain, D.ASSISTANT_PATH)

        if not ARGS.validate or not ARGS.train:
            _pp("Warning")
            print("You need to validate this domain and train a new model to install this domain properly.")
            _print("```dmt -V -T```", md=True)
        #spinner.stop()
    
    if ARGS.sync and ARGS.lang:
        #spinner = Halo(text="Summoning Domains", spinner='dots')
        # Sync domains
        _pp(f"Syncho-summoning Domains for {ARGS.lang.upper()}")
        #spinner.start()
        # Checking domains directory exists
        domains_path = print_paths(domains_path=f"{D.ASSISTANT_PATH}/domains/{ARGS.lang}")
        Path(domains_path).mkdir(parents=True, exist_ok=True)
        # for each domain
        list_installed_domains = get_list_installed_domains(domains_path)
        for domain in tqdm(list_installed_domains):
        ##  Clone domain
            domain_name = domain.get('name')
            domain_url = domain.get('url')
            if domain_url:
                work_dir = mktemp(f"dmt/{domain_name if domain_name else 'unamed_domain'}")
                _pp(f"Cloning Domain {domain_name}")
                git_clone(domain_url, work_dir)
        ## Install domain
                _pp(f"Installing Domain {domain_name}")
                install_domain(work_dir, D.ASSISTANT_PATH)
        #spinner.stop()
        _print("Domains have been synchronized.")

    if ARGS.validate and ARGS.lang:
        # Validate data
        #spinner = Halo(text=f"Validating {ARGS.lang.upper()}", spinner='dots')
        _pp(f"Validating Data for {ARGS.lang.upper()}")
        domains_path, data_path, config_path = print_paths(domains_path=f"domains/{ARGS.lang}", data_path=f"data/{ARGS.lang}", config_path=f"configs/{ARGS.lang}/config.yml")
        #spinner.start()
        validate_data(D.ASSISTANT_PATH, domains=domains_path, data=data_path, config=config_path)
        #spinner.stop()

    if ARGS.train and ARGS.lang:
        # Train
        #spinner = Halo(text="Training", spinner='dots')
        _pp("Training Models")
        domains_path, data_path, config_path, models_path = print_paths(domains_path=f"domains/{ARGS.lang}", data_path=f"data/{ARGS.lang}", config_path=f"configs/{ARGS.lang}/config.yml", models_path=f"models/{ARGS.lang}/NLU")
        #spinner.start()
        train_lm(D.ASSISTANT_PATH, domains=domains_path, data=data_path, config=config_path, models=models_path)
        #spinner.stop()
    
    if ARGS.serve and ARGS.lang:
        # Train
        #spinner = Halo(text="Serving", spinner='dots')
        _pp("Serving Models")
        models_path = print_paths(models_path=f"models/{ARGS.lang}/NLU")
        #spinner.start()
        models_as_service(models=models_path, lang=ARGS.lang)
        #spinner.stop()
    
    return 0
