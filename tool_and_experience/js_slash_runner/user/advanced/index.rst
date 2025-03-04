************************************************************************************************************************
进阶: 分文件编写脚本
************************************************************************************************************************

你当然可以利用 module 进行分文件编写:

.. code-block:: typescript
  :caption: ``src/index.ts``

  import { detectMessageUpdated } from './util.js'  // 注意是 .js

  eventOn(tavern_events.MESSAGE_UPDATED, detectMessageUpdated);

.. code-block:: typescript
  :caption: ``src/util.ts``

  export function detectMessageUpdated(message_id: number) {
    alert(`你刚刚修改了第 ${message_id} 条聊天消息对吧😡`);
  }

========================================================================================================================
实时修改脚本内容
========================================================================================================================

你只需要按之前单文件那样使用入口文件即可; 但相比于之前的写法, 你需要在 ``<scripdoc>`` 中指定类型为 module:

.. code-block:: html

  <script type="module" src="http://localhost:5500/build/src/index.js"></script>

========================================================================================================================
打包为单文件
========================================================================================================================

在编写完成后, 你可以用 rollup 将结果打包为单个文件.

首先安装 rollup 和 @rollup/plugin-typescript:

.. code-block:: bash

  npm i -g rollup
  npm i --save-dev @rollup/plugin-typescript path url glob

然后编写 rollup.config.js 来配置要如何打包. 一般而言, 按下面的配置即可:

.. code-block:: javascript
  :emphasize-lines: 8-11

  import path from 'path'
  import typescript from '@rollup/plugin-typescript';
  import { fileURLToPath } from 'url';
  import { globSync } from 'glob';

  export default {
    input: Object.fromEntries(
      [
        ...globSync('src/**/index.ts'),  // 这一句会将 src 中所有的 index.ts 分别视为入口文件
        'src/角色卡/main.ts',             // 你某张角色卡脚本的入口文件
      ].map(file => [
        file.slice(0, file.length - path.extname(file).length),
        fileURLToPath(new URL(file, import.meta.url)),
      ]),
    ),
    output: {
      dir: 'dist',
      format: 'es',
    },
    plugins: [typescript()],
  };


然后我们在该目录下运行 ``rollup -c`` 即可将其打包.

========================================================================================================================
第三方库
========================================================================================================================

你仍然可以用 :doc:`cdnjs, ESM>CDN 等提供的第三方库 </tool_and_experience/js_slash_runner/user/resource/index>`:

.. code-block:: typescript

  import 'https://cdnjs.cloudflare.com/ajax/libs/yamljs/0.3.0/yaml.min.js'
  import YAML from 'https://esm.sh/yaml'


************************************************************************************************************************
进阶: 分文件编写脚本(webpack 方式)
************************************************************************************************************************
如果你在工具链选择上对 webpack 有偏好，可以参照下面的步骤进行配置

.. code-block:: typescript
  :caption: ``src/index.ts``

  // 注意，下面不加 .ts 后缀哦
  import {detectMessageUpdated} from './util' //即要引入的另一个文件，有多个文件则import多个。只有在 index.ts 中才能 import。

  eventOn(tavern_events.MESSAGE_UPDATED, detectMessageUpdated);

另一个文件：

.. code-block:: typescript
  :caption: ``src/util.ts``

  export function detectMessageUpdated(message_id: number) {
    alert(`你刚刚修改了第 ${message_id} 条聊天消息对吧😡`);
  }

========================================================================================================================
打包为单文件(webpack)
========================================================================================================================

由于一开始的 frontend_writer 没有 ``package.json`` 和 ``webpack.config.js`` ，因此需要补充这些文件，用于描述构建过程，如下：


.. code-block:: json
  :caption: ``package.json``

  {
      "name": "ModExample",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
          "build:ts": "tsc -p ./tsconfig.json"
      },
      "repository": {
          "type": "git",
          "url": "https://gitlab.com/novi028/JS-Slash-Runner"
      },
      "private": true,
      "packageManager": "yarn@3.4.1",
      "dependencies": {
          "file-saver": "^2.0.5",
          "jquery-ui": "^1.14.1",
          "json5": "^2.2.3",
          "jszip": "^3.10.1",
          "lodash": "^4.17.21",
          "moment": "^2.29.4",
          "rxjs": "^7.8.1",
          "yamljs": "^0.3.0"
      },
      "devDependencies": {
          "@types/file-saver": "^2.0.7",
          "@types/jquery": "^3.5.19",
          "@types/jqueryui": "^1.12.24",
          "@types/lodash": "^4.14.198",
          "@types/node": "^20.6.0",
          "@types/yamljs": "^0.2.34",
          "@webpack-cli/generators": "^3.0.7",
          "bootstrap": "^5.3.1",
          "css-loader": "^6.8.1",
          "fork-ts-checker-webpack-plugin": "^8.0.0",
          "html-webpack-plugin": "^5.5.3",
          "nodemon": "^3.0.1",
          "sass": "^1.66.1",
          "sass-loader": "^13.3.2",
          "style-loader": "^3.3.3",
          "ts-loader": "^9.4.4",
          "ts-mixer": "^6.0.3",
          "tsconfig-paths-webpack-plugin": "^4.1.0",
          "typescript": "^5.1.6",
          "webpack": "^5.88.2",
          "webpack-cli": "^5.1.4",
          "webpack-dev-server": "^4.15.1"
      }
  }

.. code-block:: javascript
  :caption: ``webpack.config.js``

  const path = require('path');
  const HtmlWebpackPlugin = require('html-webpack-plugin');
  const webpack = require('webpack');
  module.exports = {
      entry: './src/index.ts', //这里会指定一个ts文件作为入口文件，从这个文件的 import 去扫描对其他文件的依赖
      module: {
          rules: [
              {
                  test: /\.ts$/,
                  exclude: /iframe_client/,
                  use: 'ts-loader'
              }
          ],
      },
      resolve: {
          extensions: ['.ts', '.js'],
          alias: {
          }
      },
      output: {
          filename: 'index.js',//这里是输出到的文件
          path: path.resolve(__dirname, 'dist')
      },
      externals: [
          function({ request }, callback) {
              callback();
  
          }
      ],
      plugins: [
          new webpack.ProvidePlugin({
              // 有第三方模块时会在这里加东西
          }),
  
      ],
      mode: 'development', //development是人能大概看的，production是比较省字符数的，不过我们暂时也不需要省，对吧
      devtool: 'source-map', // 添加这一行，启用 source map
      optimization: {
          usedExports: false
      }
  };

创建完这些文件之后，需要执行 ``npm install`` 以安装所有需要的依赖

那之后可以在这个目录下运行 ``webpack -c ./webpack.config.js`` 进行打包。一次正常的打包输出类似于：

.. code-block:: shell

  > webpack -c ./webpack.config.js

  asset bundle.js 12 KiB [emitted] (name: index) 1 related asset
  modules by path ./src/*.ts 9.16 KiB
    ./src/index.ts 384 bytes [built] [code generated]
    ./src/util.ts 6.74 KiB [built] [code generated]
  webpack 5.98.0 compiled successfully in 2173 ms

为了方便，你也可以把构建的指令加入到 ``package.json`` 中，以获取更好的 IDE 等支持：

.. code-block:: json5

  {
      "name": "项目名",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
          "build:webpack": "webpack -c ./webpack.config.js" //加在这里，之后就也可以使用 npm run build:webpack 运行啦
      }
  }

========================================================================================================================
实时修改脚本内容
========================================================================================================================

你只需要按之前单文件那样使用入口文件即可; 但相比于之前的写法, 你需要在 ``<scripdoc>`` 中指定类型为 module:

.. code-block:: html

  <script type="module" src="http://localhost:5500/build/src/index.js"></script>

========================================================================================================================
第三方库
========================================================================================================================

你可以将指定的 npm 依赖通过配置最终打包到输出的单文件中。以 ``toml`` 为例，下面修改了代码逻辑使用第三方库，并在配置中新增相应描述，保证最终打包在内。

.. code-block:: typescript
  :caption: ``src/index.ts``

  import {tomlFn, detectMessageUpdated} from './util' //即要引入的另一个文件，有多个文件则import多个。只有在 index.ts 中才能 import。
  eventOn(tavern_events.MESSAGE_UPDATED, detectMessageUpdated);
  eventOn(tavern_events.GENERATION_ENDED, tomlFn); //随便找个时间点使用它，这个是LLM回复完成的时间点，总之不报运行时错误就是代表这里成功了。（实际上也不会报

另一个文件：

.. code-block:: typescript
  :caption: ``src/util.ts``

  declare const toml: any; //避免ts报错
    
  const tomlStr = `
     title = "TOML Example"
     [owner]
     name = "John Doe"
     `;
  export function tomlFn(): any{
      return toml.parse(tomlStr);//使用toml库
  }
  
  export function detectMessageUpdated(message_id: number) {
    alert(`你刚刚修改了第 ${message_id} 条聊天消息对吧😡`);
  }

除了代码本身之外，你还要修改 ``package.json`` 引入新的依赖：

.. code-block:: json5

  {
      "name": "ModExample",
      //略
      "packageManager": "yarn@3.4.1",
      "dependencies": {
          "toml": "^3.0.0" //新增的依赖在这里加就可以了！
      },
      "devDependencies": {
          "@types/jquery": "^3.5.19" //有些库如果有自己的 ts 定义包，就在 devDependencies 里面加啦，因为 toml 不需要，这里就以 jquery 为例了。
      }
  }

完成配置后需要重新运行 npm install 安装相关依赖，以获取 IDE 类型支持。

接着需要调整 ``webpack.config.js`` 配置项，让它把对应的依赖打包进最终的 js 文件中：


.. code-block:: javascript
  :caption: ``webpack.config.js``

  const path = require('path');
  const HtmlWebpackPlugin = require('html-webpack-plugin');
  const webpack = require('webpack');
  module.exports = {
      entry: './src/index.ts', //这里会指定一个ts文件作为入口文件，从这个文件的 import 去扫描对其他文件的依赖
      /*略*/
      plugins: [
          new webpack.ProvidePlugin({
              // 在这里加上后，如果有ts文件使用了 toml 变量，就会自动加载 toml 模块啦
              toml: 'toml' // <- 变动的是这个部分！
          }),
      ],
      /*略*/
  };


最后重新运行 ``webpack -c ./webpack.config.js`` 进行打包，就可以发现有新的 js 被打包进去了，下面是样例输出：

.. code-block:: shell

  > webpack -c ./webpack.config.js

  asset bundle.js 120 KiB [emitted] (name: index) 1 related asset
  modules by path ./src/*.ts 9.16 KiB
    ./src/index.ts 384 bytes [built] [code generated]
    ./src/util.ts 6.74 KiB [built] [code generated]
  modules by path ./node_modules/toml/ 108 KiB
    ./node_modules/toml/index.js 218 bytes [built] [code generated]
    ./node_modules/toml/lib/parser.js 102 KiB [built] [code generated]
    ./node_modules/toml/lib/compiler.js 5.01 KiB [built] [code generated]
  webpack 5.98.0 compiled successfully in 2173 ms
