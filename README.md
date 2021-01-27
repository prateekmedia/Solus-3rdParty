# 3rdParty Packages for Solus

# Archived
I am no longer willing to maintain the packages to the latest version as I no longer use them.  
You can use this as the template of your repo and maintain if you want.

## Disclaimer
These packages are **not official**, they are neither supported nor endorsed by the official Solus devs. Do not ask for help in Solus's help forum, instead create an issue [here](https://github.com/prateekmedia/Solus-3rdParty/issues).

## Direct .eopkg files(NEW)
Now you can directly download the compiled .eopkg files from [here](https://github.com/prateekmedia/Solus-3rdParty/releases/latest)

To install any program directly from eopkg file, First download the file and then `cd` into that folder like `$ cd ~/Downloads`, After that run  
```
$ sudo eopkg it ./your-program-name.eopkg
```
**NOTE** : Please read the release notes first to know if their are any extra dependencies or not

### Building from Source

**For Microsoft Edge Dev:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/browser/microsoft-edge-dev/pspec.xml && sudo eopkg it microsoft-edge-dev*.eopkg && sudo rm microsoft-edge-dev*.eopkg
```
**For Figma Linux:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/graphics/figma-linux/pspec.xml && sudo eopkg it figma-linux*.eopkg && sudo rm figma-linux*.eopkg
```
**For Magnus:**  
```
$ sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/graphics/magnus/pspec.xml && sudo eopkg it magnus*.eopkg && sudo rm magnus*.eopkg
```
