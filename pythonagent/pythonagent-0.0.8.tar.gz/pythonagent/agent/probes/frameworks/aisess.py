import os
import sys
import cProfile
import threading
import pstats
import logging
from collections import Counter
from pyclbr import readmodule
logger = logging.getLogger('pythonagent.agent')


class Aisession():
    def __init__(self, istart, starttime, duration, sess):
        self.duration = duration
        self.istart = istart
        self.starttime = starttime
        self.sess = sess
        self.prof = cProfile.Profile()
        os.environ['aisess_status'] = 'True' 

    def enableprof(self):
        self.prof.enable()
        #os.environ['aisess_status'] = 'True'
        #os.environ['Aisession_flag'] = 'True'

    def endsession(self):
        self.prof.disable()
        self.printst()
        os.environ['aisess_status'] = 'False'
        os.environ['Aisession_flag'] = 'False'
        logger.info("@!#@$#%$^&*^&%^$%#$@####$#%$^% IN endsession")
        self.prof = None
        

    def disableprof(self):
        #if self.istart == 0:
        #   self.endsession()
        timer = threading.Timer(self.duration,self.endsession)
        timer.start()
        logger.info("exiting endsession")




    def printst(self):
        path =  "/opt/cavisson/netdiagnostics/logs/"
        filename = str(self.sess.decode('ascii'))+"_AI.txt"
        file_to_open = os.path.join(path, filename)
        filenameai = str(self.sess.decode('ascii'))+".txt"
        aifile_to_open = os.path.join(path, filenameai)
        xmlfilename = str(self.sess.decode('ascii'))+".xml"
        xmlfile_to_open = os.path.join(path, xmlfilename)
        xmlfile = open(xmlfile_to_open, 'w')
        f = open(file_to_open, 'w')
        f2 = open(aifile_to_open, 'w')
        #f = open(f'/opt/cavisson/netdiagnostics/logs/{self.sess}.txt', 'w')
        f.writelines("************************************  AUTO-INSTRUMENTATION  **************************************** \n")
        f2.writelines("************************************  AUTO-INSTRUMENTATION  **************************************** \n")
        f.writelines("# <FQM>| <I:(instrumented) / C :(consisdered) / R :(remove) >| < Total Count > | < Total Duration > | < Added TimeStamp > | < Remove TimeStamp > \n")
        f.writelines(f"#Start_Time {self.starttime}\n")
        #f.writelines(f"#End_Time {}")
        f.writelines(f"#Total Duration {self.duration}\n")
        p = pstats.Stats(self.prof)
        client_app_root = os.path.dirname(sys.argv[0])
        logger.info("application:-{}".format(client_app_root))
        methodcountdict = {}
        for k,v in p.stats.items():
            #print(k[0])
            if client_app_root in k[0]:
                modulek001 = k[0]
                logger.info("$$$$$$$$$$$$$$$$$$ {}".format(modulek001))
                module = k[0]
                logger.info("module:-{}".format(k[0]))
                module_path = os.path.split(os.path.abspath(module))[0]
                modulefullname = os.path.split(os.path.abspath(module))[1]
                module_name = modulefullname.split('.')[0]
                methodname = k[-1]
                modulemethod = module_path+'*'+module_name+'*'+methodname
                total_call = str(v[1])
                total_duration =str(v[3])
                logger.info('modulemethod:-{}'.format(modulemethod))
                logger.info('module path:- {}'.format(module_path))
                logger.info('module name:-{}'.format(module_name))
                logger.info('method name:- {}'.format(k[-1]))
                logger.info('Total call:- {}'.format(v[1]))
                logger.info('Response time of method:-{}'.format(v[3]))
                #methodcountdict = {}
                methodcountdict[modulemethod] = total_call
                mod = readmodule(module_name, path=[module_path])
                li = []
                for k, v in mod.items():
                    li.append(k)
                    methods = v.methods.items()
                    lk = []
                    for method, lineno in methods:
                        lk.append(method)
                    li.append(lk)
                count=0
                classname =''
                for i in li:
                    count +=1
                    if type(i)==str:
                        pass
                    else:
                        for j in i:
                            if j == methodname:
                                classname = li[count-2]
                               #print("classname:-",li[count-2])
                                varfullname = module_name+"."+li[count-2]+"."+methodname
                               #print("))))))))))))*((((((((((((",a)
                            else:
                                pass
                if len(classname)>0:
                    logger.info("{}".format(varfullname))
                else:
                    varfullname = module_name+"."+methodname
                    logger.info("{}".format(varfullname))
                outputform = varfullname+"|"+"I"+"|"+total_call+"|"+total_duration+"|"+"0"+"|"+"0"
                logger.info("************************************XWWDWSASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS {}".format(outputform))
               # f.writelines("************************************  AUTO-INSTRUMENTATION  **************************************** \n")
                f.writelines(f"{outputform}  \n")
                if (float(total_duration)/int(total_call)) >=0.7:
                   outputformai = varfullname+"|"+"I"+"|"+total_call+"|"+total_duration+"|"+"0"+"|"+"0"
                   f2.writelines(f"{outputformai}  \n")
        f.close()    
        f2.close()
        xmlfile.close()
        logger.info("{}".format(methodcountdict))

"""def aisession():
    ai = WSGIInterceptor()
    ai.application_callable = agentprofiler.application_callable_pro

#aisession()

def ta():
    wsgi.WSGIInterceptor.application_callable = agentprofiler.application_callable

#if flag ==True:
#timer = threading.Timer(300, ta)
#timer.start()
def enablendisablesess():
    aisession()
    timer = threading.Timer(300, ta)
    timer.start()"""    
