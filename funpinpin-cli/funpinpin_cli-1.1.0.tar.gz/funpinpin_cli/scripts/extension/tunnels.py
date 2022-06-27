"""Tunnel command."""
import click

from funpinpin_cli.core.tunnel import Tunnel
from funpinpin_cli.core.util.exception import (
    NgrokAuthError, NgrokNotRunning, NgrokCannotStopped,
    NgrokError
)
from ..message import (
    get_ngrok_auth_error_msg, get_ngrok_run_msg,
    NGROK_CANNOT_STOPPED_MSG, get_ngrok_108_msg,
    get_ngrok_107_msg
)


@ click.command("status")
def status():
    """
    \b
    \033[96mstatus\033[0m: Output the current status of the ngrok tunnel.
      Usage: \033[96mshopify extension tunnel status\033[0m
    """
    tunnel_urls = Tunnel.urls()
    tunnel_url = ""
    for url in tunnel_urls:
        if url.startswith("https://"):
            tunnel_url = url
    if not tunnel_url and tunnel_urls:
        tunnel_url = tunnel_urls[0]
    if tunnel_url:
        click.echo(
            "ngrok tunnel running at " +
            click.style(f"{tunnel_url}", underline=True)
        )
    else:
        click.echo("No tunnel running.")


@click.command("auth")
@click.argument("token")
def auth(token):
    """
    \b
    \033[96mauth\033[0m: Writes an ngrok auth token to ~/.ngrok2/ngrok.yml to connect with an ngrok account. Visit https://dashboard.ngrok.com/signup to sign up.
      Usage: \033[96mfunpinpin app tunnel auth <token>\033[0m
    """
    Tunnel.auth(token)


@click.command("start")
@click.option(
    "--port",
    default=39351,
    help="Forward the ngrok subdomain to local port PORT. Defaults to 39351."
)
def start(port):
    """
    \b
    \033[96mstart\033[0m: Starts an ngrok tunnel, will print the URL for an existing tunnel if already running.
      Usage: \033[96mfunpinpin extension tunnel start --port=<PORT>\033[0m
    """
    try:
        account, url = Tunnel.start(port)
    except NgrokAuthError:
        msg = get_ngrok_auth_error_msg()
        click.echo(msg)
        return
    except NgrokError as e:
        e_str = str(e)
        if "ERR_NGROK_107" in e_str:
            click.echo(get_ngrok_107_msg())
        elif "ERR_NGROK_108" in e_str:
            click.echo(get_ngrok_108_msg())
        else:
            click.echo(e_str)
        return
    msg = get_ngrok_run_msg(account, url)
    click.echo(msg)


@click.command("stop")
def stop():
    """
    \b
    \033[96mstop\033[0m: Stops the ngrok tunnel.
      Usage: \033[96mfunpinpin app tunnel stop\033[0m
    """
    try:
        Tunnel.stop()
    except NgrokNotRunning as e:
        click.echo(str(e))
        return
    except NgrokCannotStopped:
        click.echo(NGROK_CANNOT_STOPPED_MSG)
        return

    click.echo("ngrok tunnel stopped")
