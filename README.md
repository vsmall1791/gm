# gm

A simple and very TOS-following python script for saying: "gm" to your friends in Discord

## Setup

To use this, follow these steps:

1. Clone the repository.
2. Install the discord.py library using pip:

```bash
pip install discord.py-self
```
3. Open the `gm.py` file and insert your Discord user token and friends' information as instructed in the file.

## Format

The script expects the friends' information in the following format:

```python
frens = {
    "friend_id" : "friend_name",
    # add as many friends as you want
}
```

## Getting a Friend's ID

To obtain your friend's ID, you need to follow these steps:

1. In your Discord settings, go to the 'Appearance' tab.
2. Scroll down to the 'Advanced' section.
3. Turn on 'Developer Mode'. This will allow you to copy IDs.
4. Exit out of your settings.
5. Right-click on your friend's username.
6. Click 'Copy ID'.

The copied ID is what you will use as the `friend_id` in the `frens` dictionary.

## Getting your Discord Token

Your Discord authentication token can be found with the following steps:

1. Open Discord on a web browser.
2. Open Developer console.
3. Click on the Network tab.
4. Reload the page.
5. In the filter bar type "/api".
6. Click on different entries until you find one that has an 'authorization' attribute, copy that token and use that in the script.

***WARNING***: DO NOT share your token as it can be used by someone to access your account.

## Running the script

Run the script using Python:

```bash
python gm.py "Your message here"
```

## License

This project is licensed under the terms of the MIT License. See [LICENSE](LICENSE) for more details.
