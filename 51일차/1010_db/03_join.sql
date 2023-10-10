SELECT * FROM articles;
SELECT * FROM users;

DROP TABLE articles;
DROP TABLE users;

CREATE TABLE users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50) NOT NULL,
content VARCHAR(100) NOT NULL,
userId INTEGER NOT NULL,
FOREIGN KEY (userId) -- userId 컬럼은 외래키 제약 조건인데
    REFERENCES users(id) -- users 테이블의 id 컬럼값을 참조
);
SELECT * FROM users WHERE id = 1;

INSERT INTO
    users (name)
VALUES
    ("하석주"),
    ("송윤미"),
    ("유하선");

INSERT INTO
    articles (title, content, userId)
VALUES
    ('제목1', '내용1', 1),
    ('제목2', '내용2', 2),
    ('제목3', '내용3', 3),
    ('제목4', '내용4', 4),
    ('제목5', '내용5', 5);

SELECT * FROM articles WHERE id = 1;

-- 1번 게시글의 작성자 찾기

SELECT userId FROM articles WHERE id = 1;

SELECT name FROM users WHERE id = 1;

SELECT id
FROM articles
INNER JOIN users
ON users.id = articles.userId;


-- LEFT JOIN
SELECT *
FROM articles
LEFT JOIN users
ON users.id = articles.userId;


-- 테이블 레코드 삭제시
DELETE FROM users
WHERE id = 3;

SELECT * FROM articles;

SELECT * FROM albums;
select * FROM artists;