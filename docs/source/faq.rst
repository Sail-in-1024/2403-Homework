========
常见问题
========

这是什么？
----------

这是 |class-name| 的作业记录项目，用来为忘记作业的人提供参考。

这也是一个 `Sphinx`_ 文档项目，但并非用于部署文档。

.. _how-to-realize:

\* 怎么做的？
^^^^^^^^^^^^^
   
这个项目被存储在 `The GitHub Repository`_ 上，使用了 `Read the Docs tutorial`_ 模板。

网页主要由 `Sphinx 文档生成工具 <Sphinx_>`_ ，使用 `book主题 <book`_ 渲染，而整个项目由 `Read the Docs`_ 托管。感兴趣的话可以参考 `Sphinx 项目部署文档 <Read the Docs intro_>`_ 。

.. _The GitHub Repository: https://github.com/Sail-in-1024/2403-Homework
.. _Read the Docs tutorial: https://github.com/readthedocs/tutorial-template/
.. _Read the Docs intro: https://docs.readthedocs.com/platform/stable/intro/sphinx.html

\* 为什么选择在线上发布？
^^^^^^^^^^^^^^^^^^^^^^^^^

线上的功能更丰富。

这就很像一个类似的问题“\ :ref:`is-overqualified`\ ”。

每次打开怎么都那么慢？
----------------------

大多数情况下不是我的问题。也可能是，因为我不是 `Read the Docs`_ 的付费用户，在公共资源访问高峰时一般打开较慢；不过据我所知，这可能和你连接的网络、你的设备（例如，用 :term:`803的破电脑` 时），以及使用的浏览器有关。

另外， `Cloudflare`_ 的安全验证可能也要花费很多时间（这个是自带的）。

移动端该怎么找到以前的作业内容？
--------------------------------

看到右上角的“`🔍 <search.html>`_”图标了吗？点击它就能看到一个搜索框 [#book-based]_。无论你正在哪个页面浏览，这都会启用 *全局搜索*。

展开右下角的“ReadtheDocs”菜单也可以找到搜索框\ *(Search docs)*\ 。

好像要输入至少3个字符才会自动调用搜索。

怎么下载 PDF 格式的文件？
-------------------------

每个页面右上角都有一个“下载”图标，点击会出现一个菜单，选择“.pdf”即可～ [#book-based]_

.. _is-overqualified:

真的不是大材小用吗？
--------------------

可能是的。

但使用 `Sphinx`_ 部署文档还是有优点的。这里的文档编辑功能很好用。支持 **粗体** ， *斜体* ， ``字面值`` ，`超链接 <https://www.example.com/>`__，:ref:`交叉引用 <is-overqualified>`，以及 ---

.. code-block:: rest
   :caption: 代码块
   
   .. 这可以生成一张表格
   
   +--------+----------+------------+
   |文档类型|线上      |线下        |
   +========+==========+============+
   |优点    |灵活、智能|随处可写    |
   +--------+----------+------------+
   |缺点    |要联网    |形式单一    |
   |        |          |可见范围有限|
   +--------+----------+------------+

，还有 ---

.. admonition:: 提示
   
   提示信息...

以及，如 :ref:`how-to-realize` 所述，每次源文件修改并上传到 `GitHub`_ 后，文档会自动生成。这意味着，无论你在什么地方，只要面前有一台可以联网的设备（并且拥有像我这样的管理员权限），就可以通过 *Commit* （提交）请求更新文档。

后续维护怎么样？
----------------

按照计划，这个项目将持续维护～😊

.. [#based] 基于 `book`_ 主题的

.. _Sphinx: https://www.sphinx-doc.org/zh-cn/master/
.. _Read the Docs: https://www.readthedocs.org/
.. _GitHub: https://www.github.com/
.. _Cloudflare: https://www.cloudflare-cn.com/
.. _book-based: https://sphinx-book-theme.readthedocs.io/en/latest/