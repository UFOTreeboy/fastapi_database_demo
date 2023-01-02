# fastapi_database_demo

# 作品介紹

粉絲團留言板beta，你可以留下你的留言給站長，或是提供相關建議，</br>
目前的狀態是可以隨時刪除你的留言與對方的留言。</br>

# 作品技術介紹
作品是呈現留言板後端的應用，以及資料庫的資料存取，</br>
主要採用FastAPI作為後端開發，實現RESTful API的概念，</br>
包含了對資料GET、POST、PUT與DELETE方法，</br>
還有資料庫的應用。</br>

網頁採用了bootstrap與Jinja2，製作網頁作為參考。</br>


以FASTAPI範本進行實作</br>
https://github.com/UFOTreeboy/fastapi_demo

連結</br>
https://web-production-807d.up.railway.app/

## 佈署至Railway.app

### 第一步、靜態文件讀取路徑
- Railway.app支援Fastapi和jinja2模板，但目前觀察到的問題是jinja2的"url_for()"功能無法起作用。</br>
- 直接改成「相對路徑」，直接提供檔案的路徑會比較容易讀取到靜態文件。 </br>

- 範例: 有一段程式碼用到了url_for()，要讀取一個叫static的檔案中的css。</br>
`<link href="{{ url_for('static', path='/css/styles.css') }}" rel="stylesheet">`</br>

- 如果要正常讀取的資料的話就要改成這樣子。</br>
`<link href="static/css/styles.css"  rel="stylesheet">`</br>

### 第二步、增加requirement.txt、runtime.txt與Procfile這三個檔案
### 第三部、直接佈署(deploy)

成功後，你會看到這畫面</br>

![image](https://i.imgur.com/OgYsigk.png)
</br>
