### 介绍

一个subprocess模块的封装,可以更方便的进行系统调用

To Do List:

1. return realtime result

### 安装

```
pip install easyrun
```

### 使用方法

```
>>> import easyrun
>>> r = easyrun.run('uptime')
 04:06:37 up 2 min,  1 user,  load average: 0.20, 0.19, 0.08
>>> r.output
>>> r.success
True
>>> r.retcode
0
```

>>> r = easyrun.run_capture('uptime')
>>> r.output
' 04:07:16 up 2 min,  1 user,  load average: 0.11, 0.17, 0.08\n'
>>> r.success
True
>>> r.retcode
0
```

Quick comparison of result objects:

| envoy.Response | easyrun.Result |
| -------------- | --------------- |
| .command       | .command        |
| .status_code   | .retcode        | 
|                | .success        |
|                | .output         |
| .std_out       |                 |
| .std_err       |                 |
| .std_err       |                 |

Example of `.success` usage:

    from easyrun import run_capture

    r = run_capture('ls -la')
    if r.success:
        print(r.output)
    else:
        print("Error: '%s' exit code %s" % (r.command, r.retcode))
        print("         ...")
        # print last three lines of output
        for line in r.output.splitlines()[-3:]:
            print("       %s" % line)

