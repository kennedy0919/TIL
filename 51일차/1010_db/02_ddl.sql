CREATE TABLE examples(
    ExamID INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
-- 테이블 정보 확인
PRAGMA table_info('examples');

-- 테이블 구조 변경: 컬럼 추가
ALTER TABLE
    examples
ADD COLUMN
    Country VARCHAR(100);

ALTER TABLE
    examples
ADD COLUMN
    Age INTERSECT;

ALTER TABLE
    examples
ADD COLUMN
    Address VARCHAR(100);

-- 테이블의 컬럼 이름 변경
ALTER TABLE
    examples
RENAME COLUMN Address TO PostCode;

-- 테이블의 컬럼 삭제
ALTER TABLE
    examples
DROP COLUMN PostCode;

-- 테이블 구조 변경 :  컬럼 추가시 기본값 설정
ALTER TABLE
    examples
ADD COLUMN
    PostCode VARCHAR(100) DEFAULT 'N' NOT NULL;

-- 테이블 이름 변경
ALTER TABLE
    examples
RENAME TO
    new_examples11;

-- 테이블 삭제
DROP TABLE new_examples11;