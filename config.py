log_file = "/var/log/pythonms.log"
run={
    "SMTPTester" : {"directory":"SMTPTester", "restart":False, "main_method":"main", "repository":"https://github.com/lupin012345/SMTPTester.git"},
    "epitech_api_flask" : {"repository":"https://github.com/lupin012345/epitech-api-public.git", "restart": False, "main_method":"app.run", "directory":"epitechApi", "flask":{"host":"0.0.0.0", "port":8081}},
    "poller" : {"repository":"https://github.com/lupin012345/link_poller.git", "restart": False, "main_method":"main", "directory":"link_poller"}
}

daemon={
    "port": 8888,
    "host": "0.0.0.0",
    "services_directory": "run"
}
