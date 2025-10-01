from TaqnyatSms import *


bearer = '**************************0adc2b'
taqnyatClient = client(bearer)
status = taqnyatClient.sendMsg("Hello from Taqnyat.sa", ["96655xxxxxxx"],"Taqnyat.sa")
 
print(status);