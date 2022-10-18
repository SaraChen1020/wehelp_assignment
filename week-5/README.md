### 要求三：SQL CRUD
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

---
### 要求四：SQL Aggregate Functions
- 取得 member 資料表中，總共有幾筆資料 (幾位會員)。

    `SELECT COUNT(*) FROM member`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/4-1.png)

- 取得 member 資料表中，所有會員 follower_count 欄位的總和。

    (計算此題之前，有再新增follower_count欄位資料如下)  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/4-2-1.png)  
    `SELECT SUM(follower_count) FROM member;`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/4-2-2.png)

- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

    `SELECT AVG(follower_count) FROM member;`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/4-3.png)

---
### 要求五：SQL JOIN (Optional)
- 建立 message 資料表紀錄留言資訊
    
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/5.png)  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/5.1.png)

- 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。

    `SELECT member.name, message.content, message.like_count, message.time FROM member INNER JOIN message ON member.id=message.member_id`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/5-1.png)

- 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。

    `SELECT member.name, message.content, message.like_count, message.time FROM member INNER JOIN message ON member.id=message.member_id AND member.username='test';`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/5-2.png)

- 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。

    `SELECT member.username, AVG(like_count) FROM member INNER JOIN message ON member.id=message.member_id AND member.username='test';`  
    ![image](https://github.com/SaraChen1020/wehelp_assignment/blob/main/week-5/screenshot/5-3.png)

