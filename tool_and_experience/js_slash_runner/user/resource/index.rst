************************************************************************************************************************
常用资源网站
************************************************************************************************************************

========================================================================================================================
免费字体
========================================================================================================================

在 https://fonts.zeoseven.com/ 中, 我们可以搜索字体然后在 CSS (``<style>...</style>``) 中嵌入它们.

以 Sarasa Gothic 更纱黑体 Mono SC 为例, 我们搜索到它, 点击 :menuselection::`嵌入到 Web 项目` 即会跳转到对应内容, 再点击复制即可:

.. figure:: 免费字体-嵌入到web项目.png

.. figure:: 免费字体-复制css.png

.. code-block:: css

  @import url('https://static.zeoseven.com/zsft/159/main/result.css');

  body {
    font-family: "Sarasa Mono SC";
    font-weight: normal;
  }

========================================================================================================================
第三方库
========================================================================================================================

------------------------------------------------------------------------------------------------------------------------
CDNJS
------------------------------------------------------------------------------------------------------------------------

在 https://cdnjs.com/ 中, 我们可以搜索第三方库然后以 ``<script src="第三方库链接"></script>`` 的形式使用它们 (当然别忘了像 :doc:`../coding/index` 说的那样为它支持语法高亮).

以 yaml 解析库为例, 我们搜索找到合适的库, 点击 :menuselection:`Copy Script Tag` 即可得到对应的嵌入代码:

.. figure:: 第三方库.png

.. code-block:: html

  <script src="https://cdnjs.cloudflare.com/ajax/libs/yamljs/0.3.0/yaml.min.js" integrity="sha512-f/K0Q5lZ1SrdNdjc2BO2I5kTx8E5Uw1EU3PhSUB9fYPohap5rPWEmQRCjtpDxNmQB4/+MMI/Cf+nvh1VSiwrTA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

为了在 VSCode 中也支持对它的解析, 你需要像之前教程那样

- 安装对应的库, 此处为 ``npm install yaml``
- 将它加入到 tsconfig.json 的 ``types`` 中

------------------------------------------------------------------------------------------------------------------------
ESM>CDN
------------------------------------------------------------------------------------------------------------------------

利用 https://esm.sh/, 我们可以将 https://www.npmjs.com/ 中的很多库直接以链接形式加载.

以 yaml 解析库为例, 我们在 npmjs 搜索找到它安装方法是 ``npm install yaml``, 则可以以 ``https://esm.sh/yaml`` 在 module script 中使用它:

.. code-block:: html

  <script type="module">
  import YAML from 'https://esm.sh/yaml'

  alert(YAML.stringify({神乐光: {好感度: 5}}));
  </script>

为了在 VSCode 中也支持对它的解析, 你需要

- 安装对应的库, 此处为 ``npm install yaml``
- 在 src 文件夹中新建一个文件 global.d.ts, 里面书写:

  .. code-block:: typescript

    declare module "https://esm.sh/yaml" {
      export * from "yaml";
    }
