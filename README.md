# gm
A simply and very TOS-following python script for saying: "gm"

## Setup

To use this, follow these steps:

1. Clone the repository.
2. Install the discord.py library using pip:

```bash
pip install discord.py-self
```
3. Open the `gm.py` file and insert your Discord user token and friends' information as instructed in the file.

## Format

The bot expects the friends' information in the following format:

```python
friends = {
    "friend_id" : "friend_name",
    # add as many friends as you want
}
```

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
