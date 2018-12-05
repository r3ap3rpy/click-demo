import click

@click.command()
def hello():
	click.echo('Welcome to my tutorial!')


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
def pythonrocks(count):
	for i in range(count):
		click.echo('Python rocks!!!!!')