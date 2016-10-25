run={
    "SMTPTester" : {"directory":"SMTPTester", "restart":False, "main_method":"main", "repository":"https://github.com/lupin012345/SMTPTester.git"},
}

daemon={
    "port": 4242,
    "host": "127.0.0.1",
    "services_directory": "run",
    "password": "password",
    "log_file": "/var/log/pythonms.log"
}
