import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(AsyncWebsocketConsumer):
  async  def connect(self):

        self.group_name=self.scope['url_route']['kwargs']['userid']
        
        await(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)
        print(self.channel_layer.group_add)
        await self.accept()
        await self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!!'      
                  }))
          
  async def receive(self,text_data):
        print(text_data)
        



       
        #self.send(text_data=jsontext_data)

  async def disconnect(self , *args , **kwargs):
        print('disconnect')
  async def send_notification(self,event):
        print('___test___')
        print(event['type'])
        await self.send(text_data=json.dumps(event))
        #await self.send(text_data=json.dumps(event))
