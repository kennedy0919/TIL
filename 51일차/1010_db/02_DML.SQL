CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt Date NOT NULL
);

-- 테이블 정보 확인
PRAGMA table_info('articles');

-- 테이블에 데이터 여러개 삽입
INSERT INTO
    articles(title, content, createdAt)
VALUES
    ('hello1', 'content1', '2000-01-01'),
    ('hello2', 'content2', '2000-01-01'),
    ('hello3', 'content3', '2000-01-01');

-- Date() 함수를 사용해서 날짜 데이터 입력
INSERT INTO
    articles(title, content, createdAt)
VALUES
    ('mytitle', 'mycontent', Date());

-- 테이블의 데이터 수정
UPDATE
    articles
SET
    title = 'update Title'
WHERE
    id = 1;

DELETE FROM
    articles
WHERE
    id IN (
    SELECT 
        id
    FROM
        articles
    ORDER BY
        createdAt DESC
    LIMIT 1
);