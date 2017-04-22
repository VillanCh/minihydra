# MiniHydra: 爆破的艺术
[![Build Status](https://travis-ci.org/VillanCh/minihydra.svg?branch=master)](https://travis-ci.org/VillanCh/minihydra)

MiniHydra 我们可以很自豪的把它称作一个爆破框架，为什么？它不仅仅针对密码爆破，
其实还针对各种需要爆破的场景：尝试各种 Payload 的效果？Fuzz？

不过现在 MiniHydra 只是一个小孩子，在它的主人尝试极限编程的时候十个小时完成了它，
到现在仍然有一些不完善的地方。但是我相信他已经足够优美了。

那么，它比起大多数的爆破框架有什么优势呢？

* 字典的流式读取
* 更加节能的线程池
* 进度保存与任务继续

#### v0.5.0 - UPDATE

在这个版本中，MiniHydra 升级为一个第三方的包，而不是一个小型程序框架，你可以通过 pip install minihydra 就可以很轻松的开始 minihydra 的使用，并且通过传入函数来快速构建攻击模块。

## Quick Look

{% highlight python %}
from minihydra import MiniHydra
import requests
import urllib

dict_name = '/Users/v1ll4n/Desktop/dir.txt'

#----------------------------------------------------------------------
def target_func(target, payloads):
    """"""
    _p = payloads[0]
    _t = target

    _target_url = _t + _p
    #print _target_url

    rsp = requests.get(_target_url)
    if rsp.status_code == 404:
        return False
    else:
        return True

hydra = MiniHydra(target='http://172.16.51.130', mod=target_func, dict_file=[dict_name,], thread_max=10)

hydra.start()

_queue = hydra.get_final_queue()
while True:
    print _queue.get()
{% endhighlight %}

## 架构_

微内核架构大家并不陌生，MiniHydra 就是采用了微内核架构
所有的具体的爆破的功能都作为它的插件存在着，我们称之为 `mod`。
关于 `mod` 就可以把它当作是打游戏时候需要加载的补丁，我们甚至可以随用随写，编写极为简单，
完全让人专注业务逻辑。

架构图解：  
![Arch](http://omqhpiogv.bkt.clouddn.com/minihydra_arch.png)


## 依赖

#### Python2

```
g3ar
cmd2
progressive
```

## 当然你可以通过 shell 调用 minihydra

MiniHydra 还提供一个 `cmd2` 支持的 cli 接口，对 `cmd2` 有了解的用户肯定知道，
一个 `cmd2` 可以做到与 `python shell ／ ipython ／ shell` 无缝的链接，
可以做到管道，重定向，等各种操作。

```
v1ll4n@v1ll4n-mbp ~/Project/minihydra# python minihydra_console.py

__  __ _       _ _   _           _
|  \/  (_)_ __ (_| | | |_   _  __| |_ __ __ _
| |\/| | | '_ \| | |_| | | | |/ _` | '__/ _` |
| |  | | | | | | |  _  | |_| | (_| | | | (_| |
|_|  |_|_|_| |_|_|_| |_|\__, |\__,_|_|  \__,_|
                       |___/                   -by v1ll4n


Author: v1ll4n
Home: http://minihydra.villanch.top

Brute Password or more?
Read the BIG DICTIONARY with stream?
Work with g3ar.ThreadPool.
Less cost and run faster.

Happy hunting!

MiniHydra> start -c -target -m testmod
<module 'minihydra.mods.testmod' from '/Users/v1ll4n/Project/minihydra/minihydra/mods/testmod.pyc'>
MiniHydra> watch
{'exception': None, 'payload': '\xef\xbb\xbfa123456789', 'success': False}
{'exception': None, 'payload': '000000000', 'success': False}
{'exception': None, 'payload': 'asdfghjkl', 'success': False}
{'exception': None, 'payload': '1234567890', 'success': False}
{'exception': None, 'payload': '111111111', 'success': False}
{'exception': None, 'payload': '1q2w3e4r', 'success': False}
...
...
...
{'exception': None, 'payload': '05962514787', 'success': False}
{'exception': None, 'payload': '22222222', 'success': False}
{'exception': None, 'payload': '1Q2W3E4R5T', 'success': False}
{'exception': None, 'payload': '12345600', 'success': False}
{'exception': None, 'payload': 'q123456789', 'success': False}
{'exception': None, 'payload': '44444444', 'success': True}
{'exception': None, 'payload': '123321123', 'success': False}
{'exception': None, 'payload': '789456123', 'success': False}
{'exception': None, 'payload': 'xiaoxiao', 'success': False}
{'exception': None, 'payload': 'qq123456', 'success': False}

```

当然 MiniHydra 还提供了其他的接口可以调用：可以使用 Python，把 minihyra 作为一个包导入。
相关文档正在完善中
