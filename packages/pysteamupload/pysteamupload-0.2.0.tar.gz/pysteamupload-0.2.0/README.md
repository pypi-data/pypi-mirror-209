# PySteamUpload

A convenient tool to upload easily your binaries to Steam.

## How does it work ?

`PySteamUpload` requires two environment variables:
- `STEAM_USERNAME`
- `STEAM_PASSWORD`

## Initialize SteamCMD

Execute then initialize SteamCMD with provided command:<br>
`python -m pysteamupload initialize_only`

### Upload

`python -m pysteamupload upload --app_id="123456" --depot_id="1234567" --build_description="My first upload" --content_path="C:\Temp\MyBinariesAreLocatedHere"`

### Packaging

- `python -m pip install twine setuptools wheel`
- `python setup.py sdist bdist_wheel`
- `python -m twine upload dist/*`
