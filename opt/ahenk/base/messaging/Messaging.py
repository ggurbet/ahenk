#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Volkan Şahin <volkansah.in> <bm.volkansahin@gmail.com>
import datetime
import json
import os
import pwd
import sys

sys.path.append('../..')
from base.Scope import Scope


# TODO Message Factory
class Messaging(object):
    def __init__(self):
        scope = Scope().getInstance()
        self.logger = scope.getLogger()
        self.conf_manager = scope.getConfigurationManager()
        self.db_service = scope.getDbService()

        self.event_manger = scope.getEventManager()

    # TODO can use sh commands or api for getting username and timestamp

    def policy_request_msg(self):
        # TODO volkan

        self.logger.debug('[Messaging] Creating policy request message')

        ahenk_version = self.db_service.select('policy', ['version'], 'type = \'A\'')
        username = 'volkan'
        user_version = self.db_service.select('policy', ['version'], 'type = \'U\' and name = \'' + username + '\'')

        if len(ahenk_version) == 0:
            ahenk_version.append(-1)
        if len(user_version) == 0:
            user_version.append(-1)

        data = {}
        data['type'] = 'POLICY_REQUEST'
        data['username'] = username
        data['ahenkPolicyVersion'] = str(''.join(ahenk_version[0]))
        data['userPolicyVersion'] = str(''.join(user_version[0]))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Policy request message was created')
        print(json_data)
        return json_data

    def login_msg(self, username):
        data = {}
        data['type'] = 'LOGIN'
        data['username'] = username
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Login message was created')
        return json_data

    def logout_msg(self, username):
        data = {}
        data['type'] = 'LOGOUT'
        data['username'] = str(username)
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Logout message was created')
        return json_data

    def policies_msg(self):
        data = {}
        data['type'] = 'GET_POLICIES'
        data['username'] = str(pwd.getpwuid(os.getuid())[0])
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Get Policies message was created')
        return json_data

    def registration_msg(self):
        data = {}
        data['type'] = 'REGISTER'
        data['from'] = str(self.conf_manager.get('REGISTRATION', 'from'))
        data['password'] = str(self.conf_manager.get('REGISTRATION', 'password'))
        data['macAddresses'] = str(self.conf_manager.get('REGISTRATION', 'macAddresses'))
        data['ipAddresses'] = str(self.conf_manager.get('REGISTRATION', 'ipAddresses'))
        data['hostname'] = str(self.conf_manager.get('REGISTRATION', 'hostname'))
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Registration message was created')
        return json_data

    def ldap_registration_msg(self):
        data = {}
        data['type'] = 'REGISTER_LDAP'
        data['from'] = str(self.conf_manager.get('REGISTRATION', 'from'))
        data['password'] = str(self.conf_manager.get('REGISTRATION', 'password'))
        data['macAddresses'] = str(self.conf_manager.get('REGISTRATION', 'macAddresses'))
        data['ipAddresses'] = str(self.conf_manager.get('REGISTRATION', 'ipAddresses'))
        data['hostname'] = str(self.conf_manager.get('REGISTRATION', 'hostname'))
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] LDAP Registration message was created')
        return json_data

    def unregister_msg(self):
        data = {}
        data['type'] = 'UNREGISTER'
        data['from'] = str(self.conf_manager.get('REGISTRATION', 'from'))
        data['password'] = str(self.conf_manager.get('REGISTRATION', 'password'))
        data['macAddresses'] = str(self.conf_manager.get('REGISTRATION', 'macAddresses'))
        data['ipAddresses'] = str(self.conf_manager.get('REGISTRATION', 'ipAddresses'))
        data['hostname'] = str(self.conf_manager.get('REGISTRATION', 'hostname'))
        # data['username'] = str(pwd.getpwuid( os.getuid() )[ 0 ])
        data['timestamp'] = str(datetime.datetime.now().strftime("%d-%m-%Y %I:%M"))
        json_data = json.dumps(data)
        self.logger.debug('[Messaging] Unregister message was created')
        return json_data
