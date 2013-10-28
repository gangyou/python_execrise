#coding=utf-8

import operator
import UserList

def dump(data):
    print type(data), "=>",
    # deprecated since version 2.0: User isinstance(x, collections.Callable) instead
    if operator.isCallable(data):
        print "CALLABLE",
    # deprecated since version 2.7: Use isinstance(x, collections.Mapping) instead
    if operator.isMappingType(data):
        print "MAPPING",
    # deprecated since version 2.7: Use isinstance(x, numbers.Number) instead
    if operator.isNumberType(data):
        print "NUMBER",
    # deprecated since version 2.7: Use isinstance(x, collections.Sequence) instead
    if operator.isSequenceType(data):
        print "SEQUENCE",
    print
        
dump(0)
dump("string")
dump("string"[0])
dump([1, 2, 3])
dump((1, 2, 3))
dump({"a": 1})
dump(len) # function 函数
dump(UserList) # module 模块
dump(UserList.UserList) # class 类
dump(UserList.UserList()) # instance 实例