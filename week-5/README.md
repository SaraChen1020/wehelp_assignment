### 要求三
- 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
    
    `INSERT INTO member(id,name,username,password) VALUES (1,'admin','test','test');`
    
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-1.png)

- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

    `SELECT * FROM member;`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-2.png)

- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

    `SELECT * FROM member ORDER BY time DESC;`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-3.png)

- 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。

    `SELECT * FROM member ORDER BY time DESC LIMIT 1,3;`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-4.png)

- 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

    `SELECT * FROM member WHERE username='test';`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-5.png)

- 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

    `SELECT * FROM member WHERE username='test' AND password='test';`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-6.png)

- 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

    `UPDATE member SET name='test2' WHERE username='test';`

    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/3-7.png)