

[Discord server](https://discord.gg/rX4A6YdXkt) | [YouTube](https://www.youtube.com/c/DuyFI) | [PyPI](https://pypi.org/project/donatello/)
# donatello.py
Donatello.py is a simple unofficial library for the Donatello API



# First step

#### Get [Donatello](https://donatello.to/panel/doc-api) API Token
![alt text](https://raw.githubusercontent.com/Beengoo/donatello.py/master/rm_imgs/1.png)
  1. Go to [Donatello API Docs](https://donatello.to/panel/doc-api)
  2. Enable API
  3. Copy Token

#### Example code:

```py
from donatello import Donatello

donate = Donatello(token="Your token here")

print(f"Hello my name is {donate.get_nickname()}, donate me pleace:)\n{donate.get_page()}")
```

## API Reference

#### Methods list


| Method   | Return | Description                                                            |
| :--------| :------| :----------------------------------------------------------------------|
| `me`     | `dict` | Return information about the user such as nickname, page, status, etc  |
| `donates`| `dict` | Return a list of donations                                             |
| `clients`| `dict` | Return a list of clients                                               |

#### Methods for quick access to information

| Method             | Return  | Description                                                                          |
| :------------------| :-------| :------------------------------------------------------------------------------------|
| `get_total_donates`| `int`   | Return a total count of donations                                                    |
| `get_full_info`    | `list`  | Return a `me`, `donates` and `clients` in list                                       |
| `get_nickname`     | `str`   | Return a nickname in Donatello                                                       |
| `get_donates`      | `dict`  | Return a total donations amount and count                                            |
| `created_at`       | `str`   | Return the date when the account was created in the format `yyyy-mm-dd hh:mm:ss`     |
| `get_status`       | `dict`  | Returns a dict with activity and privacy status `{'isActive':bool, 'isPublic': bool}`|
| `get_page`         | `str`   | Returns a link to the donation page                                                  |


