# (内部向け)kreateのHP使い方ガイド

## 初めて使うとき
1. hugo,npmをインストール
2. terminalに、
    ```
    git clone https://github.com/kreate-tohoku/kreate-tohoku.github.io.git
    ```
    ```
    npm install
    ```

## HPを更新するときのワークフロー
- 直接編集するのは、/content, /assets, hugo.yamlのどれかです。github上にある/docsの内容が自動的にHPになります。

- ローカルに変更したHPを確認するとき

    ```
    npm run test
    ```
    コマンドによって現れたURLをブラウザで表示すればOK。だいたい、http://localhost:1313/ だと思います。

- ホームページの元となるHTML(/docs)をつくるとき。HPの変更後、最後にこのコマンドを打ちましょう。

    ```
    npm run build
    ```

- githubにアップロードするときの基本操作
    - すべてのファイルをコミットする候補に加える
        ```
        git add -A
        ```
    - コミット。ゲームでいうところのセーブ機能。
        ```
        git commit -m "do somthing"
        ```
    - ローカルで行ったコミットをファイルをgithubにおくる。
        ```
        git push
        ```
    - リモートの状態をローカルに引っ張ってくる。他人が編集したコードを自分のコードに持ってくるときに使用。
        ```
        git pull
        ```
