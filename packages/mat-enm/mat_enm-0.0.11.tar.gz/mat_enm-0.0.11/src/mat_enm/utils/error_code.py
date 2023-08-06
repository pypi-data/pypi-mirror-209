# ENM Lib Error Codes

STATUS = {
    "OK":{
        "status": True,
        "code":10000,
        "description":"Successfully"
    },
    "SUCCESS_TO_AUTHENTICATED":{
        "status": True,
        "code":10001,
        "description":"Successfully Authenticated"
    },
    "FAIL_TO_CONNECT":{
        "status": False,
        "code":30001,
        "description": ""
    },
    "FAIL_TO_AUTHENTICATED":{
        "status": False,
        "code":30002,
        "description": "Authentication failed"
    },
    "INVALID_COMMAND":{
        "status": False,
        "code":30020,
        "description": "Invalid command"
    },
    "FAIL_WHILE_EXECUTING_COMMAND":{
        "status": False,
        "code":30021,
        "description":"Fail while execute command"
    },
    "FILE_DOES_NOT_EXIST":{
        "status": False,
        "code":30030,
        "description":"File does not exist"
    },
    "PARSE_ERROR":{
        "status": False,
        "code":30040,
        "description":"Error parsing output"
    },
    "UNKNOW_ERROR":{
        "status": False,
        "code":30099,
        "description":"Unknow error"
    },

}