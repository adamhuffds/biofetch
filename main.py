import cmd
import os

from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

from uniprot import fetch_uniprot, display_uniprot



console = Console()

def show_panel():
    print("")
    print(Panel("Welcome to [bold green]BioFetch[/bold green]! Type help for a list of available commands.", title="BioFetch", subtitle="Protein Data Explorer"))
    print("")

class BioFetch(cmd.Cmd):
    #intro = "[bold cyan]Welcome to BioFetch[/bold cyan]\n"
    prompt="(BioFetch) "

    #def do_help(self, line):
        #to be done later
    
    def preloop(self):
        show_panel()

    def do_quit(self, line):
        "Exit BioFetch"
        print("\nGoodbye.\n")
        return True
    
    def do_clear(self, line):
        "Clear the terminal screen"
        console.clear()
        show_panel()

    def do_uniprot(self, line):
        "Query UniProt using UniProt ID"
        uniprot_id = Prompt.ask("\nPlease enter a UniProt ID\n")
        data = fetch_uniprot(uniprot_id)
        display_uniprot(data)

    def do_ncbi(self, line):
        "Query NCBI using Gene ID"
        gene_id = Prompt.ask("\nPlease enter a Gene ID")
        print(f"\nYou entered: {gene_id}\n")

    def do_chembl(self, line):
        "Query ChEMBL using ChEMBL ID"
        chembl_id = Prompt.ask("\nPlease enter a ChEMBL ID")
        print(f"\nYou entered: {chembl_id}\n")
    

if __name__ == "__main__":
    BioFetch().cmdloop()