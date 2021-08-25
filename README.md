<div align="center">
<a target="_blank" href="https://github.com/ASHWIN990/template">
<img alt="template logo" src="https://i.ibb.co/YBjWLR3/scrshot-2021-08-24-19-10-05.png" />
</a></div>

<h3 align="center">A script to generate template files from CLI 🖥️</h3>

<p markdown="1">

**template** is a PYTHON Script to handle **_Template files_** from the fancy of your terminal screen, it's annoying when you have to create a _bash script_ or a _HTML_ document you have to create a file and make the file executable if neccessary, but using this you dont have to deal with all of that just a single command and you're sorted.

</p>

<div align="center">
    <b>template</b> will create a file and the boilerplate.
</div>

## Prerequisite

* Install ```python3``` for your distro

Generally ```python3``` can be installed with package name ```python3``` 

## Installation

**Arch linux** and **Arch based distro** (**_AUR_**)

- yay -S [template](https://aur.archlinux.org/packages/template/)
- pamac install [template](https://aur.archlinux.org/packages/template/)

**Normal Installation**

```bash
git clone https://github.com/ASHWIN990/template.git

cd template

sudo make install
```

**Uninstallation**

```
sudo make uninstall
```

## Usage

```bash
$ template -f bash -n test.sh -x
    # Above command will create a 'Bash script' with file name 'test.sh' and due to -x flag the file will be exucutable.

$ template -f html
    # Above command will create a 'HTML Doc', with file name 'index.html'.

$ template -l
    # Above command will print the Available templates.
    # Output :
    # Available Templates are:-

    # Language   File Name
    # --------------------
    # python     script.py
    # bash       script.sh
    # c          main.c
    # html       index.html

```

## Options
```bash

  -h,  --help       Show this help message and exit
  -f   FILE TYPE    Provide the Template type
  -n   FILE NAME    Provide the desired File name
  -x                Make the new file executable
  -l                List the available Templates
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support Me

<a href="https://www.buymeacoffee.com/ashwinisahu" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Author

* **[ASHWINI SAHU](https://ashwini.codes)**
* **Email me at : *ashwinisahu990@gmail.com***
* **Follow me at : *[Instagram](https://instagram.com/kumar_ashwin_sahu) , [Twitter](https://twitter.com/ashwinisahu990)***
