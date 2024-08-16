call_from_sys(cmd, has_status=False):
    if(sys.version_info >= (3, 0)):
        if has_status == False:
            output = subprocess.getoutput(cmd)
            return output.split()
        else:
            status, output = subprocess.getstatusoutput(cmd)
            # return status, output.split()
    else:
        r = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=open(os.devnull, 'w')).stdout
        return [i.decode() for i in i.readlines() if i != b'\n']
