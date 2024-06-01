- Install clink
- Add clink in path
- Add auto run
```shell
clink autorun install
```
- Disable clink from cmder

- Install oh_my_posh
- Download and set a nerd font
- Copy code in clink folder, named "oh-my-posh.lua"
```lua
load(io.popen('oh-my-posh init cmd --config C:/Users/Posh/quick-term.omp.json'):read("*a"))()
-- ou load(io.popen('oh-my-posh init cmd --config C:/Users/Foxinow/AppData/Local/Programs/oh-my-posh/themes/quick-term.omp.json'):read("*a"))()
```

wsl:
- sudo chmod 777 usr/local/bin/
- curl -s https://ohmyposh.dev/install.sh | bash -s
- dans barshrc : eval "$(oh-my-posh init bash --config /mnt/c/Users/Foxinow/AppData/Local/Programs/oh-my-posh/themes/quick-term.omp.json)"