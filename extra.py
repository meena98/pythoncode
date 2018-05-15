@click.group()
@click.option('--removedigits/--no-removedigits',default=False,help='removes digits')
def cli(removedigits):
    result = ''.join([i for i in removedigits if not i.isdigit()])
    click.echo(result)

@click.command()
@click.option('--upper',default='',help='converts into uppercase')
@click.option('--lower',default='',help='converts into lowercase')
@click.option('--concat',default='',help='joins strings')
def sync(upper,lower,concat):
    if verbose:
        click.echo("we are in verbose mode.")
    if upper:
        click.echo(upper.upper())
    if lower:
        click.echo(lower.lower())
    if concat:
        click.echo(concat.replace(",",""))
    else:
        click.echo("hello world")