# Click To Partial

A Sublime Text 3 plugin to alt + click a partial path and open it.

## Installation

Add ```Default (OSX).sublime-mousemap``` file to ```~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/``` and add:
```
[
  {
      "button": "button1", 
      "count": 1, 
      "modifiers": ["alt"],
      "command": "click_to_partial"
  }
]
```

And:

_macOS_
```
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User/
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/click_to_partial.py
```

_Ubuntu_
```
cd ~/.config/sublime-text-3/Packages/User
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/click_to_partial.py
```


## Contribute

Click To Partial is a small utility created by [Tiago Alves](https://twitter.com/alvesjtiago) & [Filipe Pina](https://twitter.com/filipepina).
Any help on this project is more than welcome. Or if you find any problems, please comment or open an issue with as much information as you can provide.

