def send_notification(message=''):
    def notify_observe(fn):
        def wrapped_fun(obj):
            result = fn(obj)

            for observe in obj.observers:
                print(observe.send(message))

            return result

        return wrapped_fun

    return notify_observe
