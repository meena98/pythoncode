import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    if debug:
        click.echo("hey")
        #click.echo('hey' if debug else '')


@cli.command()
@click.argument('name')
@click.argument('name2')
def sync(**kwargs):
    output=''
    for r in kwargs:
        output=output+kwargs[r]
    click.echo(output)
    pass

@cli.command()
@click.argument('name')
def upper(**kwargs):
    '''converts to uppercase'''
    output = '{0}'.format(kwargs['name'])
    click.echo(output.upper())

@cli.command()
@click.argument('name')
def lower(**kwargs):
    '''converts to lowercase'''
    output = '{0}'.format(kwargs['name'])
    click.echo(output.lower())

'''
@click.group()
@click.option('--removedigits/--no-removedigits',default=False,help='removes digits')
def cli(removedigits):
    result = ''.join([i for i in removedigits if not i.isdigit()])
    click.echo(result)

@click.command()
@click.option('--upper',default='',help='converts into uppercase')
def upper(upper):
    click.echo(upper.upper())

@click.command()
@click.option('--lower',default='',help='converts into lowercase')
def lower(lower):
    click.echo(lower.lower())

@click.command()
@click.option('--concat',default='',help='joins strings')
def concat(concat):
    click.echo(concat.replace(",",""))

cli.add_command(upper)
cli.add_command(lower)
cli.add_command(concat)
'''
