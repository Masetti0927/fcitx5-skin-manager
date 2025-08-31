# 简介
本项目预计开发一个拥有GUI，可以同时在一个程序中管理、配置fcitx5输入法的主题，而不用打开KDE系统设置配置fcitx5的应用。
项目涉及ssf皮肤处理、解密与整理部分的源代码来自 https://github.com/fkxxyz/ssfconv 。

## 缺陷

### ssf转fcitx5皮肤样式无法完全匹配的问题

部分皮肤可能转换后效果不太好，例如一些搜狗的异形皮肤，输入的拼音和底下候选字的左侧起点不在同一位置，本人技术有很多不足，目前不清楚fcitx5能否实现相关的功能
  - 一些典型例子：https://pinyin.sogou.com/skins/detail/view/info/610817

## 声明
本项目不提供相关的ssf文件下载，目前也不打算将相关内容，如自动获取搜狗的皮肤库、在线预览、即时下载等纳入To do list。
 - 详见 https://pinyin.sogou.com/skins/robots.txt

需要ssf格式的输入法皮肤，可以前往 https://pinyin.sogou.com/skins/ 进行下载。

## 致谢
再次感谢 https://github.com/fkxxyz/ssfconv 项目的源码作为本工作的基础。