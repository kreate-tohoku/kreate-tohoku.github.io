# kreate

## 初めて使うとき
1. hugoをインストール
2. terminalに、
    ```
    git clone https://github.com/kreate-tohoku/kreate-tohoku.github.io.git
    npm install
    ```
3. ページをlocalhostでみるとき

    ```
    npm run test
    ```

4. ホームページの元となるHTML(docs)をつくるとき

    ```
    npm run test
    ```

5. githubにアップロードするとき
    - すべてのファイルをコミットする候補に加える
        ```
        git add -A
        ```
    - ゲームでいうところのセーブ機能。変更不可
        ```
        git commit -m "do somthing"
        ```

    - ローカルなファイルをgithubにおくる。
        ```
        git push
        ```
    - リモートの状態をローカルに引っ張ってくる
        ```
        git pull
        ```