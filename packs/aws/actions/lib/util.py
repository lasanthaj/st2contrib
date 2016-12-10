def get_listners(listener_string):
        listeners = listener_string.split('#')
        
        if len(listeners) == 0:
                listeners = listener_string

        listener_list = []

        for i in range(len(listeners)):
                values = listeners[i].split(',')
                tup = (int(values[0]),int(values[1]),values[2])

                listener_list.append(tup)

        return listener_list
