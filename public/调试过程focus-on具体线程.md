# 调试过程focus on具体线程

# 如何在调试的时候指定一个线程进行调试

# base

- vscode
- cuda launch

# STEP

- 第一步开启调试
- 第二部：单击右下角CUDA（0，0，0）![](https://cdn.jsdelivr.net/gh/Kui2ei/picpic@main/image-20240419153248954.png)
- 第三步：在提示的对话框中键入命令，回车![image-20240419153542271](https://cdn.jsdelivr.net/gh/Kui2ei/picpic@main/image-20240419153542271.png)

## 关于命令(可直接复制)

```sh
cuda block (0, 0, 0) thread (1, 0, 0)
```



其中thread中的维度和正常人认知的维度是反着的，（1，0，0）代表着第二个线程【假设（0，0，0）代表着第一个线程】

当然，还有其他版本，当不需要块切换

```sh
cuda thread (1, 0, 0)
```

cuda也可以省略

```sh
thread (1, 0, 0)
```




