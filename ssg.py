import typer
from ssg.site import Site

def main(source="content",dest="dist"):
    config = {}
    config['source'] = source
    config['dest'] = dest

    site = Site(**config).build()


if __name__=='__main__':
    typer.run(main)
