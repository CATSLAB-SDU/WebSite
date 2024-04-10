# 连接GitHub

# 连接GitHub

## HTTP

访问不了主要是DNS被污染了，在本机DNS即可。打开如下文件将下面的内容后缀在文件中即可，修改需要管理员权限，确保自己真的修改成功了`C:\Windows\System32\drivers\etc\hosts`​。在 CMD 窗口输入：`ipconfig /flushdns`​

linux则是修改`/etc/hosts` 保存可以执行`sudo nscd restart`确保其生效。

下面的内容可以在下面的网站中找到最新的：

[hosts · frankwuzp/github-host - Gitee.com](https://gitee.com/frankwuzp/github-host/blob/main/hosts)

[maxiaof/github-hosts: 通过修改Hosts解决国内Github经常抽风访问不到,每日更新](https://github.com/maxiaof/github-hosts)

```shell
#Github Hosts Start
#Project Address: https://github.com/maxiaof/github-hosts
#Update URL: https://raw.githubusercontent.com/maxiaof/github-hosts/master/hosts
151.101.129.194	github.global.ssl.fastly.net
185.199.109.153	assets-cdn.github.com
185.199.108.153	documentcloud.github.com
140.82.112.3	gist.github.com
185.199.109.133	gist.githubusercontent.com
185.199.108.154	github.githubassets.com
140.82.112.18	help.github.com
140.82.114.9	nodeload.github.com
185.199.109.133	raw.github.com
140.82.112.17	status.github.com
185.199.111.153	training.github.com
185.199.109.133	avatars.githubusercontent.com
185.199.109.133	avatars0.githubusercontent.com
185.199.109.133	avatars1.githubusercontent.com
185.199.108.133	avatars2.githubusercontent.com
185.199.111.133	avatars3.githubusercontent.com
185.199.110.133	avatars4.githubusercontent.com
185.199.111.133	avatars5.githubusercontent.com
185.199.109.133	avatars6.githubusercontent.com
185.199.109.133	avatars7.githubusercontent.com
185.199.111.133	avatars8.githubusercontent.com
185.199.109.133	favicons.githubusercontent.com
140.82.114.9	codeload.github.com
52.217.116.57	github-cloud.s3.amazonaws.com
52.216.48.177	github-com.s3.amazonaws.com
3.5.25.27	github-production-release-asset-2e65be.s3.amazonaws.com
52.216.221.89	github-production-user-asset-6210df.s3.amazonaws.com
3.5.29.126	github-production-repository-file-5c1aeb.s3.amazonaws.com
185.199.111.153	githubstatus.com
140.82.114.18	github.community
185.199.110.133	media.githubusercontent.com
185.199.109.133	camo.githubusercontent.com
185.199.110.133	raw.githubusercontent.com
185.199.109.133	cloud.githubusercontent.com
185.199.110.133	user-images.githubusercontent.com
2606:50c0:8003::153	customer-stories-feed.github.com
185.199.108.153	pages.github.com
140.82.112.5	api.github.com
140.82.114.26	live.github.com
140.82.112.30	githubapp.com
140.82.113.3	github.com
52.224.38.193	github.dev
140.82.112.21	central.github.com
140.82.113.25	alive.github.com
185.199.111.133	desktop.githubusercontent.com
#Github Hosts End
```

## SSH

命令行中输入如下指令。

```cmd
ssh-keygen -t rsa -C "your_email@example.com"
#github注册账号的邮箱，其他的不知道可不可以
```

去用户目录（C:\\Users\\用户）下找到.ssh目录，没有该目录，设置显示隐藏目录，在.ssh目录下找到id_rsa.pub，前往GitHub，创建一个SSH keys，把id_rsa.pub复制过来就可以。

![](https://cdn.jsdelivr.net/gh/yinxiangkai/ImageBed@main/202403281530899.png)![](https://cdn.jsdelivr.net/gh/yinxiangkai/ImageBed@main/202403281530228.png)​

将下面内容添加到.ssh/config中,如果没有可以自己创建一个。

```cmd
Host github.com
    User git
    Hostname ssh.github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa
    Port 443
```

在cmd中输入，验证。

```cmd
ssh -T git@github.com
```

‍

‍

