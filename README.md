# impdef
`.def` file generator for `.dll` files

## Usage
`python impdef.py destination.def source.dll`

Import libraries can then e.g. be generated by running `lib` (typically included in same installations as `dumpbin`, see below):<BR>
`lib /machine:amd64 /def:destination.def`

## Dependencies
- Python 2 or 3
- `dumpbin.exe` from e.g. Visual C++ Compiler for Python 2.7, Visual Studio Community, or Platform SDKs<BR>
  (adjust `dumpbin` variable in `impdef.py` to point to installed `dumpbin.exe`)
