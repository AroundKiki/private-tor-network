import stem


def main(config):
  config.set('start_time', str(int(time.time())))

  try:
    args = nyx.arguments.parse(sys.argv[1:])
    config.set('logged_events', args.logged_events)
  except ValueError as exc:
    print(exc)
    sys.exit(1)

  if args.print_help:
    print(nyx.arguments.get_help())
    sys.exit()
  elif args.print_version:
    print(nyx.arguments.get_version())
    sys.exit()

  if args.debug_path is not None:
    try:
      _setup_debug_logging(args)
      print('Saving a debug log to %s, please check it for sensitive information before sharing it.' % args.debug_path)
    except IOError as exc:
      print('Unable to write to our debug log file (%s): %s' % (args.debug_path, exc.strerror))
      sys.exit(1)

  if os.path.exists(args.config):
    try:
      config.load(args.config)
    except IOError as exc:
      stem.util.log.warn('Failed to load configuration (using defaults): "%s"' % exc.strerror)
  else:
    # TODO: move this url to 'nyx_config.sample' when we're about to issue another release

    stem.util.log.notice('No nyx configuration loaded, using defaults. You can customize nyx by placing a configuration file at %s (see https://nyx.torproject.org/nyxrc.sample for its options).' % args.config)

  # If a password is provided via the user's nyx configuration that will be use, otherwise
  # users are prompted for a password if required.

  controller_password = config.get('password', None)

  if controller_password:
    stem.connection.CONNECT_MESSAGES['incorrect_password'] = 'Unable to authenticate to tor using the controller password in %s' % args.config

  controller = init_controller(           ##连接成功后的实例
    control_port = args.control_port,
    control_socket = args.control_socket,
    password = controller_password,
    password_prompt = True,
    chroot_path = nyx.chroot(),
  )

  if controller is None:
    exit(1)

  if args.debug_path is not None:
    torrc_path = controller.get_info('config-file')

    try:
      with open(torrc_path) as torrc_file:
        torrc_content = torrc_file.read()
    except Exception as exc:
      torrc_content = 'Unable to read %s: %s' % (torrc_path, exc)

    stem.util.log.trace(TORRC.format(torrc_path = torrc_path, torrc_content = torrc_content))

  use_acs = config.get('acs_support', True)

  _warn_if_root(controller)
  _warn_if_unable_to_get_pid(controller)
  _use_unicode()
  _set_process_name()
  _warn_about_unused_config_keys()

  # These os.putenv calls fail on FreeBSD, and even attempting causes python to
  # print the following to stdout...
  #
  #   nyx: environment corrupt; missing value for

  if not stem.util.system.is_bsd():
    os.putenv('LANG', 'C')  # make subcommands (ps, netstat, etc) provide english results
    os.putenv('ESCDELAY', '0')  # make 'esc' take effect right away

  try:
    nyx.curses.start(nyx.draw_loop, acs_support = use_acs, transparent_background = True, cursor = False)     ##开始绘制图形界面
  except KeyboardInterrupt:
    pass  # skip printing a stack trace
  finally:
    nyx.curses.halt()
    _shutdown_daemons(controller)
