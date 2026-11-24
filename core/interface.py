import rich
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.console import Console
console = Console()
banner = r'''
███╗   ███╗██╗███╗   ███╗██╗██████╗ 
████╗ ████║██║████╗ ████║██║██╔══██╗
██╔████╔██║██║██╔████╔██║██║██████╔╝
██║╚██╔╝██║██║██║╚██╔╝██║██║██╔══██╗
██║ ╚═╝ ██║██║██║ ╚═╝ ██║██║██║  ██║
╚═╝     ╚═╝╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝
'''

def show_banner():
   console.print(Align.center(Text(banner, style="bold green")))
   console.print(Align.center("[bold green]OSINT INTELLIGENCE FRAMEWORK[/bold green]"))
   console.print(Align.center("[dim]VERSION 0.1.0[/dim]"))
   show_status()

def show_status():
   status = Table.grid(padding=1)
   status.add_column(style="cyan")
   status.add_column(style="green")

   status.add_row("FRAMEWORK", "MIMIR")
   status.add_row("VERSION", "0.1.0")
   status.add_row("ENGINE", "ONLINE")
   status.add_row("MODE", "PASSIVE INVESTIGATION")

def show_menu():
   menu = Table(title="INTELLIGENCE MODULES", border_style="bright_green", header_style="dim green")
   menu.add_column("OPTION", justify="center")
   menu.add_column("MODULE")
   menu.add_column("DESCRIPTION")
   menu.add_row("[1]", "DNS Intelligence", "DNS record collection")
   menu.add_row("[2]", "WHOIS Intelligence", "Domain registration data")
   menu.add_row("[3]", "Certificate Intelligence", "Public certificate records")
   menu.add_row("[4]", "IP Intelligence", "Public IP and network information")
   menu.add_row("[5]", "Investigation History", "Previous investigations")
   menu.add_row("[0]", "Exit", "Close MIMIR")
   console.print(Align.center(menu))
def show_footer():
   console.print(Align.center("MIMIR OSINT FRAMEWORK"))
