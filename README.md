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

> **Note**
>
> 可通过修改 <https://github.com/ShigureLab/python-c-api-example/blob/main/csrc/spam.c#L24> 来观察通过 C API 暴露的函数在 Python 端的产生的效果：
>
> - `NULL` -> `inspect.signature` 报错、`__doc__` 返回 `None`
> - 不含签名的字符串 -> `inspect.signature` 报错、`__doc__` 返回该字符串
> - 含签名的字符串（即当前的代码） -> `inspect.signature` 能够正确返回字符串、`__doc__` 返回该字符串

目前 C++ 端的签名还不能实现 Type Annotation，见 [Add a signature, with annotations, to extension methods](https://stackoverflow.com/questions/50537407/add-a-signature-with-annotations-to-extension-methods/50763175#50763175)

## References

- [Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)
- [Specifying Python function signature in C/API](https://stackoverflow.com/questions/38818400/specifying-python-function-signature-in-c-api)
