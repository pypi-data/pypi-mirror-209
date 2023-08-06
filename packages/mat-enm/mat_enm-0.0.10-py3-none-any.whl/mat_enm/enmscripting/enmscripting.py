#!/usr/bin/python -tt
# To make Py2 code safer (more like Py3) by preventing implicit relative imports
from __future__ import absolute_import
from .private import session

"""
enm module  - allows execution of enm cli commands to an enm deployment
            - commands are entered as strings, including all parameters, as per entering a command in the web-cli
            - file import is supported as an optional parameter to be added to the execute function
            - the command result returned contains the result data as a list of Strings
            - the result also contains the http-response code and a file if the command exports a file

    Sample usage :
    session = enm.open("https://url.to.enm/","user","password")
    response = session.terminal().execute("cmedit get * ENodeBFunction.*")
    for line in response.get_output():
        print (line)
    enm.close(session)
"""


def open(url, username=None, password=None):
    """
    Opens a connection towards ENM CLI.

    The connection should be closed using close() if it is not required anymore.

    :param url:                 url of the enm deployment
    :param username:            username
    :param password:            password

    :raise: ValueError if username or password is invalid
            requests.exceptions.ConnectionError if there is an issue with the connection

    :return:                    EnmSession
    """
    return session._open_external_session(url, username, password)


def close(enm_session):
    """
    Closes the session to free the underlying resources
    :param enm_session:    EnmSession instance to be closed. This will terminate the Session contained
                          in this instance
    :return:              boolean, true if successfully closed
    """
    return session._close_session(enm_session)
