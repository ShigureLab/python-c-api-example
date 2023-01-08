# C API Example

> **Note**
>
> 本示例仅用于 Paddle Type Hints 引入方案中的部分的可行性验证

## 安装与运行

本示例使用 Poetry 管理依赖项，需要先安装 Poetry。

可以在 [Poetry 文档中](https://python-poetry.org/docs/#installation)找到合适的安装方式。

之后安装依赖项并编译 C 源码：

```bash
poetry install
```

> **Note**
>
> 每次修改 C 源码后都需要重新运行此命令。

之后就可以直接运行啦～

```bash
poetry run c_api_example
```

## References

- [Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)
- [Specifying Python function signature in C/API](https://stackoverflow.com/questions/38818400/specifying-python-function-signature-in-c-api)
