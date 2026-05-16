# BioFetch

An interactive command-line tool for fetching and displaying protein and biochemical data from public scientific APIs.

## Status

In active development. UniProt query and display is functional. NCBI and ChEMBL integrations are in progress.

## Features

- Interactive shell built with Python's `cmd` module and `rich` for styled terminal output
- Query UniProt by accession ID and display a formatted protein profile
- Displays protein name, accession, organism, entry type, sequence length, molecular weight, and full amino acid sequence

## Planned

- Disease association display (UniProt)
- NCBI gene query integration
- ChEMBL bioactivity query integration

## Usage

```bash
cd biofetch
python3 main.py
```

Then type `uniprot` at the prompt and enter a UniProt accession ID (e.g. `P02768` for human serum albumin).

## Dependencies

- `requests`
- `rich`

Install with:

```bash
pip install requests rich
```