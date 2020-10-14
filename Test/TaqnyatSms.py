import http.client
import mimetypes
import json


class client:
  auth = ''
  base = 'api.taqnyat.sa'
  result=''
  method=''
  json ={}
  error =''

  def __init__(self, auth):
    self.auth = auth
  def checkUserInfo(self):
    if self.auth:
      self.json.update({'auth' : self.auth})
    else:
      self.error = 'Add Authentication'
      return self.error 
  def sendMsg(self,body, recipients, sender , scheduled ):
    self.checkUserInfo()
    #getSendMethod
    
    if not self.error:
      data = {
        'recipients': recipients,
        'sender': sender,
        'body': body,
        'scheduled': scheduled,
      }
      self.json.update(data)
      self.json = json.dumps(self.json)   

      conn = http.client.HTTPSConnection(self.base)
      headers = {
      'Authorization': 'Bearer ' + self.auth,
      'Content-Type': 'application/json'
      }


      conn.request("POST", "/v1/messages", self.json, headers)
      res = conn.getresponse()
      data = res.read()
      return data.decode("utf-8")

    else:
      return self.error
  def sendStatus(self ):
    self.checkUserInfo()
    #getSendMethod
    
    if not self.error:
      data = {
      }
      self.json.update(data)
      self.json = json.dumps(self.json)   

      conn = http.client.HTTPSConnection(self.base)
      headers = {
      'Authorization': 'Bearer ' + self.auth,
      'Content-Type': 'application/json'
      }


      conn.request("GET", "/system/status", self.json, headers)
      res = conn.getresponse()
      data = res.read()
      return data.decode("utf-8")

    else:
      return self.error
  def balance(self ):
    self.checkUserInfo()
    #getSendMethod
    
    if not self.error:
      data = {
      }
      self.json.update(data)
      self.json = json.dumps(self.json)   

      conn = http.client.HTTPSConnection(self.base)
      headers = {
      'Authorization': 'Bearer ' + self.auth,
      'Content-Type': 'application/json'
      }


      conn.request("GET", "/account/balance", self.json, headers)
      res = conn.getresponse()
      data = res.read()
      return data.decode("utf-8")

    else:
      return self.error
  def senders(self ):
      self.checkUserInfo()
      #getSendMethod
      
      if not self.error:
        data = {
        }
        self.json.update(data)
        self.json = json.dumps(self.json)   

        conn = http.client.HTTPSConnection(self.base)
        headers = {
        'Authorization': 'Bearer ' + self.auth,
        'Content-Type': 'application/json'
        }


        conn.request("GET", "/v1/messages/senders", self.json, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

      else:
        return self.error
  def deleteMsg(self , deleteKey ):
      self.checkUserInfo()
      #getSendMethod
      
      if not self.error:
        data = {
        }
        self.json.update(data)
        self.json = json.dumps(self.json)   

        conn = http.client.HTTPSConnection(self.base)
        headers = {
        'Authorization': 'Bearer ' + self.auth,
        'Content-Type': 'application/json'
        }


        conn.request("DELETE", "/v1/messages", self.json, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

      else:
        return self.error
