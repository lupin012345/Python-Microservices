### PythonMS-CLI

Python MicroService is a Python utility to manage your Python scripts.

You can remotely check if they are up and running, their state, automatically restart them in case of failure and log and kill, stop or restart them.

## Requirements

- Python3.4
- Pip (recommended)

## Setup

Install the required python modules

``` pip install -r requirements.txt ```

You can install PythonMS as a service as root using the pythonms.service (systemd compatible)

``` ln -s $PWD/pythonms.service /etc/systemd/system/ ```

## Configuration

Before starting to use PythonMS you must configure it. You can use the config.example.py for reference :

```
run={
"SMTPTester" : {"directory":"SMTPTester", "restart":False, "main_method":"main", "repository":"https://github.com/lup\
in012345/SMTPTester.git"},
    "epitech_api_flask" : {"repository":"https://github.com/lupin012345/epitech-api-public.git", "restart": False, "main_\
method":"app.run", "directory":"epitechApi", "flask":{"host":"0.0.0.0", "port":8081}},
"myScript" : {"directory":"myscript_dir", "restart":True, "main_method":"run"}
}

daemon={
    "port": 4242,
    "host": "127.0.0.1",
    "services_directory": "run",
    "password": "password",
    "log_file": "/var/log/pythonms.log"
}
```

### Usage

Once you run PythonMS with the ```pythonms``` Python script, it listens on the selected port.

I'm not sure there exactly a need for a PythonMS client since the Netcat package can do everything I'd like a client to do.

That's why I recommend to use telnet or netcat to interact with your PythonMS server, for instance :

```nc your_host your_port```

You will then be prompted for your password, enter it

```
### Python Manager
Hello !
(password)
#> your_password
```

You can now use the following commands in the prompt :

- quit : Kill the running daemon and server
- list : List the services you added to the server
- start {id}: Start one of your services
- kill {id}: Kill one of your services
- status {id}: Show informations about one of your services
- restart : Restart the daemon and server. To refresh your configuration for example
- clear : Clear the screen
- keepalive {id} {True|False} : Choose if a service should be automatically restarted or not
- log : Print the contents of the logfile
- reclone : Delete the directory of a service and clone it again