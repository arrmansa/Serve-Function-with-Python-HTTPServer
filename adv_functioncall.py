import urllib3
import pickle
import time

#with timing
def adv_functioncall(fn_input):
    first = time.perf_counter()
    request = adv_functioncall.PoolManager.request('POST', 'http://127.0.0.1:1234', body = pickle.dumps(fn_input), retries=0)
    out = pickle.loads(request.data)
    second = time.perf_counter()
    time_taken = round((second - first),5)
    return out,time_taken

setattr(adv_functioncall, 'PoolManager', urllib3.PoolManager())