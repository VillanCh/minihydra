from .base import ModBase
from .exceptions import ModReturnError

########################################################################
class TemplateMod(ModBase):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, target, attack_func=None, only_one_result=True):
        """"""
        ModBase.__init__(self, target)
        
        self._attack_func = attack_func
        
        self._only_one_result = True

    #----------------------------------------------------------------------
    def attack(self, payload):
        """"""
        result = self._attack_func(self.target, payload)
        if isinstance(result, bool):
            if self._only_one_result:
                if result:
                    self.finish()
            return result
        else:
            try:
                _success_flag = result[0]
            except:
                raise ModReturnError()
            
            if isinstance(_success_flag, bool):
                if self._only_one_result:
                    if _success_flag:
                        self.finish()
                return result
            else:
                raise ModReturnError()
        