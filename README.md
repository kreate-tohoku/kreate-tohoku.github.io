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

## HP更新の仕方
- `/content`のmdファイルを変更・追加すると自動でページが作られます。

- 直接編集するのは、`/content`, `/assets`, `/static`, `hugo.yaml`のどれかです。github上にある`/docs`の内容が自動的にHPになります。

- ローカルに変更したHPを確認するとき

    ```
    npm run test
    ```
    コマンドによって現れたURLをブラウザで表示すればOK。だいたい、http://localhost:1313/ だと思います。

- ホームページの元となるHTML(`/docs`)をつくるとき。HPの変更後、最後にこのコマンドを打ちましょう。
    ```
    npm run build
    ```


## 画像をいれたいとき

ヘッダー画像は、`assets/images/`に入れましょう。とくに、postsを更新した場合は、 `assets/images/posts/`にいれましょう。**画像は勝手にリサイズされるので、サイズ調節は必要ありません。**



```markdown
<!-- 例 -->

---
date: 2021-12-18T11:10:36+08:00
draft: false
description: わわわわに関する記事
featured_image: ../assets/images/posts/wawawawa.jpg
---
```


記事の中に使用する画像は、`static/images/`に入れましょう。とくに、postsを更新した場合は、 `static/images/posts/`にいれましょう。**画像はそのままのサイズで入るので、リサイズしてから入れましょう**

```markdown
<!-- 例 -->
![](/images/posts/acon.jpg)
```


## HPを更新するときのワークフロー

- githubにアップロードするときの基本操作。
    1. ホームページをビルドする (git addするまえにこれをやらないと、生成されるHPがおかしくなるので注意)
        ```
        npm run build
        ```
    1. すべてのファイルをコミットする候補に加える
        ```
        git add -A
        ```
    1. コミット。ゲームでいうところのセーブ機能。
        ```
        git commit -m "do somthing"
        ```
    1. ローカルで行ったコミットをファイルをgithubにおくる。
        ```
        git push
        ```
    1. リモートの状態をローカルに引っ張ってくる。他人が編集したコードを自分のコードに持ってくるときに使用。
        ```
        git pull
        ```

- githubにpushすると、1分後くらいに変更が反映されます。正しく表示できているかチェックしてください。とくに、リンク切れ等を起こしていないかチェックすること。