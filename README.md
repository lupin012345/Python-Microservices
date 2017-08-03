### PythonMS-CLI

Python MicroServices is a Python utility to manage your Python scripts of all kinds without the hassle of creating a service for each.

You can remotely deploy them using git, then access the console to check if they are up and running.
Monitor their state, automatically restart them in case of failure, log, kill, stop or restart them.

### How to use this?

#### Step 1
    Write your Python script    
![step1](https://github.com/lp1dev/Python-Microservices/blob/master/screens/step1.png?raw=true)
#### Step 2
    Add your repository's configuration to your config.py file
![step2](https://github.com/lp1dev/Python-Microservices/blob/master/screens/step2.png?raw=true)
#### Step 3
    Once you are connected to the console you can check your script's status with the list command
![step3](https://github.com/lp1dev/Python-Microservices/blob/master/screens/step3.png?raw=true)
#### Step 4
    Display your script's log using the log command
![step4](https://github.com/lp1dev/Python-Microservices/blob/master/screens/step4.png?raw=true)

## Requirements

- systemd
- Python3.4+
- pip (recommended)

## Setup

Install the required python modules

``` pip install -r requirements.txt ```

You can install PythonMS as a service as root using the pythonms.service (systemd compatible)

``` ln -s $PWD/pythonms.service /etc/systemd/system/ ```

## Configuration

Before starting to use PythonMS you must configure it. You can use the config.example.py for reference :

```
run={
"SMTPTester" : {"directory":"SMTPTester", "restart":False, "main_method":"main", "repository":"https://github.com/lp1dev/SMTPTester.git"},
    "epitech_api_flask" : {"repository":"https://github.com/lp1dev/epitech-api-public.git", "restart": False, "main_method":"app.run", "directory":"epitechApi", "flask":{"host":"0.0.0.0", "port":8081}},
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
