# Configuration file for jupyterhub.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterHub(Application) configuration
#------------------------------------------------------------------------------

## An Application for starting a Multi-User Jupyter Notebook server.

## Maximum number of concurrent servers that can be active at a time.
#  
#  Setting this can limit the total resources your users can consume.
#  
#  An active server is any server that's not fully stopped. It is considered
#  active from the time it has been requested until the time that it has
#  completely stopped.
#  
#  If this many user servers are active, users will not be able to launch new
#  servers until a server is shutdown. Spawn requests will be rejected with a 429
#  error asking them to try again.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.active_server_limit = 0

## Duration (in seconds) to determine the number of active users.
#c.JupyterHub.active_user_window = 1800

## Resolution (in seconds) for updating activity
#  
#  If activity is registered that is less than activity_resolution seconds more
#  recent than the current value, the new value will be ignored.
#  
#  This avoids too many writes to the Hub database.
#c.JupyterHub.activity_resolution = 30

## Grant admin users permission to access single-user servers.
#  
#  Users should be properly informed if this is enabled.
#c.JupyterHub.admin_access = False

## DEPRECATED since version 0.7.2, use Authenticator.admin_users instead.
#c.JupyterHub.admin_users = set()

## Allow named single-user servers per user
#c.JupyterHub.allow_named_servers = False

## Answer yes to any questions (e.g. confirm overwrite)
#c.JupyterHub.answer_yes = False

## PENDING DEPRECATION: consider using services
#  
#  Dict of token:username to be loaded into the database.
#  
#  Allows ahead-of-time generation of API tokens for use by externally managed
#  services, which authenticate as JupyterHub users.
#  
#  Consider using services for general services that talk to the JupyterHub API.
#c.JupyterHub.api_tokens = {}

## Authentication for prometheus metrics
#c.JupyterHub.authenticate_prometheus = True

## Class for authenticating users.
#  
#          This should be a subclass of :class:`jupyterhub.auth.Authenticator`
#  
#          with an :meth:`authenticate` method that:
#  
#          - is a coroutine (asyncio or tornado)
#          - returns username on success, None on failure
#          - takes two arguments: (handler, data),
#            where `handler` is the calling web.RequestHandler,
#            and `data` is the POST form data from the login page.
#  
#          .. versionchanged:: 1.0
#              authenticators may be registered via entry points,
#              e.g. `c.JupyterHub.authenticator_class = 'pam'`
#  
#  Currently installed: 
#    - default: jupyterhub.auth.PAMAuthenticator
#    - dummy: jupyterhub.auth.DummyAuthenticator
#    - pam: jupyterhub.auth.PAMAuthenticator
#c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
#c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
#c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
#c.PAMAuthenticator.open_sessions = False

# for LTI v1.2.0
c.JupyterHub.authenticator_class = 'ltiauthenticator.LTIAuthenticator'
#c.LTI11Authenticator.consumers = {"":""}

c.LTI11Authenticator.username_key = 'ext_user_username'             # for Moodle
#c.LTI11Authenticator.username_key = 'custom_lis_user_username'      # for Canvas or BlackBoard
#c.LTI11Authenticator.username_key = 'ext_d2l_username'              # for Desire2Learn
#c.LTI11Authenticator.username_key = 'lis_person_sourcedid'          # for Sakai


# for LDAP
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
#c.LDAPAuthenticator.server_address = '202.26.150.51'
#c.LDAPAuthenticator.server_address = '202.26.144.11'
#c.LDAPAuthenticator.use_ssl = True

## 大学の AD template 付き
#c.LDAPAuthenticator.lookup_dn = False
#c.LDAPAuthenticator.bind_dn_template = [
#    'cn={username},ou=教員,ou=ユーザー,dc=edutuis,dc=local',
#    'cn={username},ou=学生,ou=ユーザー,dc=edutuis,dc=local'
#]
#c.LDAPAuthenticator.user_search_base = 'dc=edutuis,dc=local'
#c.LDAPAuthenticator.user_attribute = 'sAMAccountName'

#
## 大学の AD template なし
#c.LDAPAuthenticator.lookup_dn = True
#c.LDAPAuthenticator.user_search_base = 'dc=edutuis,dc=local'
#c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
#c.LDAPAuthenticator.lookup_dn_search_user = 'cn=ldapauth,cn=users,dc=edutuis,dc=local'
#c.LDAPAuthenticator.lookup_dn_search_password = '*****'
#c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'

## NSL: username から dn が探せる場合
#c.LDAPAuthenticator.lookup_dn = False
#c.LDAPAuthenticator.bind_dn_template = 'cn={username},ou=user,dc=nsl,dc=tuis,dc=ac,dc=jp'

## NSL: ツリーを検索する場合
#c.LDAPAuthenticator.lookup_dn = True
#c.LDAPAuthenticator.user_search_base = 'ou=user,dc=nsl,dc=tuis,dc=ac,dc=jp'
#c.LDAPAuthenticator.user_attribute = 'uid'
#c.LDAPAuthenticator.lookup_dn_search_user = 'cn=Manager'
#c.LDAPAuthenticator.lookup_dn_search_password = '*******'
#c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'


## The base URL of the entire application.
#  
#  Add this to the beginning of all JupyterHub URLs. Use base_url to run
#  JupyterHub within an existing website.
#  
#  .. deprecated: 0.9
#      Use JupyterHub.bind_url
#c.JupyterHub.base_url = '/'

##
# My IP Address
#my_ip_addr = '172.22.1.75'
#my_ip_addr = '202.26.150.55'

## The public facing URL of the whole JupyterHub application.
#  
#  This is the address on which the proxy will bind. Sets protocol, ip, base_url
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'

## Whether to shutdown the proxy when the Hub shuts down.
#  
#  Disable if you want to be able to teardown the Hub while leaving the proxy
#  running.
#  
#  Only valid if the proxy was starting by the Hub process.
#  
#  If both this and cleanup_servers are False, sending SIGINT to the Hub will
#  only shutdown the Hub, leaving everything else running.
#  
#  The Hub should be able to resume from database state.
#c.JupyterHub.cleanup_proxy = True

## Whether to shutdown single-user servers when the Hub shuts down.
#  
#  Disable if you want to be able to teardown the Hub while leaving the single-
#  user servers running.
#  
#  If both this and cleanup_proxy are False, sending SIGINT to the Hub will only
#  shutdown the Hub, leaving everything else running.
#  
#  The Hub should be able to resume from database state.
#c.JupyterHub.cleanup_servers = True

## Maximum number of concurrent users that can be spawning at a time.
#  
#  Spawning lots of servers at the same time can cause performance problems for
#  the Hub or the underlying spawning system. Set this limit to prevent bursts of
#  logins from attempting to spawn too many servers at the same time.
#  
#  This does not limit the number of total running servers. See
#  active_server_limit for that.
#  
#  If more than this many users attempt to spawn at a time, their requests will
#  be rejected with a 429 error asking them to try again. Users will have to wait
#  for some of the spawning services to finish starting before they can start
#  their own.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.concurrent_spawn_limit = 100

## The config file to load
#c.JupyterHub.config_file = 'jupyterhub_config.py'

## DEPRECATED: does nothing
#c.JupyterHub.confirm_no_ssl = False

## Number of days for a login cookie to be valid. Default is two weeks.
#c.JupyterHub.cookie_max_age_days = 14

## The cookie secret to use to encrypt cookies.
#  
#  Loaded from the JPY_COOKIE_SECRET env variable by default.
#  
#  Should be exactly 256 bits (32 bytes).
#c.JupyterHub.cookie_secret = b''

## File in which to store the cookie secret.
#c.JupyterHub.cookie_secret_file = '/var/lib/jupyterhub/jupyterhub_cookie_secret'

## The location of jupyterhub data files (e.g. /usr/local/share/jupyterhub)
#c.JupyterHub.data_files_path = '/usr/local/anaconda/envs/jupyterhub38/share/jupyterhub'

## Include any kwargs to pass to the database connection. See
#  sqlalchemy.create_engine for details.
#c.JupyterHub.db_kwargs = {}

## url for the database. e.g. `sqlite:///jupyterhub.sqlite`
#c.JupyterHub.db_url = 'sqlite:////var/lib/jupyterhub/jupyterhub.sqlite'

## log all database transactions. This has A LOT of output
#c.JupyterHub.debug_db = False

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.debug
#c.JupyterHub.debug_proxy = False

## If named servers are enabled, default name of server to spawn or open, e.g. by
#  user-redirect.
#c.JupyterHub.default_server_name = ''

## The default URL for users when they arrive (e.g. when user directs to "/")
#  
#  By default, redirects users to their own server.
#c.JupyterHub.default_url = ''

## Dict authority:dict(files). Specify the key, cert, and/or ca file for an
#  authority. This is useful for externally managed proxies that wish to use
#  internal_ssl.
#  
#  The files dict has this format (you must specify at least a cert)::
#  
#      {
#          'key': '/path/to/key.key',
#          'cert': '/path/to/cert.crt',
#          'ca': '/path/to/ca.crt'
#      }
#  
#  The authorities you can override: 'hub-ca', 'notebooks-ca', 'proxy-api-ca',
#  'proxy-client-ca', and 'services-ca'.
#  
#  Use with internal_ssl
#c.JupyterHub.external_ssl_authorities = {}

## Register extra tornado Handlers for jupyterhub.
#  
#  Should be of the form ``("<regex>", Handler)``
#  
#  The Hub prefix will be added, so `/my-page` will be served at `/hub/my-page`.
#c.JupyterHub.extra_handlers = []

## DEPRECATED: use output redirection instead, e.g.
#  
#  jupyterhub &>> /var/log/jupyterhub.log

## Extra log handlers to set on JupyterHub logger
#c.JupyterHub.extra_log_handlers = []

## Generate certs used for internal ssl
#c.JupyterHub.generate_certs = False

## Generate default config file
#c.JupyterHub.generate_config = False

## The URL on which the Hub will listen. This is a private URL for internal
#  communication. Typically set in combination with hub_connect_url. If a unix
#  socket, hub_connect_url **must** also be set.
#  
#  For example:
#  
#      "http://127.0.0.1:8081"
#      "unix+http://%2Fsrv%2Fjupyterhub%2Fjupyterhub.sock"
#  
#  .. versionadded:: 0.9
c.JupyterHub.hub_bind_url = 'http://'+my_ip_addr+':8081'

## The ip or hostname for proxies and spawners to use for connecting to the Hub.
#  
#  Use when the bind address (`hub_ip`) is 0.0.0.0 or otherwise different from
#  the connect address.
#  
#  Default: when `hub_ip` is 0.0.0.0, use `socket.gethostname()`, otherwise use
#  `hub_ip`.
#  
#  Note: Some spawners or proxy implementations might not support hostnames.
#  Check your spawner or proxy documentation to see if they have extra
#  requirements.
#  
#  .. versionadded:: 0.8
c.JupyterHub.hub_connect_ip = my_ip_addr

## DEPRECATED
#  
#  Use hub_connect_url
#  
#  .. versionadded:: 0.8
#  
#  .. deprecated:: 0.9
#      Use hub_connect_url
#c.JupyterHub.hub_connect_port = 0

## The URL for connecting to the Hub. Spawners, services, and the proxy will use
#  this URL to talk to the Hub.
#  
#  Only needs to be specified if the default hub URL is not connectable (e.g.
#  using a unix+http:// bind url).
#  
#  .. seealso::
#      JupyterHub.hub_connect_ip
#      JupyterHub.hub_bind_url
#  
#  .. versionadded:: 0.9
#c.JupyterHub.hub_connect_url = ''

## The ip address for the Hub process to *bind* to.
#  
#  By default, the hub listens on localhost only. This address must be accessible
#  from the proxy and user servers. You may need to set this to a public ip or ''
#  for all interfaces if the proxy or user servers are in containers or on a
#  different host.
#  
#  See `hub_connect_ip` for cases where the bind and connect address should
#  differ, or `hub_bind_url` for setting the full bind URL.
#c.JupyterHub.hub_ip = '127.0.0.1'
c.JupyterHub.hub_ip = '0.0.0.0'

## The internal port for the Hub process.
#  
#  This is the internal port of the hub itself. It should never be accessed
#  directly. See JupyterHub.port for the public port to use when accessing
#  jupyterhub. It is rare that this port should be set except in cases of port
#  conflict.
#  
#  See also `hub_ip` for the ip and `hub_bind_url` for setting the full bind URL.
c.JupyterHub.hub_port = 8081

## Timeout (in seconds) to wait for spawners to initialize
#  
#  Checking if spawners are healthy can take a long time if many spawners are
#  active at hub start time.
#  
#  If it takes longer than this timeout to check, init_spawner will be left to
#  complete in the background and the http server is allowed to start.
#  
#  A timeout of -1 means wait forever, which can mean a slow startup of the Hub
#  but ensures that the Hub is fully consistent by the time it starts responding
#  to requests. This matches the behavior of jupyterhub 1.0.
#  
#  .. versionadded: 1.1.0
#c.JupyterHub.init_spawners_timeout = 10
c.JupyterHub.init_spawners_timeout = 30

## The location to store certificates automatically created by JupyterHub.
#  
#  Use with internal_ssl
#c.JupyterHub.internal_certs_location = 'internal-ssl'

## Enable SSL for all internal communication
#  
#  This enables end-to-end encryption between all JupyterHub components.
#  JupyterHub will automatically create the necessary certificate authority and
#  sign notebook certificates as they're created.
#c.JupyterHub.internal_ssl = False

## The public facing ip of the whole JupyterHub application (specifically
#  referred to as the proxy).
#  
#  This is the address on which the proxy will listen. The default is to listen
#  on all interfaces. This is the only address through which JupyterHub should be
#  accessed by users.
#  
#  .. deprecated: 0.9
#      Use JupyterHub.bind_url
#c.JupyterHub.ip = my_ip_addr

## Supply extra arguments that will be passed to Jinja environment.
#c.JupyterHub.jinja_environment_options = {}

## Interval (in seconds) at which to update last-activity timestamps.
#c.JupyterHub.last_activity_interval = 300

## Dict of 'group': ['usernames'] to load at startup.
#  
#  This strictly *adds* groups and users to groups.
#  
#  Loading one set of groups, then starting JupyterHub again with a different set
#  will not remove users or groups from previous launches. That must be done
#  through the API.
#c.JupyterHub.load_groups = {}

## Specify path to a logo image to override the Jupyter logo in the banner.
#c.JupyterHub.logo_file = ''

## Maximum number of concurrent named servers that can be created by a user at a
#  time.
#  
#  Setting this can limit the total resources a user can consume.
#  
#  If set to 0, no limit is enforced.
#c.JupyterHub.named_server_limit_per_user = 0

## File to write PID Useful for daemonizing JupyterHub.
#c.JupyterHub.pid_file = '/var/lib/jupyterhub/jupyterhub.pid'
#c.ConfigurableHTTPProxy.pid_file = '/var/lib/jupyterhub/jupyterhub-proxy.pid'
#c.JupyterHub.pid_file = '/var/run/jupyterhub.pid'
#c.ConfigurableHTTPProxy.pid_file = '/var/run/jupyterhub-proxy.pid'

## for Ltictr_Proxy
#c.JupyterHub.cleanup_proxy = False
#c.ConfigurableHTTPProxy.should_start = False
#c.ConfigurableHTTPProxy.api_url = 'http://localhost:8001'
#c.ConfigurableHTTPProxy.auth_token = "ABCDEFG"


## The public facing port of the proxy.
#  
#  This is the port on which the proxy will listen. This is the only port through
#  which JupyterHub should be accessed by users.
#  
#  .. deprecated: 0.9
#      Use JupyterHub.bind_url
#c.JupyterHub.port = 8000

## DEPRECATED since version 0.8 : Use ConfigurableHTTPProxy.api_url
#c.JupyterHub.proxy_api_ip = ''

## DEPRECATED since version 0.8 : Use ConfigurableHTTPProxy.api_url
#c.JupyterHub.proxy_api_port = 0

## DEPRECATED since version 0.8: Use ConfigurableHTTPProxy.auth_token
#c.JupyterHub.proxy_auth_token = ''

## Interval (in seconds) at which to check if the proxy is running.
#c.JupyterHub.proxy_check_interval = 30

## The class to use for configuring the JupyterHub proxy.
#  
#          Should be a subclass of :class:`jupyterhub.proxy.Proxy`.
#  
#          .. versionchanged:: 1.0
#              proxies may be registered via entry points,
#              e.g. `c.JupyterHub.proxy_class = 'traefik'`
#  
#  Currently installed: 
#    - configurable-http-proxy: jupyterhub.proxy.ConfigurableHTTPProxy
#    - default: jupyterhub.proxy.ConfigurableHTTPProxy
#c.JupyterHub.proxy_class = 'jupyterhub.proxy.ConfigurableHTTPProxy'

## DEPRECATED since version 0.8. Use ConfigurableHTTPProxy.command
#c.JupyterHub.proxy_cmd = []

## Recreate all certificates used within JupyterHub on restart.
#  
#  Note: enabling this feature requires restarting all notebook servers.
#  
#  Use with internal_ssl
#c.JupyterHub.recreate_internal_certs = False

## Redirect user to server (if running), instead of control panel.
#c.JupyterHub.redirect_to_server = True

## Purge and reset the database.
#c.JupyterHub.reset_db = False


#
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

#
# LTIDockerSpawner v1.0.2 for LTI by Fumi.Iseki
#
#                                      BSD License.
#

from dockerspawner import DockerSpawner

from traitlets import (
    Bool,
    Dict,
    List,
    Int,
    Unicode,
)

from urllib.parse import urlparse

import pwd, grp, os, sys, re


class LTIDockerSpawner(DockerSpawner):
    #
    use_group      = Bool(True, config = True)
    default_group  = Unicode('users', config = True)
    group_home_dir = Unicode('/home/{groupname}', config = True)
    user_home_dir  = Unicode('/home/{groupname}/{username}', config = True)
    projects_dir   = Unicode('jupyter', config = True)
    works_dir      = Unicode('works', config = True)
    volumes_dir    = Unicode('.volumes', config = True)
    teacher_gname  = Unicode('TEACHER', config = True)
    teacher_gid    = Int(7000,  config = True)
    base_id        = Int(30000, config = True)

    # extension command
    ext_user_id_cmd     = 'user_userid'
    ext_group_id_cmd    = 'user_groupid'
    ext_grp_name_cmd    = 'user_groupname'

    # custom command
    custom_image_cmd    = 'lms_image'
    custom_cpulimit_cmd = 'lms_cpulimit'
    custom_memlimit_cmd = 'lms_memlimit'
    custom_cpugrnt_cmd  = 'lms_cpugrnt'
    custom_memgrnt_cmd  = 'lms_memgrnt'
    custom_defurl_cmd   = 'lms_defurl'
    custom_users_cmd    = 'lms_users'
    custom_teachers_cmd = 'lms_teachers'
    custom_volumes_cmd  = 'lms_vol_'
    custom_submits_cmd  = 'lms_sub_'
    custom_prsnals_cmd  = 'lms_prs_'
    custom_iframe_cmd   = 'lms_iframe'
    custom_ssninfo_cmd  = 'lms_sessioninfo'
    custom_options_cmd  = 'lms_options'

    #
    user_id          = -1
    group_id         = -1
    grp_name         = ''
    lms_user_id      = -1    # LMS USER ID
    course_id        = '0'
    host_name        = ''
    host_url         = ''
    host_port        = 80
    userdata         = {}
    #
    ext_user_id      = -1
    ext_group_id     = -1
    ext_grp_name     = ''
    #
    custom_image     = ''
    custom_cpulimit  = '0.0'
    custom_memlimit  = '0'
    custom_cpugrnt   = '0.0'
    custom_memgrnt   = '0'
    custom_defurl    = '/lab'
    custom_users     = []
    custom_teachers  = []
    custom_volumes   = {}
    custom_submits   = {}
    custom_prsnals   = {}
    custom_iframe    = False
    custom_ltictr_id = 0
    custom_lti_id    = 0
    custom_options   = ''


    def init_parameters(self):
        #print('=== init_parameters() ===')
        self.user_id          = -1
        self.group_id         = -1
        self.grp_name         = ''
        self.lms_user_id      = -1
        self.course_id        = '0'
        self.host_name        = 'localhost'
        self.host_url         = 'http://localhost'
        self.host_port        = 80
        self.userdara         = {}
        #
        self.ext_user_id      = -1
        self.ext_group_id     = -1
        self.ext_grp_name     = ''
        #
        self.custom_image     = ''
        self.custom_cpulimit  = '0.0'
        self.custom_memlimit  = '0'
        self.custom_cpugrnt   = '0.0'
        self.custom_memgrnt   = '0'
        self.custom_defurl    = '/lab'
        self.custom_users     = []
        self.custom_teachers  = []
        self.custom_volumes   = {}
        self.custom_submits   = {}
        self.custom_prsnals   = {}
        self.custom_iframe    = False
        self.custom_ltictr_id = 0
        self.custom_lti_id    = 0
        self.custom_options   = ''
        #
        return


    def get_lms_userinfo(self):
        grp_name = self.default_group
        userinfo = {}
        #
        userinfo['uid']   = self.base_id + self.lms_user_id
        userinfo['gname'] = grp_name
        try :
            userinfo['gid'] = grp.getgrnam(grp_name).gr_gid
        except :
            userinfo['gid'] = self.base_id

        return userinfo


    def get_userid(self):
        if self.user_id < 0:
            try :
                self.user_id = pwd.getpwnam(self.user.name).pw_uid  # from system user account
            except :
                if self.ext_user_id>=0 :
                    self.user_id = self.ext_user_id                 # from extension command
                else :
                    self.user_id = self.get_lms_userinfo()['uid']   # form LMS user accound
        #
        return self.user_id


    def get_groupname(self):
        if self.group_id < 0:
            try :
                self.group_id = pwd.getpwnam(self.user.name).pw_gid # from system user account
            except :
                if self.ext_group_id>=0 :
                    self.group_id = self.ext_group_id               # from extension command
                else :
                    self.group_id = self.get_lms_userinfo()['gid']  # form LMS user accound
        #
        if self.use_group and self.group_id >= 0 :
            if self.grp_name == '' :
                try :
                    self.grp_name = grp.getgrgid(self.group_id).gr_name     # from system user account
                except :
                    if self.ext_grp_name != '' :
                        self.grp_name = self.ext_grp_name                   # from extension command
                    else :
                        self.grp_name = self.get_lms_userinfo()['gname']    # form LMS user accound
        #
        return self.grp_name


    def template_namespace(self):
        d = super(LTIDockerSpawner, self).template_namespace()
        d['groupname'] = self.get_groupname()
        return d


    @property
    def homedir(self):
        return self.user_home_dir.format(username=self.user.name, groupname=self.get_groupname())

    @property
    def groupdir(self):
        return self.group_home_dir.format(groupname=self.get_groupname())


    def get_args(self):
        #print('=== get_args() ===')
        args = super(LTIDockerSpawner, self).get_args()

        if self.custom_iframe :
            if sys.version_info >= (3, 8) : cookie_options = ', "cookie_options": { "SameSite": "None", "Secure": True }'
            else :                          cookie_options = ''
            #
            frame_ancestors = "frame-ancestors 'self' " + self.host_url
            args.append('--NotebookApp.tornado_settings={ "headers":{"Content-Security-Policy": "'+ frame_ancestors + '" }' + cookie_options + '}')
            #get_config().NotebookApp.disable_check_xsrf = True
        #
        args.append('--SingleUserNotebookApp.default_url=' + self.default_url)   # for jupyterhub (<2.00) in images
        return args


    def create_dir(self, directory, uid, gid, mode) :
        if not os.path.isdir(directory) :
            os.makedirs(directory)
            os.chown(directory, uid, gid)
            os.chmod(directory, mode)


    #def auth_hook(authenticator, handler, authentication):
    #    print('=== auth_hook() ===')
    #    return authentication


    #def spawn_hook(self):
    #    print('=== spawn_hook() ===')


    #
    # for custom/ext data
    # パラメータから情報を得る
    #
    def userdata_hook(self, auth_state):
        #print('=== userdata_hook() ===')
        self.userdata = auth_state              # raw data
        self.init_parameters()

        for key, value in self.userdata.items():

            if key == 'context_id' : self.course_id = value         # LMS Course ID (string)

            elif key == 'user_id'  : self.lms_user_id = int(value)  # LMS USER ID

            elif key == 'lis_outcome_service_url' :
                parsed = urlparse(value)
                self.host_name = parsed.netloc                      # Host Name
                scheme = parsed.scheme                              # HTTP Scheme
                self.host_url = scheme + '://' + self.host_name     # Host URL
                portnm = parsed.port
                if portnm is None :
                    if   scheme == 'https' : portnm = 443
                    elif scheme == 'http'  : portnm = 80
                self.host_port = portnm
                #
            elif key.startswith('ext_'):                            # Extension Command
                ext_cmd = key.replace('ext_', '')
                #
                if ext_cmd == self.ext_user_id_cmd:                                             # User ID Command
                    value = re.sub('[^0-9]', '', value)
                    if value != '' : self.ext_user_id = int(value)
                #
                elif ext_cmd == self.ext_group_id_cmd:                                          # User Group ID Command
                    value = re.sub('[^0-9]', '', value)
                    if value != '' : self.ext_group_id = int(value)
                #
                elif ext_cmd == self.ext_grp_name_cmd:                                          # User Group Name Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.ext_grp_name = value
                #
            elif key.startswith('custom_'):                         # Custom Command
                costom_cmd = key.replace('custom_', '')
                #
                if costom_cmd == self.custom_image_cmd:                                         # Container Image Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~ ]', '', value)
                    self.custom_image = value
                #
                elif costom_cmd == self.custom_users_cmd:                                       # Users Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_users = value.replace(',',' ').split()
                #
                elif costom_cmd[0:len(self.custom_teachers_cmd)] == self.custom_teachers_cmd:   # Teachers Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_teachers = value.replace(',',' ').split()
                #
                elif costom_cmd[0:len(self.custom_cpugrnt_cmd)] == self.custom_cpugrnt_cmd:     # CPU Limit Guarantee Command
                    value = re.sub('[^0-9\.]', '', value)
                    self.custom_cpugrnt = value
                #
                elif costom_cmd[0:len(self.custom_memgrnt_cmd)] == self.custom_memgrnt_cmd:     # Memory Guarantee Command
                    value = re.sub('[^0-9]', '', value)
                    self.custom_memgrnt = value
                #
                elif costom_cmd[0:len(self.custom_cpulimit_cmd)] == self.custom_cpulimit_cmd:   # CPU Limit Command
                    value = re.sub('[^0-9\.]', '', value)
                    self.custom_cpulimit = value
                #
                elif costom_cmd[0:len(self.custom_memlimit_cmd)] == self.custom_memlimit_cmd:   # Memory Limit Command
                    value = re.sub('[^0-9]', '', value)
                    self.custom_memlimit = value
                #
                elif costom_cmd == self.custom_defurl_cmd:                                      # Default URL Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~ ]', '', value)
                    self.custom_defurl = value
                #
                elif costom_cmd[0:len(self.custom_options_cmd)] == self.custom_options_cmd:     # Option Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_options = value
                #
                elif costom_cmd[0:len(self.custom_volumes_cmd)] == self.custom_volumes_cmd:     # Volumes Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_volumes[costom_cmd] = value
                #
                elif costom_cmd[0:len(self.custom_submits_cmd)] == self.custom_submits_cmd:     # Submits Volume Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_submits[costom_cmd] = value
                #
                elif costom_cmd[0:len(self.custom_prsnals_cmd)] == self.custom_prsnals_cmd:     # Personals Volume Command
                    value = re.sub('[;$\!\"\'&|\\<>?^%\(\)\{\}\n\r~\/ ]', '', value)
                    self.custom_prsnals[costom_cmd] = value
                #
                elif costom_cmd[0:len(self.custom_iframe_cmd)] == self.custom_iframe_cmd:       # iframe Command
                    if value == '1' :
                        self.custom_iframe = True
                #
                elif costom_cmd[0:len(self.custom_ssninfo_cmd)] == self.custom_ssninfo_cmd:     # sessioninfo Command
                    value = re.sub('[^0-9]', ' ', value)
                    self.custom_ltictr_id = value.split()[0]
                    self.custom_lti_id    = value.split()[1]
                #
        return


    #
    # ユーザのアクセス情報をチェックし，マウントする課題ボリュームのパスの配列を返す．
    #
    def get_volumes_info(self, assoc):
        #print('=== get_volumes_info() ===')
        vols = []
        for key, value in assoc.items():
            usrs = []
            disp = ''
            lst  = value.split(':')
            num  = len(lst)

            if num > 0 : disp = lst[0]
            if num > 1 : usrs = lst[1].replace(',',' ').split()

            if disp != '' :
                mnt = False
                if len(usrs) != 0 :                                                         # : によるアクセス制限の指定あり
                    if ('*' in usrs) or (self.user.name in usrs) :
                        mnt = True
                elif ('*' in self.custom_users) or (self.user.name in self.custom_users) :  # : によるアクセス制限の指定なし
                    mnt = True
                elif (self.user.name in self.custom_teachers) :                             # 教師
                    mnt = True

                if mnt:
                    dirname = key + '_' + self.course_id + '_' + self.host_name
                    vols.append(self.volumes_dir + '/' + dirname + ':' + disp)
        #
        return vols


    #
    # コンテナに渡す環境変数を設定する．
    # NB_UID, NB_GID, NB_USER, NB_GROUP, NB_UMASK, NB_VOLUMES, NB_SUBMITS, NB_PRSNAL,
    # NB_TEACHER, NB_THRGROUP, NB_THRGID, ...
    #
    def get_env(self):
        #print('=== get_env() ===')
        env = super(LTIDockerSpawner, self).get_env()

        userid    = self.get_userid()
        username  = self.user.name
        groupname = self.get_groupname()
        groupid   = self.group_id

        env.update(NB_UID       = userid)
        env.update(NB_USER      = username)
        env.update(NB_GID       = groupid)
        env.update(NB_GROUP     = groupname)
        env.update(NB_DIR       = self.notebook_dir.format(username=username, groupname=groupname))

        env.update(NB_THRGID    = self.teacher_gid)
        env.update(NB_THRGROUP  = self.teacher_gname)
        env.update(NB_OPTION    = self.custom_options)
        env.update(NB_HOSTNAME  = self.host_name)
        if (self.user.name in self.custom_teachers) :
            env.update(NB_UMASK = '0033')
            env.update(NB_TEACHER = self.user.name)
        else:
            env.update(NB_TEACHER = '')

        # volumes
        volumes = ' '.join(self.get_volumes_info(self.custom_volumes))
        env.update(NB_VOLUMES = volumes)

        submits = ' '.join(self.get_volumes_info(self.custom_submits))
        env.update(NB_SUBMITS = submits)

        prsnals = ' '.join(self.get_volumes_info(self.custom_prsnals))
        env.update(NB_PRSNALS = prsnals)

        return env


    #
    # START LTIDockerSpawner
    #
    def start(self):
        #print('=== start() ===')
        username  = self.user.name
        groupname = self.get_groupname()    # get self.group_id, too
        hosthome  = self.homedir
        grouphome = self.groupdir
        self.notebook_dir = hosthome
        self.volumes = {}

        course_id = self.course_id
        lti_id    = self.custom_lti_id
        host_name = self.host_name
        self.object_name = f'jupyterhub-{username}-{course_id}-{lti_id}-{host_name}'

        # cpu and memory
        if self.custom_cpugrnt != '':
            self.cpu_guarantee = float(self.custom_cpugrnt)
        #
        if self.custom_memgrnt != '':
            self.mem_guarantee = int(self.custom_memgrnt)
        #
        if self.custom_cpulimit != '':
            self.cpu_limit     = float(self.custom_cpulimit)
        #
        if self.custom_memlimit != '':
            self.mem_limit     = int(self.custom_memlimit)

        # image
        if self.custom_image != '':
            self.image = self.custom_image

        # default url
        if self.custom_defurl != '':
            self.default_url = self.custom_defurl

        # volume
        self.volumes[hosthome] = hosthome

        self.create_dir(grouphome, 0, self.group_id, 0o0755)
        self.create_dir(hosthome,  self.user_id, self.group_id, 0o0700)
        self.create_dir(hosthome + '/' + self.projects_dir,  self.user_id, self.group_id, 0o0700)
        self.create_dir(hosthome + '/' + self.projects_dir + '/' + self.works_dir, self.user_id, self.group_id, 0o0700)

        fullpath_dir  = hosthome + '/' + self.projects_dir + '/' + self.works_dir
        mount_volumes = self.get_volumes_info(self.custom_volumes)
        mount_submits = self.get_volumes_info(self.custom_submits)

        for volume in mount_volumes:
            mountp  = volume.rsplit(':')[0]
            dirname = mountp.split('/')[-1]
            self.volumes[dirname] = fullpath_dir + '/' + mountp

        for submit in mount_submits:
            mountp  = submit.rsplit(':')[0]
            dirname = mountp.split('/')[-1]
            self.volumes[dirname] = fullpath_dir + '/' + mountp

        #
        self.remove = True

        #print('=== START LTIDockerSpawner ===')
        return super(LTIDockerSpawner, self).start()


    #def stop(self, now=True):
    #    return super(LTIDockerSpawner, self).stop(now)


    #def get_cmdmand(self):
    #    cmd = super(LTIDockerSpawner, self).get_cmdmand()
    #    return cmd
    #
    #    '''
    #    if self._user_set_cmd:
    #        cmd = self.cmd
    #    else:
    #        image_info = yield self.docker("inspect_image", self.image)
    #        cmd = image_info["Config"]["Cmd"]
    #    return cmd + self.get_args()
    #    '''


    #def docker(self, method, *args, **kwargs):
    #    #return self.executor.submit(self._docker, method, *args, **kwargs)
    #    return super(LTIDockerSpawner, self).docker(method, *args, **kwargs)



#
# LTIDockerSpawner Parameters
#

c.LTIDockerSpawner.use_group = True

# Volumes are mounted at /user_home_dir/projects_dir/works_dir/volumes_dir
default_group  = 'others'                       # ホストに存在しないユーザ（ID不明）のグループ（予め作って置く）
group_home_dir = '/home/{groupname}'
user_home_dir  = group_home_dir + '/{username}'
projects_dir   = 'jupyter'
works_dir      = 'works'
volumes_dir    = '.volumes'
#
teacher_gid    = 7000                           # 1000以上で，システムで使用していない GID
base_id        = 30000                          # ID 不明の場合に，基底となる ID番号．システムで使用されていない部分．

time_zone      = 'JST-9'

#
notebook_dir = user_home_dir
c.LTIDockerSpawner.default_group = default_group
c.LTIDockerSpawner.user_home_dir = user_home_dir
c.LTIDockerSpawner.projects_dir  = projects_dir
c.LTIDockerSpawner.works_dir     = works_dir
c.LTIDockerSpawner.volumes_dir   = volumes_dir
c.LTIDockerSpawner.teacher_gid   = teacher_gid
c.LTIDockerSpawner.base_id       = base_id

#
c.Spawner.environment = {
    'GRANT_SUDO'      : 'no',                   # 通常使用では 'no'
    'PRJCT_DIR'       : projects_dir,
    'WORK_DIR'        : works_dir,
    'VOLUME_DIR'      : volumes_dir,
    'NB_UMASK'        : '0037',
    'CONDA_DIR'       : '/opt/conda',
    'TZ'              : time_zone,
    'CHOWN_HOME'      : 'yes',
    'CHOWN_HOME_OPTS' : '-R',
}

# CHOWN_EXTRA, CHOWN_EXTRA_OPTS


#
# culler and admin-service
#
#c.JupyterHub.services = [
#    # culler
#    {
#        'name': 'idle-culler',
#        'admin': True,
#        'command': [
#            sys.executable,
#            '/usr/local/bin/cull_idle_servers.py',
#            '--timeout=1200'
#        ],
#    },
#
#    # admin-service
#    {
#        'name': 'admin-service',
#        'api_token': '',    # at least 8 characters
#    },
#]

#
# role of admin-service
#
#c.JupyterHub.load_roles = [
#    {
#        "name": "service-role",
#        "scopes": [
#            "admin:users",
#        ],
#        "services": [
#            "admin-service",
#        ],
#   }
#]


#
# for iframe
#
iframe_url = 'http://*'                          # iframe Host URL

c.JupyterHub.tornado_settings = { "headers":{ "Content-Security-Policy": "frame-ancestors 'self' " + iframe_url } }

# if you charenge to show iframe, uncomment bellow 3 lines.
#if sys.version_info >= (3, 8) :
#   cookie_options = { "SameSite": "None", "Secure": True }
#   c.JupyterHub.tornado_settings["cookie_options"] = cookie_options


#
c.Exchange.timestamp_format = '%Y%m%d %H:%M:%S %Z'
c.Exchange.timezone = time_zone


#
#c.NbGrader.logfile = "/var/log/nbgrader.log"
#c.Exchange.root = '/home/share/nbgrader/exchange'

#
## Interval (in seconds) at which to check connectivity of services with web
#  endpoints.
#c.JupyterHub.service_check_interval = 60

## Dict of token:servicename to be loaded into the database.
#  
#  Allows ahead-of-time generation of API tokens for use by externally managed
#  services.
#c.JupyterHub.service_tokens = {}

## List of service specification dictionaries.
#  
#  A service
#  
#  For instance::
#  
#      services = [
#          {
#              'name': 'cull_idle',
#              'command': ['/path/to/cull_idle_servers.py'],
#          },
#          {
#              'name': 'formgrader',
#              'url': 'http://127.0.0.1:1234',
#              'api_token': 'super-secret',
#              'environment':
#          }
#      ]
#c.JupyterHub.services = []


## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.JupyterHub.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.JupyterHub.show_config_json = False

## Shuts down all user servers on logout
c.JupyterHub.shutdown_on_logout = True


## The class to use for spawning single-user servers.
#  
#          Should be a subclass of :class:`jupyterhub.spawner.Spawner`.
#  
#          .. versionchanged:: 1.0
#              spawners may be registered via entry points,
#              e.g. `c.JupyterHub.spawner_class = 'localprocess'`
#  
#  Currently installed: 
#    - default: jupyterhub.spawner.LocalProcessSpawner
#    - localprocess: jupyterhub.spawner.LocalProcessSpawner
#    - simple: jupyterhub.spawner.SimpleLocalProcessSpawner
#    - docker: dockerspawner.DockerSpawner
#    - docker-swarm: dockerspawner.SwarmSpawner
#    - docker-system-user: dockerspawner.SystemUserSpawner
#c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
#c.JupyterHub.spawner_class = 'coursewareuserspawner.CoursewareUserSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.SwarmSpawner'
#c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'
c.JupyterHub.spawner_class = LTIDockerSpawner

#c.DockerSpawner.image = 'niicloudoperation/jupyterhub-singleuser'
#c.DockerSpawner.image = 'niicloudoperation/notebook'
#c.DockerSpawner.image = 'jupyter/datascience-notebook'
#c.DockerSpawner.image = 'jupyterhub/singleuser'
#c.DockerSpawner.image = 'www.nsl.tuis.ac.jp:5000/jupyterhub-ltictr/jupyter-singleuser'

#c.DockerSpawner.image_whitelist = {
#    "deepdetect-gpu (Tensorflow+PyTorch)": "jolibrain/jupyter-dd-notebook-gpu",
#    "tensorflow-2-gpu (Tensorflow 2.0)": "d4n1el/tensorflow-2-notebook-gpu",
#    "datascience-gpu (Python+Julia+R)": "d4n1el/datascience-notebook-gpu",
#    "tensorflow-cpu (Tensorflow)": "jupyter/tensorflow-notebook",
#    "datascience-cpu (Python+Julia+R)": "jupyter/datascience-notebook",
#    "TEST" : "jupyterhub-test"
#}

c.DockerSpawner.remove = True
c.DockerSpawner.extra_create_kwargs = {'user': 'root'}          # root or rootless mode
c.DockerSpawner.extra_host_config = {'privileged': True}
c.DockerSpawner.network_name = 'jupyterhub-network'
#c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}
#notebook_dir = '/home/jovyan/work'
#notebook_dir = '/home/{username}/work'

c.DockerSpawner.notebook_dir = notebook_dir
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

#from jupyter_client.localinterfaces import public_ips
#c.JupyterHub.hub_ip = public_ips()[0]

#c.DockerSpawner.args = ['--username={username}']
#c.SystemUserSpawner.args = ['--user-name={username}', '--test']

##
#c.DockerSpawner.image = 'jupyterhub/singleuser'
#c.DockerSpawner.remove = True
#c.DockerSpawner.extra_create_kwargs = {'user': 'root'}
#c.Spawner.environment = {'GRANT_SUDO': 'yes'}
#notebook_dir = '/home/jovyan/work'
#c.DockerSpawner.notebook_dir = notebook_dir
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

#from jupyter_client.localinterfaces import public_ips

## Path to SSL certificate file for the public facing interface of the proxy
#  
#  When setting this, you should also set ssl_key
#c.JupyterHub.ssl_cert = '/etc/gitlab/ssl/gitlab.crt'
#c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/gitlab.nsl.tuis.ac.jp/cert.pem'
#c.JupyterHub.ssl_cert = '/etc/pki/tls/certs/server.pem'
#c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/jupyterhub01.nsl.tuis.ac.jp/cert.pem'

## Path to SSL key file for the public facing interface of the proxy
#  
#  When setting this, you should also set ssl_cert
#c.JupyterHub.ssl_key = '/etc/gitlab/ssl/gitlab.key'
#c.JupyterHub.ssl_key = '/etc/letsencrypt/live/gitlab.nsl.tuis.ac.jp/privkey.pem'
#c.JupyterHub.ssl_key = '/etc/pki/tls/private/key.pem' 
#c.JupyterHub.ssl_key = '/etc/letsencrypt/live/jupyterhub01.nsl.tuis.ac.jp/privkey.pem'

## Host to send statsd metrics to. An empty string (the default) disables sending
#  metrics.
#c.JupyterHub.statsd_host = ''

## Port on which to send statsd metrics about the hub
#c.JupyterHub.statsd_port = 8125

## Prefix to use for all metrics sent by jupyterhub to statsd
#c.JupyterHub.statsd_prefix = 'jupyterhub'

## Run single-user servers on subdomains of this host.
#  
#  This should be the full `https://hub.domain.tld[:port]`.
#  
#  Provides additional cross-site protections for javascript served by single-
#  user servers.
#  
#  Requires `<username>.hub.domain.tld` to resolve to the same host as
#  `hub.domain.tld`.
#  
#  In general, this is most easily achieved with wildcard DNS.
#  
#  When using SSL (i.e. always) this also requires a wildcard SSL certificate.
#c.JupyterHub.subdomain_host = ''

## Paths to search for jinja templates, before using the default templates.
#c.JupyterHub.template_paths = []

## Extra variables to be passed into jinja templates
#c.JupyterHub.template_vars = {}

## Extra settings overrides to pass to the tornado application.
#c.JupyterHub.tornado_settings = {}

## Trust user-provided tokens (via JupyterHub.service_tokens) to have good
#  entropy.
#  
#  If you are not inserting additional tokens via configuration file, this flag
#  has no effect.
#  
#  In JupyterHub 0.8, internally generated tokens do not pass through additional
#  hashing because the hashing is costly and does not increase the entropy of
#  already-good UUIDs.
#  
#  User-provided tokens, on the other hand, are not trusted to have good entropy
#  by default, and are passed through many rounds of hashing to stretch the
#  entropy of the key (i.e. user-provided tokens are treated as passwords instead
#  of random keys). These keys are more costly to check.
#  
#  If your inserted tokens are generated by a good-quality mechanism, e.g.
#  `openssl rand -hex 32`, then you can set this flag to True to reduce the cost
#  of checking authentication tokens.
#c.JupyterHub.trust_user_provided_tokens = False

## Names to include in the subject alternative name.
#  
#  These names will be used for server name verification. This is useful if
#  JupyterHub is being run behind a reverse proxy or services using ssl are on
#  different hosts.
#  
#  Use with internal_ssl
#c.JupyterHub.trusted_alt_names = []

## Downstream proxy IP addresses to trust.
#  
#  This sets the list of IP addresses that are trusted and skipped when
#  processing the `X-Forwarded-For` header. For example, if an external proxy is
#  used for TLS termination, its IP address should be added to this list to
#  ensure the correct client IP addresses are recorded in the logs instead of the
#  proxy server's IP address.
#c.JupyterHub.trusted_downstream_ips = []

## Upgrade the database automatically on start.
#  
#  Only safe if database is regularly backed up. Only SQLite databases will be
#  backed up to a local file automatically.
#c.JupyterHub.upgrade_db = False

## Callable to affect behavior of /user-redirect/
#  
#  Receives 4 parameters: 1. path - URL path that was provided after /user-
#  redirect/ 2. request - A Tornado HTTPServerRequest representing the current
#  request. 3. user - The currently authenticated user. 4. base_url - The
#  base_url of the current hub, for relative redirects
#  
#  It should return the new URL to redirect to, or None to preserve current
#  behavior.
#c.JupyterHub.user_redirect_hook = None

#------------------------------------------------------------------------------
# Spawner(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Base class for spawning single-user notebook servers.
#  
#  Subclass this, and override the following methods:
#  
#  - load_state - get_state - start - stop - poll
#  
#  As JupyterHub supports multiple users, an instance of the Spawner subclass is
#  created for each user. If there are 20 JupyterHub users, there will be 20
#  instances of the subclass.

## Extra arguments to be passed to the single-user server.
#  
#  Some spawners allow shell-style expansion here, allowing you to use
#  environment variables here. Most, including the default, do not. Consult the
#  documentation for your spawner to verify!
#c.Spawner.args = []

## An optional hook function that you can implement to pass `auth_state` to the
#  spawner after it has been initialized but before it starts. The `auth_state`
#  dictionary may be set by the `.authenticate()` method of the authenticator.
#  This hook enables you to pass some or all of that information to your spawner.
#  
#  Example::
#  
#      def userdata_hook(spawner, auth_state):
#          spawner.userdata = auth_state["userdata"]
#  
#      c.Spawner.auth_state_hook = userdata_hook
#c.Spawner.auth_state_hook = None
c.Spawner.auth_state_hook = LTIDockerSpawner.userdata_hook

## The command used for starting the single-user server.
#  
#  Provide either a string or a list containing the path to the startup script
#  command. Extra arguments, other than this path, should be provided via `args`.
#  
#  This is usually set if you want to start the single-user server in a different
#  python environment (with virtualenv/conda) than JupyterHub itself.
#  
#  Some spawners allow shell-style expansion here, allowing you to use
#  environment variables. Most, including the default, do not. Consult the
#  documentation for your spawner to verify!
#c.Spawner.cmd = ['jupyterhub-singleuser']

## Maximum number of consecutive failures to allow before shutting down
#  JupyterHub.
#  
#  This helps JupyterHub recover from a certain class of problem preventing
#  launch in contexts where the Hub is automatically restarted (e.g. systemd,
#  docker, kubernetes).
#  
#  A limit of 0 means no limit and consecutive failures will not be tracked.
#c.Spawner.consecutive_failure_limit = 0

## Minimum number of cpu-cores a single-user notebook server is guaranteed to
#  have available.
#  
#  If this value is set to 0.5, allows use of 50% of one CPU. If this value is
#  set to 2, allows use of up to 2 CPUs.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#c.Spawner.cpu_guarantee = None

## Maximum number of cpu-cores a single-user notebook server is allowed to use.
#  
#  If this value is set to 0.5, allows use of 50% of one CPU. If this value is
#  set to 2, allows use of up to 2 CPUs.
#  
#  The single-user notebook server will never be scheduled by the kernel to use
#  more cpu-cores than this. There is no guarantee that it can access this many
#  cpu-cores.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#c.Spawner.cpu_limit = None

## Enable debug-logging of the single-user server
#c.Spawner.debug = False

## The URL the single-user server should start in.
#  
#  `{username}` will be expanded to the user's username
#  
#  Example uses:
#  
#  - You can set `notebook_dir` to `/` and `default_url` to `/tree/home/{username}` to allow people to
#    navigate the whole filesystem from their notebook server, but still start in their home directory.
#  - Start with `/notebooks` instead of `/tree` if `default_url` points to a notebook instead of a directory.
#  - You can set this to `/lab` to have JupyterLab start by default, rather than Jupyter Notebook.
c.Spawner.default_url = '/lab'

## Disable per-user configuration of single-user servers.
#  
#  When starting the user's single-user server, any config file found in the
#  user's $HOME directory will be ignored.
#  
#  Note: a user could circumvent this if the user modifies their Python
#  environment, such as when they have their own conda environments / virtualenvs
#  / containers.
#c.Spawner.disable_user_config = False

## Whitelist of environment variables for the single-user server to inherit from
#  the JupyterHub process.
#  
#  This whitelist is used to ensure that sensitive information in the JupyterHub
#  process's environment (such as `CONFIGPROXY_AUTH_TOKEN`) is not passed to the
#  single-user server's process.
#c.Spawner.env_keep = ['PATH', 'PYTHONPATH', 'CONDA_ROOT', 'CONDA_DEFAULT_ENV', 'VIRTUAL_ENV', 'LANG', 'LC_ALL']

## Extra environment variables to set for the single-user server's process.
#  
#  Environment variables that end up in the single-user server's process come from 3 sources:
#    - This `environment` configurable
#    - The JupyterHub process' environment variables that are whitelisted in `env_keep`
#    - Variables to establish contact between the single-user notebook and the hub (such as JUPYTERHUB_API_TOKEN)
#  
#  The `environment` configurable should be set by JupyterHub administrators to
#  add installation specific environment variables. It is a dict where the key is
#  the name of the environment variable, and the value can be a string or a
#  callable. If it is a callable, it will be called with one parameter (the
#  spawner instance), and should return a string fairly quickly (no blocking
#  operations please!).
#  
#  Note that the spawner class' interface is not guaranteed to be exactly same
#  across upgrades, so if you are using the callable take care to verify it
#  continues to work after upgrades!
#c.Spawner.environment = {}

## Timeout (in seconds) before giving up on a spawned HTTP server
#  
#  Once a server has successfully been spawned, this is the amount of time we
#  wait before assuming that the server is unable to accept connections.
#c.Spawner.http_timeout = 30
c.Spawner.http_timeout = 60

## The IP address (or hostname) the single-user server should listen on.
#  
#  The JupyterHub proxy implementation should be able to send packets to this
#  interface.
#c.Spawner.ip = ''

## Minimum number of bytes a single-user notebook server is guaranteed to have
#  available.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#c.Spawner.mem_guarantee = None

## Maximum number of bytes a single-user notebook server is allowed to use.
#  
#  Allows the following suffixes:
#    - K -> Kilobytes
#    - M -> Megabytes
#    - G -> Gigabytes
#    - T -> Terabytes
#  
#  If the single user server tries to allocate more memory than this, it will
#  fail. There is no guarantee that the single-user notebook server will be able
#  to allocate this much memory - only that it can not allocate more than this.
#  
#  **This is a configuration setting. Your spawner must implement support for the
#  limit to work.** The default spawner, `LocalProcessSpawner`, does **not**
#  implement this support. A custom spawner **must** add support for this setting
#  for it to be enforced.
#c.Spawner.mem_limit = None

## Path to the notebook directory for the single-user server.
#  
#  The user sees a file listing of this directory when the notebook interface is
#  started. The current interface does not easily allow browsing beyond the
#  subdirectories in this directory's tree.
#  
#  `~` will be expanded to the home directory of the user, and {username} will be
#  replaced with the name of the user.
#  
#  Note that this does *not* prevent users from accessing files outside of this
#  path! They can do so with many other means.
#c.Spawner.notebook_dir = '/home/jupyter'
#c.Spawner.notebook_dir = '~/notebook'

## An HTML form for options a user can specify on launching their server.
#  
#  The surrounding `<form>` element and the submit button are already provided.
#  
#  For example:
#  
#  .. code:: html
#  
#      Set your key:
#      <input name="key" val="default_key"></input>
#      <br>
#      Choose a letter:
#      <select name="letter" multiple="true">
#        <option value="A">The letter A</option>
#        <option value="B">The letter B</option>
#      </select>
#  
#  The data from this form submission will be passed on to your spawner in
#  `self.user_options`
#  
#  Instead of a form snippet string, this could also be a callable that takes as
#  one parameter the current spawner instance and returns a string. The callable
#  will be called asynchronously if it returns a future, rather than a str. Note
#  that the interface of the spawner class is not deemed stable across versions,
#  so using this functionality might cause your JupyterHub upgrades to break.
#c.Spawner.options_form = traitlets.Undefined

## Interval (in seconds) on which to poll the spawner for single-user server's
#  status.
#  
#  At every poll interval, each spawner's `.poll` method is called, which checks
#  if the single-user server is still running. If it isn't running, then
#  JupyterHub modifies its own state accordingly and removes appropriate routes
#  from the configurable proxy.
#c.Spawner.poll_interval = 30

## The port for single-user servers to listen on.
#  
#  Defaults to `0`, which uses a randomly allocated port number each time.
#  
#  If set to a non-zero value, all Spawners will use the same port, which only
#  makes sense if each server is on a different address, e.g. in containers.
#  
#  New in version 0.7.
#c.Spawner.port = 0

## An optional hook function that you can implement to do work after the spawner
#  stops.
#  
#  This can be set independent of any concrete spawner implementation.
#c.Spawner.post_stop_hook = None

## An optional hook function that you can implement to do some bootstrapping work
#  before the spawner starts. For example, create a directory for your user or
#  load initial content.
#  
#  This can be set independent of any concrete spawner implementation.
#  
#  This maybe a coroutine.
#  
#  Example::
#  
#      from subprocess import check_call
#      def my_hook(spawner):
#          username = spawner.user.name
#          check_call(['./examples/bootstrap-script/bootstrap.sh', username])
#  
#      c.Spawner.pre_spawn_hook = my_hook
#c.Spawner.pre_spawn_hook = None
#c.Spawner.pre_spawn_hook = LTIDockerSpawner.spawn_hook

## List of SSL alt names
#  
#  May be set in config if all spawners should have the same value(s), or set at
#  runtime by Spawner that know their names.
#c.Spawner.ssl_alt_names = []

## Whether to include DNS:localhost, IP:127.0.0.1 in alt names
#c.Spawner.ssl_alt_names_include_local = True

## Timeout (in seconds) before giving up on starting of single-user server.
#  
#  This is the timeout for start to return, not the timeout for the server to
#  respond. Callers of spawner.start will assume that startup has failed if it
#  takes longer than this. start should return when the server process is started
#  and its location is known.
#c.Spawner.start_timeout = 60
c.Spawner.start_timeout = 120

#------------------------------------------------------------------------------
# Authenticator(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Base class for implementing an authentication provider for JupyterHub

## Set of users that will have admin rights on this JupyterHub.
#  
#  Admin users have extra privileges:
#   - Use the admin panel to see list of users logged in
#   - Add / remove users in some authenticators
#   - Restart / halt the hub
#   - Start / stop users' single-user servers
#   - Can access each individual users' single-user server (if configured)
#  
#  Admin access should be treated the same way root access is.
#  
#  Defaults to an empty set, in which case no user has admin access.
#c.Authenticator.admin_users = set()
c.Authenticator.admin_users = {'admin'}

## The max age (in seconds) of authentication info before forcing a refresh of
#  user auth info.
#  
#  Refreshing auth info allows, e.g. requesting/re-validating auth tokens.
#  
#  See :meth:`.refresh_user` for what happens when user auth info is refreshed
#  (nothing by default).
#c.Authenticator.auth_refresh_age = 300

## Automatically begin the login process
#  
#  rather than starting with a "Login with..." link at `/hub/login`
#  
#  To work, `.login_url()` must give a URL other than the default `/hub/login`,
#  such as an oauth handler or another automatic login handler, registered with
#  `.get_handlers()`.
#  
#  .. versionadded:: 0.8
#c.Authenticator.auto_login = False

## Blacklist of usernames that are not allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can not log in.
#  This is an additional blacklist that further restricts users, beyond whatever
#  restrictions the authenticator has in place.
#  
#  If empty, does not perform any additional restriction.
#  
#  .. versionadded: 0.9
#c.Authenticator.blacklist = set()

## Enable persisting auth_state (if available).
#  
#  auth_state will be encrypted and stored in the Hub's database. This can
#  include things like authentication tokens, etc. to be passed to Spawners as
#  environment variables.
#  
#  Encrypting auth_state requires the cryptography package.
#  
#  Additionally, the JUPYTERHUB_CRYPT_KEY environment variable must contain one
#  (or more, separated by ;) 32B encryption keys. These can be either base64 or
#  hex-encoded.
#  
#  If encryption is unavailable, auth_state cannot be persisted.
#  
#  New in JupyterHub 0.8
#c.Authenticator.enable_auth_state = False
c.Authenticator.enable_auth_state = True

os.environ['JUPYTERHUB_CRYPT_KEY'] = 'c283a5e73c8f74cdc8c6fef5415f1c97948a5a5450b5dc7524b9939093a2bd1d'

## An optional hook function that you can implement to do some bootstrapping work
#  during authentication. For example, loading user account details from an
#  external system.
#  
#  This function is called after the user has passed all authentication checks
#  and is ready to successfully authenticate. This function must return the
#  authentication dict reguardless of changes to it.
#  
#  This maybe a coroutine.
#  
#  .. versionadded: 1.0
#  
#  Example::
#  
#      import os, pwd
#      def my_hook(authenticator, handler, authentication):
#          user_data = pwd.getpwnam(authentication['name'])
#          spawn_data = {
#              'pw_data': user_data
#              'gid_list': os.getgrouplist(authentication['name'], user_data.pw_gid)
#          }
#  
#          if authentication['auth_state'] is None:
#              authentication['auth_state'] = {}
#          authentication['auth_state']['spawn_data'] = spawn_data
#  
#          return authentication
#  
#      c.Authenticator.post_auth_hook = my_hook
#c.Authenticator.post_auth_hook = None
#c.Authenticator.post_auth_hook = LTIDockerSpawner.auth_hook

## Force refresh of auth prior to spawn.
#  
#  This forces :meth:`.refresh_user` to be called prior to launching a server, to
#  ensure that auth state is up-to-date.
#  
#  This can be important when e.g. auth tokens that may have expired are passed
#  to the spawner via environment variables from auth_state.
#  
#  If refresh_user cannot refresh the user auth data, launch will fail until the
#  user logs in again.
#c.Authenticator.refresh_pre_spawn = False

## Dictionary mapping authenticator usernames to JupyterHub users.
#  
#  Primarily used to normalize OAuth user names to local users.
#c.Authenticator.username_map = {}

## Regular expression pattern that all valid usernames must match.
#  
#  If a username does not match the pattern specified here, authentication will
#  not be attempted.
#  
#  If not set, allow any username.
#c.Authenticator.username_pattern = ''

## Whitelist of usernames that are allowed to log in.
#  
#  Use this with supported authenticators to restrict which users can log in.
#  This is an additional whitelist that further restricts users, beyond whatever
#  restrictions the authenticator has in place.
#  
#  If empty, does not perform any additional restriction.
#c.Authenticator.whitelist = set()

#------------------------------------------------------------------------------
# CryptKeeper(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## Encapsulate encryption configuration
#  
#  Use via the encryption_config singleton below.

## 
#c.CryptKeeper.keys = []

## The number of threads to allocate for encryption
#c.CryptKeeper.n_threads = 16

