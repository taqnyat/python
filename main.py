from TaqnyatSms import *


bearer = '**************************0adc2b'
taqnyt = client(bearer)
status = taqnyt.sendStatus();
 
print(status);
