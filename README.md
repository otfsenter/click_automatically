1. 按键的配置文件为config.ini，一个时间点按下若干按键，修改config.ini文件来配置
2. 时间，按键和次数都是可以改的，改完config.ini保存之后重新运行click.exe程序，记得运行程序之后要点一下需要点击的页面

配置文件举例：
```
[item1]
time = 10:59:40
key1 = up,2
key2 = down,5
key3 = enter,1
```

多个时间点依次为item1、item2、item3，以此类推， 一个时间点item1下

* time是执行的时间
* key1是第一个按下的键，up是上方向键，按下2次
* key2是第二个按下的键，down是下方向键，按下5次
* key3是第三个按下的键，enter是回车键，按下1次

以此类推

按键对应关系如下：

* 上方向键对应单词up
* 下方向键对应单词down
* 左方向键对应单词left
* 右方向键对应单词right
* 回车对应单词enter
* 空格对应单词space
* shift对应单词shift
* Ctrl对应单词ctrl
* Alt对应单词alt
* Tab对应单词tab
* Esc对应单词esc

二十六个字母
* 用小写字母abcdefghijklmnopqrstuvwxyz

数字
* 1234567890
