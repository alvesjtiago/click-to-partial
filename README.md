# Click To Partial

A Sublime Text 3 plugin to alt + click a partial path and open it.

## Installation

Click to partial has been submitted to Package Control and is waiting to be approved. This README file will be updated once it is possible to install Hover Preview via the Package Control.

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
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/Default%20(OSX).sublime-mousemap.py
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/click_to_partial.py
```

_Ubuntu_
```
cd ~/.config/sublime-text-3/Packages/User
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/Default%20(OSX).sublime-mousemap.py
curl -O https://raw.githubusercontent.com/alvesjtiago/click-to-partial/master/click_to_partial.py
```

Or manually copy the click_to_partial.py and Default (OSX).sublime-mousemap.py files to your User Packages folder.


## Contribute

Click To Partial is a small utility created by [Tiago Alves](https://twitter.com/alvesjtiago) & [Filipe Pina](https://twitter.com/filipepina).
Any help on this project is more than welcome. Or if you find any problems, please comment or open an issue with as much information as you can provide.

