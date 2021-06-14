import stem

controller = stem.connection.connect(control_port = ('127.0.0.1', 'default'),
    control_socket = '/var/run/tor/control',
    password = 'password',)


controller.get_info('traffic/read', None)

controller.get_info('bw-event-cache', None)
