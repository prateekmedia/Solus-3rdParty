# 3rdParty Packages for Solus
### Disclaimer
These packages are **not official**, they are neither supported nor endorsed by the official Solus devs. Do not ask for help in Solus's help forum, instead create an issue [here](https://github.com/prateekmedia/Solus-3rdParty/issues).

### To install any program from this repo
```
$ sudo eopkg bi --ignore-safety ${program pspec.xml  url}

$ sudo eopkg it ${program_name}*.eopkg

$ sudo rm ${program_name}*.eopkg
```
***where ${program_name} = name of the package without spaces like `microsoft-edge-dev` && ${program pspec.xml  url} = url of pspec.xml for that package which look like this `https://raw.githubusercontent.com/prateekmedia/Solus-3rdParty/main/{PATH}/pspec.xml`***

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
