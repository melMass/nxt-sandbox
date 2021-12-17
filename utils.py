def source(filepath):
    import sys, os, subprocess as sp, json
    source = "source {}".format(filepath)
    bin = sys.executable
    dump = '{} -c "import os, json;print(json.dumps(dict(os.environ)))"'.format(bin)
    pipe = sp.Popen(['/bin/bash', '-c', '%s && %s' %(source,dump)], stdout=sp.PIPE)
    env = json.loads(pipe.stdout.read().decode())
    os.environ = env
