   channel.basic_consume(queue='hello',
                         on_message_callback=callback,
                         auto_ack=True)
   