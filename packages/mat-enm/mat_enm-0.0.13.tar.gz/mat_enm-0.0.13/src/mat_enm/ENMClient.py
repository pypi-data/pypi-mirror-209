from mat import *
import mat_enm.enmscripting as enmscripting
import requests
import json
import time

import re

from mat_enm.utils.error_code import *
from mat_enm.utils.constants import *
from mat_enm.utils.cm_command_type import *

class ENMClient():
    def __init__(self, mat_host, mat_credential=None):
        
        inv = Inventory()
        
        mathost = inv.get("mathost", query=f"data.hostname={mat_host}")
        if not mathost:
            raise Exception("Debe ingresar una host correcto")
        mathost = mathost[0]
        
        if mat_credential:
            matcredentials = inv.get("matcredentials", query=f"data.credentialName={mat_credential}")
            if not matcredentials:
                raise Exception("Debe ingresar una credencial correcta")
            matcredentials = matcredentials[0]
        else:
            matcredentials = mathost['data'].get('storedCredentials')
            
        ip = mathost["data"]["managementIp"]
        username = matcredentials["data"]["username"]
        password = matcredentials["data"]["password"]
        
        url = f"https://{ip}/" # Por default usa la ip
        var_list = mathost["data"]["env_vars"]
        for var in var_list:
            if var["name"] == "url": url = var["value"]
        
        self._ip = ip
        self._url = url
        self._user = username
        self._password = crypto.aes256.MATCipher().decrypt(password)
        self._file_timeout = 1800
        self._session = None
    
    def parse_response_alarm_get(self, table):
        output = []
        req = type('parseTable', (object,), {})()
                
        res = STATUS['OK']
        description = table.pop()
        table  = [row for row in table if row != '']
        if len(table) < 2:
            req.status = res['status']
            req.code = res['code']
            req.description = description
            req.output = output
        
        title_list = table[0].split('\t')
        
        for row in table[1:]:
            col_list = row.split('\t')
            
            item = {}
            for index,title in enumerate(title_list):
                item.update({title: col_list[index]})
            output.append(item)
        
        req.status = res['status']
        req.code = res['code']
        req.description = description
        req.output = output
        
        return req
    
    def parse_response_cmedit_get(self, lines):
        obj = {}
        elem_list = []
        for line in lines:
            if 'FDN' in line:
                elem_list.append(obj)
                elem = line.split(':')
                if len(elem) == 2: obj = {elem[0].strip(): elem[1].strip()}
            else:
                elem = line.split(':')
                if len(elem) == 2: obj.update({elem[0].strip(): elem[1].strip()})
        elem_list.append(obj)
        elem_list.pop(0)
        
        if not elem_list:
            if '0 instance' in lines[1]:
                res = STATUS['OK']
                output = elem_list
            else:
                res = STATUS['PARSE_ERROR']
                output =  lines
        else:
            res = STATUS['OK']
            output =  elem_list
    
        req = type('parseOutput', (object,), {})()
        req.status = res['status']
        req.code = res['code']
        req.description = res['description']
        req.output = output
            
        return req
    
    def parse_response_cmedit_describe(self, lines):
        obj = {}
        lines = [line for line in lines if 'instance' not in line and line != ""]
        split_item = lines[0]
        elem_list = []
        for line in lines:
            if line == split_item:
                elem_list.append(obj)
                obj = {}
            else:
                elem = line.split(':')
                key = elem[0].strip()
                value = elem[1].strip() if len(elem) == 2 else ""
                obj.update({key: value})
        elem_list.append(obj)
        elem_list.pop(0)
        
        if not elem_list:
            if '0 instance' in lines[1]:
                res = STATUS['OK']
                output = elem_list
            else:
                res = STATUS['PARSE_ERROR']
                output =  lines
        else:
            res = STATUS['OK']
            output =  elem_list
    
        req = type('parseOutput', (object,), {})()
        req.status = res['status']
        req.code = res['code']
        req.description = res['description']
        req.output = output
            
        return req
    
    def parse_output(self, response):
        output = response.get_output()
        
        for item in output:
            error = re.findall("Error \d+", item)
            if error:
                error_code_list = item.split(':', 1)
                error_code = error_code_list[0].replace('Error', '').strip()
                try:
                    code = 30000 + int(error_code)
                except Exception as e:
                    code = 30099
                
                error = error_code_list[1].strip()
                
                solution = ""
                for item in output:
                    sol = re.findall("Suggested Solution", item)
                    if sol:
                        solution = item.strip()
                
                if error_code == '9999':
                    solution += "Suggested Solution : Check if there is a configuration pending to activate in the node."
                
                return {'status': False, 'code': str(code), 'description': f'{error}. {solution}'.strip()}
            elif "Invalid Command" in item:
                res = STATUS['INVALID_COMMAND']
                res['description'] = item
                return res
        
        return STATUS['OK']
    
    
    def open(self):
        if self._session == None:
            self._session = enmscripting.open(self._url, self._user, self._password)
        return self._session
    
    def close(self):
        enmscripting.close(self._session)
        self._session = None 
    
        
    def test_credential(self):       
        headers = {'Content-Type':'application/json'}
        logindata = {'IDToken1':self._user, 'IDToken2': self._password}
        try:
            enm_session = requests.Session()
            req = enm_session.post(self._url + 'login', data=logindata, verify=False)
            if req.status_code ==  200:
                req = json.loads(req.text)
                if req["code"] == "SUCCESS":
                    res = STATUS['SUCCESS_TO_AUTHENTICATED']
                else:
                    res = STATUS['FAIL_TO_AUTHENTICATED']
            else:
                res = STATUS['FAIL_TO_AUTHENTICATED']
        except Exception as e:
            res = STATUS['FAIL_TO_CONNECT']
            res['description'] = e
        finally:
            req = type('authenticationOutput', (object,), {})()
            req.status = res['status']
            req.code = res['code']
            req.description = res['description']
            return req
    
    def execute_command(self, command, path=None, timeout = 20,close_conn=True):
        session = self.open()
        terminal = session.terminal()
        
        command = command.rstrip()
        response = terminal.execute(command)
    
        while not response.is_command_result_available() and i < timeout:
            time.sleep(1)
            i += 1
        
        if "--download" in command and path:
            if response.has_files():
                for file in response.files():
                    file.download(path=path)
        
        res = self.parse_output(response)
        if close_conn: 
            self.close()
        
        command_type = [command_type for command_type in command_type_list if command_type in command]
        if command_type:
            command_type = command_type[0]
        else:
            command_type = "execute_command"
        
        response.status = res['status']
        response.code = res['code']
        response.description = res['description']

        return response
