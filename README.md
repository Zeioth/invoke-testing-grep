# invoke-testing-grep

Tested terminals: xfce4-terminal, x-terminal-emulator

Running 

    inv -l | grep meta
    
Result:

    meta.apply_settings          Applies changes in settings.py to all our
    meta.end_stg                 Terminate the stg environment of all
    meta.restart_all_instances   Restart all machines gracefuly, just in case we
    meta.stop_all_instances      Shutdown all machines gracefuly, so we can

Running 

    inv -l | grep -A1 meta
    
Result:

    meta.apply_settings          Applies changes in settings.py to all our
                                 applications and environments.
    meta.end_stg                 Terminate the stg environment of all
                                 applications.
    meta.restart_all_instances   Restart all machines gracefuly, just in case we
                                 need it (we shouldn't).
    meta.stop_all_instances      Shutdown all machines gracefuly, so we can
                                 perform critical maintenance.
