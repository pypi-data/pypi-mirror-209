import os
import subprocess
import click


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


singleton = SingletonClass()
singleton.PROJECT_ROOT_DIR = os.path.dirname(__file__)


def set_to_js_wd():
    os.chdir("{}/javascript/".format(singleton.PROJECT_ROOT_DIR))


def set_to_py_wd():
    os.chdir("{}/python/".format(singleton.PROJECT_ROOT_DIR))


def set_to_project_root_wd():
    os.chdir(singleton.PROJECT_ROOT_DIR)


def python(context, client_type, network, tag, feature):
    set_to_py_wd()
    try:
        set_python_launch_vars(network, client_type)
        load_feature_files()
        launch_behave(tag, feature)
        unload_feature_files()
    except Exception as e:
        set_to_project_root_wd()
        raise e


def javascript(context, network, tag, feature, invalidate_cache):
    set_to_js_wd()
    try:
        if invalidate_cache != 'false':
            invalidate_cache_and_rebuild()
        elif not os.path.isdir('./node_modules'):
            first_time_build()

        set_javascript_launch_vars(network)
        load_feature_files()
        launch_cucumber(tag, feature)
        unload_feature_files()
        set_to_project_root_wd()
    except Exception as e:
        set_to_project_root_wd()
        raise e

def compose_feature_helper_message():
    set_to_project_root_wd()
    message = "Feature file to be used for the test run. Allowed values are "
    features = os.listdir('./features/')
    for i in range(0, len(features)):
        message += "'{}', ".format(features[i].replace(".feature", ""))
    message += "and 'all' and is defaulted to 'payments'. \n\nMore information: https://behave.readthedocs.io/en/latest/tutorial.html?highlight=feature#feature-files."
    return message

@click.group()
@click.version_option(message=('%(prog)s version %(version)s'))
def main():
    """Claudia says hi! Please choose a command to perform an action. A command can have multiple sub-commands and options. Use '--help' option for more information."""

@main.group()
def rippled():
    """Build or install rippled"""

@main.group()
def network():
    """Setup Rippled Network"""

@main.group()
@click.pass_context
def run(context):
    """Run XRPL automated tests"""

@main.group()
def list():
    """List supported options"""

@list.command()
def e2e_features():
    """List all supported features to be tested"""
    set_to_project_root_wd()
    features = os.listdir('./features/')
    message = "Following features were found:\n"
    for i in range(0, len(features)):
        message += "   - {}\n".format(features[i].replace(".feature", ""))
    click.echo(message)

@list.command()
def system_requirements():
    """List all system requirements before continuing further with claudia"""
    message = """
    1. Common requirements:
        - Python3: More information: https://www.python.org/downloads/
        - pip: More information: https://pip.pypa.io/en/stable/installation/
        - docker: More information: https://docs.docker.com/engine/install/
    2. Pull down a fresh copy of rippled code base from https://github.com/XRPLF/rippled
    3. Optional: Following depedencies are only required if you intend to run Javascript tests:
        - node: More information: https://nodejs.org/en/download
        - npm: More information: https://www.npmjs.com/package/download
    """
    click.echo(message)

@rippled.command()
@click.option('--repo', required=True, help="The path to a local rippled repo")
def build(repo):
    """Build rippled from source"""
    set_to_project_root_wd()
    command = "sh network_setup/setup.sh --buildRippled --rippledRepo {}".format(repo)
    subprocess.call(command, shell=True)


@rippled.command()
def install():
    """Install rippled packages"""
    click.echo("Currently not supported")


@network.command()
@click.option('--repo', required=True,
              help="path to rippled repo")
def start(repo):
    """Start a new rippled network"""
    set_to_project_root_wd()
    command = "sh ./network_setup/setup.sh --networkStart  --rippledRepo {}".format(repo)
    subprocess.call(command, shell=True)


@network.command()
def stop():
    """Stop rippled network"""
    set_to_project_root_wd()
    command = "sh ./network_setup/setup.sh --networkStop"
    subprocess.call(command, shell=True)


@network.command()
def status():
    """rippled network status"""
    set_to_project_root_wd()
    command = "sh ./network_setup/setup.sh --networkStatus"
    subprocess.call(command, shell=True)

def print_explorer_message(network):
    if(network=='local'):
        click.echo("INFO: Navigate to 'https://custom.xrpl.org/localhost:6001' to open explorer for this test run against local network.\n")

@run.command()
@click.pass_context
@click.option('--lib', default='py',
              help="The type of client library to be used for running the tests. Allowed values are 'py' and 'js' and is defaulted to 'py'.  \n\nMore information: https://xrpl.org/client-libraries.html#client-libraries")
@click.option('--client_type', default='websocket',
              help="The type of client to be used. This flag should only be used with 'py' library. Allowed values are 'websocket' and 'jsonrpc' and is defaulted to 'websocket'.  \n\nMore information: https://xrpl.org/get-started-using-http-websocket-apis.html#differences-between-json-rpc-and-websocket")
@click.option('--network', default='local',
              help="The type of network to be used. Allowed values are 'devnet', 'testnet', and 'local' and is defaulted to 'local'.  \n\nMore information: https://xrpl.org/get-started-using-http-websocket-apis.html#differences-between-json-rpc-and-websocket")
@click.option('--tag', default='smoke',
              help="Tag name of the all the tests to be included in the test run. Allowed values are 'smoke', 'regression' and 'time_intensive' and is defaulted to 'smoke'.  \n\nMore information: https://behave.readthedocs.io/en/latest/tag_expressions.html")
@click.option('--feature', default='payments',
              help=compose_feature_helper_message())
@click.option('--invalidate_cache', default='false',
              help="Forces ignoring cache, and reinstalling dependencies. This flag should only be used with 'js library. Allowed values are 'true' and 'false' and is defaulted to 'false'.")
def e2etests(context, lib, client_type, network, tag, feature, invalidate_cache):
    """Launch XRPL Automated tests using XRPL library client. Please choose your options wisely."""
    if(lib == 'py'):
        if (invalidate_cache != 'false'):
            raise Exception("--invalidate_cache flag is supported not with {} library client.".format(lib))
        print_explorer_message(network)
        python(context, client_type, network, tag, feature)
    elif(lib == 'js'):
        if (client_type != 'websocket'):
            raise Exception("Client Type {} is not supported with {} library client.".format(client_type, lib))
        print_explorer_message(network)
        javascript(context, network, tag, feature, invalidate_cache)
    else:
        raise Exception("Invalid library type: {}".format(lib))

# @run.command()
# @click.pass_context
# @click.argument("text")
# def customcommand(context, text):
#     """Run a debug command"""
#     click.echo("Running command: {}".format(text))
#     subprocess.call(text, shell=True)


def invalidate_cache_and_rebuild():
    click.echo("Invalidating cache...")
    os.popen('rm -rf ./node_modules')
    install_js_dependencies_if_needed()


def first_time_build():
    click.echo("Need to install missing dependencies. It is a one time action. Please wait...")
    install_js_dependencies_if_needed()


def set_python_launch_vars(network, client_type):
    if network == "local":
        if client_type == "websocket":
            connectionScheme = "ws"
            connectionURL = "127.0.0.1:6001"
            connectionType = "websocket"
        elif client_type == "jsonrpc":
            connectionScheme = "http"
            connectionURL = "127.0.0.1:5001"
            connectionType = "jsonrpc"
        else:
            raise Exception("{} is not a valid client_type".format(client_type))
    elif network == "devnet":
        if client_type == "websocket":
            connectionScheme = "wss"
            connectionURL = "s.devnet.rippletest.net:51233"
            connectionType = "websocket"
        elif client_type == "jsonrpc":
            connectionScheme = "https"
            connectionURL = "s.devnet.rippletest.net:51234"
            connectionType = "jsonrpc"
        else:
            raise Exception("{} is not a valid client_type".format(client_type))
    elif network == "testnet":
        if client_type == "websocket":
            connectionScheme = "wss"
            connectionURL = "s.altnet.rippletest.net:51233"
            connectionType = "websocket"
        elif client_type == "jsonrpc":
            connectionScheme = "https"
            connectionURL = "s.altnet.rippletest.net:51234"
            connectionType = "jsonrpc"
        else:
            raise Exception("{} is not a valid client_type".format(client_type))
    else:
        raise Exception("{} is not a valid network".format(network))

    os.environ['CONNECTION_SCHEME'] = connectionScheme
    os.environ['CONNECTION_URL'] = connectionURL
    os.environ['CONNECTION_TYPE'] = connectionType
    click.echo("Setting CONNECTION_SCHEME='{}', CONNECTION_URL='{}' and CONNECTION_TYPE='{}'".format(connectionScheme,
                                                                                                     connectionURL,
                                                                                                     connectionType))


def set_javascript_launch_vars(network):
    if network == "local":
        connectionScheme = "ws"
        connectionURL = "127.0.0.1:6001"
        connectionType = "websocket"
    elif network == "devnet":
        connectionScheme = "wss"
        connectionURL = "s.devnet.rippletest.net:51233"
        connectionType = "websocket"
    elif network == "testnet":
        connectionScheme = "wss"
        connectionURL = "s.altnet.rippletest.net:51233"
        connectionType = "websocket"
    else:
        raise Exception("{} is not a valid network".format(network))

    os.environ['CONNECTION_SCHEME'] = connectionScheme
    os.environ['CONNECTION_URL'] = connectionURL
    os.environ['CONNECTION_TYPE'] = connectionType
    click.echo("Setting CONNECTION_SCHEME='{}', CONNECTION_URL='{}' and CONNECTION_TYPE='{}'".format(connectionScheme,
                                                                                                     connectionURL,
                                                                                                     connectionType))


def load_feature_files():
    unload_feature_files()
    os.popen("cp -fr ../features/*.feature ./features")


def unload_feature_files():
    os.popen("rm -rf ./features/*.feature")


def launch_behave(tag, feature):
    if feature == "all":
        command = "behave --no-skipped --tags={}".format(tag)
    else:
        command = "behave --no-skipped --tags={} ./features/{}.feature".format(tag, feature)
    os.system(command)


def install_js_dependencies_if_needed():
    command = "sh ./runSetup"
    subprocess.call(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)



def launch_cucumber(tag, feature):
    if feature == "all":
        command = "npx cucumber-js --format @cucumber/pretty-formatter --tags @{}".format(tag)
    else:
        command = "npx cucumber-js --format @cucumber/pretty-formatter --tags @{} ./features/{}.feature".format(tag,
                                                                                                                feature)
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    main(context, obj={})



