import threading

try:

    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as robot_logger
    from robot.api.deco import keyword

except Exception:

    pass


class ThreadClass(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.thread_dict = dict()

    @keyword('START THREAD')
    def start_thread(self,function_name,thread_name,args):
            a = threading.Thread(target=function_name, name='%s'%thread_name, args=(args,))
            a.start()
            self.thread_dict['%s'%thread_name] = a
            return self.thread_dict

    @keyword('STOP THREAD')
    def stop_thread(self,thread_dict,function_name,thread_logger):
        thread_dict['%s'%function_name].join()
        thread_logger.log_background_messages()

