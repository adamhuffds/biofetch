import requests
import json

from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

UNIPROT_BASE = "https://rest.uniprot.org/uniprotkb"

def fetch_uniprot(uniprot_id):
    try:
        url = f"{UNIPROT_BASE}/{uniprot_id}.json"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        with open("uniprot_raw.json", "w") as f:
            json.dump(data, f, indent=2)
            print("\n API call result was Written to uniprot_raw.json")
        return data

    except Exception as e:
        print("I'm sorry, that didn't work...")
        data = None
        return data

def display_summary(data):
    entry_type = data['entryType']
    primary_accession = data['primaryAccession']
    name = data["proteinDescription"]["recommendedName"]["fullName"]["value"]
    gene = data["genes"][0]["geneName"]["value"]
    organism = data["organism"]["scientificName"]
    length = str(data["sequence"]["length"])
    mol_weight = str(data['sequence']['molWeight'])

    table = Table()
    table.add_column("Attribute", no_wrap=True)
    table.add_column("Value", overflow="fold")

    table.add_row('Entry Type', entry_type)
    table.add_row('Primary Accession', primary_accession)
    table.add_row('Name',name)
    table.add_row('Gene', gene)
    table.add_row('Organism', organism)
    table.add_row('Length', length)
    table.add_row('Molecular Weight', mol_weight)

    console.print(table)

def display_sequence(data):
    sequence = data["sequence"]["value"]
    print(Panel(sequence, title="Amino Acid Sequence"))

def display_diseases(data):
    
    diseases = [c for c in data['comments'] if c['commentType'] == 'DISEASE']

    if not diseases:
        print("[yellow]No disease associations found[/yellow]")
        return
    
    table = Table()
    table.add_column("Disease")
    table.add_column("Descripton", overflow="fold")
    
    for disease in diseases:
        disease_id = disease['disease']['diseaseId']
        disease_description = disease['disease']['description']
        table.add_row(disease_id, disease_description)

    console.print(table)

def display_function(data):
     functions = [c for c in data['comments'] if c['commentType'] == 'FUNCTION']

     if not functions:
          print("[yellow]No disease associations found[/yellow]")
          return
     
     for function in functions:
         function_value = function['texts'][0]['value']
         print(Panel(function_value, title="Protein Function"))

                                                   












def display_uniprot(data):
    print("")
    display_summary(data)
    display_sequence(data)
    display_diseases(data)
    display_function(data)
