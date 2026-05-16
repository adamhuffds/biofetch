import requests
import json

from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"

def fetch_uniprot(uniprot_id):
    url = f"{UNIPROT_BASE}/{uniprot_id}.json"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    with open("uniprot_raw.json", "w") as f:
        json.dump(data, f, indent=2)
        print("Written to uniprot_raw.json")
    return data

def display_uniprot(data):
    entry_type = data['entryType']
    primary_accession = data['primaryAccession']
    name = data["proteinDescription"]["recommendedName"]["fullName"]["value"]
    gene = data["genes"][0]["geneName"]["value"]
    organism = data["organism"]["scientificName"]
    sequence = data["sequence"]["value"]
    length = str(data["sequence"]["length"])
    mol_weight = str(data['sequence']['molWeight'])

    table = Table(title="UniProt Query Result")
    table.add_column("Attribute", no_wrap=True)
    table.add_column("Value", overflow="fold")

    table.add_row('Entry Type', entry_type)
    table.add_row('Primary Accession', primary_accession)
    table.add_row('Name',name)
    table.add_row('Gene', gene)
    table.add_row('Organism', organism)
    #table.add_row('Sequence', sequence)
    table.add_row('Length', length)
    table.add_row('Molecular Weight', mol_weight)

    console = Console()
    console.print(table)

    print(Panel(sequence, title="Amino Acid Sequence"))