## Program to understand scope of the variables
# Local variables (Scope within function)
# Global variables (Scope for all file)
# nonlocal variable (Scope within nested functions)


#### Local Variable
local = 10
print('I am local variable', local)

def localfun():
    print('Inside localfun', local)

def globalfun():
    print('Inside globalfun', local)

def localintfun():
    local = 20
    print('Inside localintfun', local)

def globalintfun():
    global local
    print('Inside globalintfun', local)

def localnestfun():
    local = 30
    print('Inside localnestfun local', local)
    def localwithnestfun():
        nonlocal local
        print('Inside localwithnestfunc local', local)
        local = local + 1
        print('Inside localwithnestfun Modified local', local)
    localwithnestfun()
    print('Inside localnestfun END', local)

localfun()
globalfun()
globalintfun()
localintfun()
localnestfun()

