from pypresence import Presence
import time

client_id = "805878114415673385"
RPC = Presence(client_id)


RPC.connect()




print(RPC.update(state="pimbapimba",details="swag", small_image="8",large_text="eu tenho",small_text="drip",large_image="gandadrena",party_size=[69,420],buttons=[{"label" : "Meu Site", "url": "https://sitedripado.herokuapp.com"}, {"label" : "Meu Bot do Discord :)", "url": "https://discord.com/api/oauth2/authorize?client_id=805878114415673385&permissions=8&scope=bot"}],start=time.time()))



while True:
    time.sleep(15)


  
