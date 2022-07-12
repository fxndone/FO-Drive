# FO - Drive

---

### Easy designed drive system that allow you to remotely save your files on a server

---

FO - Drive let you save your files on a remote server (that you can take [here](https://github.com/fxndone/FO-Drive_Server)) and retrieve them with a simple interface and a really easy setup.

You don't trust me ?

Let's try it out !

Simply check the server [README.md](https://github.com/fxndone/FO-Drive_Server/blob/main/README.md) and follow the steps.

After you've setup your server, simply grab the url, the username and the password, and create your "config.cfg" file following this example :

```
    URL=https://your.server/the/path/you/set
    USER=yourusername
    DIRECTORY=localdirectory
```

Where :

 - `URL` is your remote server URL
 - `USER` is the username you configured earlier on your server
 - `DIRECTORY` is your local directory that will be linked to the remote server one (every change on this local directory will appear on the server)

After that, run [main.py](https://github.com/fxndone/FO-Drive/blob/main/main.py) locally :

    python main.py

And... that it !

The setup is finished, and now, every time you launch [main.py](https://github.com/fxndone/FO-Drive/blob/main/main.py) it will copy your saved files from the server, and every time you close it (without brutal close), it will send changes to the server !

Feel free to update this as you wish !

Please remember that, even if it's not a pentesting tool, this tool should not be used in any illegal purpose, and I'me not responsible for any sh*t you could do with it.

For any recommendations or bugs, feel free to use the comment sections.

---