from rich.console import Console
console = Console()
from core.interface import (show_banner, show_status, show_menu, show_footer)

def main():
   while True:
      console.clear()
      show_banner()
      show_status()
      show_menu()
      show_footer()
      choice = console.input("\n[bold green]> [/bold green]")
      if choice == "1":
         console.print("[green][+] DNS module selected[/green]")
         
      elif choice == "2":
         console.print("[green][+] WHOIS module selected[/green]")
         
      elif choice == "3":
         console.print("[green][+] Certificate module selected[/green]")
         
      elif choice == "4":
         console.print("[green][+] IP intelligence selected[/green]")
         
      elif choice == "5":
         console.print("[green][+] Investigation history selected[/green]")

      elif choice == "0":
         console.print("[bold red]Closing MIMIR...[/bold red]")
         break
      else:
         console.print("[red]Invalid option.[/red]")

      if choice != 0:
         console.input("\n[dim]Press ENTER to continue...[/dim]")


if __name__ == "__main__":
   main()