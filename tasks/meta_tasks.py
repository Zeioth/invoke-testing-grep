from invoke import task


@task
def apply_settings(ctx):
    """
    Applies changes in settings.py to all our applications and environments.
    """


@task
def stop_all_instances(ctx, env):
    """
    Shutdown all machines gracefuly, so we can perform critical maintenance.
    This operation will take several minutes.
    """


@task
def restart_all_instances(ctx, env):
    """
    Restart all machines gracefuly, just in case we need it (we shouldn't).
    This operation will take several minutes.
    """


@task
def end_stg(ctx):
    """
    Terminate the stg environment of all applications.
    """