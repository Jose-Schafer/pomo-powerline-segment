# Instalation instructions
[![License](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](LICENSE)

----
Hope it helps someone to do his coding hours more productive. **(POMO timer on left)**

![POMO deactivated](/assets/img/Pomo1.png "Pomo Deactivated")
![POMO working](/assets/img/Pomo2.png "Pomo Working")
----

## Initial steps
1. Clone the repository
1. Install required python packages
    1. python3-watchdog
1. Install powerline
    ```
    Ubuntu: sudo apt install powerline
    ```
1. Create the following directory
    ```
    mkdir /home/<user>/.config/powerline/python_pomo
    ```
1. Create an empty file inside the created folder with name "pomo.txt"
1. Create the following command on .bashrc (Replace <user> by your user name)
    ```
    pomo() {
        rm /home/<user>/.config/powerline/python_pomo/pomo.txt; echo "pomo $1" > /home/<user>/.config/powerline/python_pomo/pomo.txt
    }
    ```

## Debug steps
1. Open custom_debug.py and run it.
1. In your shell run "pomo 2m"
1. Now you should see that the file "pomo.txt" was modified. 

## Final steps
1. In the folder where the repository was clonned run the following command:
    ```
    pip3 install --editable ./
    ```
1. In default.json of the powerline configuration (inside shell or tmux) add:
    ```
    {
        "function": "pomo_segment.custom.pomo",
        "priority": 10
    }
    ```
1. Finally run the following commando so the changes made in the powerline configuration are loaded:
    ```
    powerline-daemon --replace
    ```


----

## Powerline configuration
1. Add the following to .tmux.conf
```
source /usr/share/powerline/bindings/tmux/powerline.conf 
```
1. Run this commando so configurations can take place:
```
tmux source-file ~/.tmux.conf
```

1. the default.json mentioned in FINAL STEPS should be inside in a folder structur similar to this one:
```
/home/<user>/.config/powerline/themes/tmux/default.json
```
