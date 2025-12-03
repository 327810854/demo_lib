# demo_lib

A standalone repository for running demos that use the dataproc library as a Git submodule.

## Setup (Windows)

1. Clone this repo:
   `powershell
   git clone https://github.com/327810854/demo_lib
   cd demo_lib
   `
2. Initialize submodules:
   `powershell
   git submodule update --init --recursive
   `
3. Create and activate a virtual environment (optional but recommended):
   `powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   `
4. Install dependencies:
   `powershell
   pip install -r requirements.txt
   `

## Run the demo

Set PYTHONPATH so Python can import the dataproc package from the submodule, then run the demo:

`powershell
set PYTHONPATH=libs\dataproc
python -m examples.image_demo
`

The script will generate an input.jpg if missing and save outputs to examples\output\.

## Project layout

- libs/dataproc: Git submodule pointing to the library repository
- examples/: Demo scripts and assets
- equirements.txt: Demo dependencies

## Notes

- If ModuleNotFoundError: No module named 'dataproc' occurs, ensure PYTHONPATH is set correctly as shown above.
- Demo outputs are ignored via .gitignore.
