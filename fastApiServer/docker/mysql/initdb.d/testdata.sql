# insert into users(user_id, user_email, password, user_name, phone, birth, address, job, user_interests)
# values (UNHEX(REPLACE(UUID(),'-','')),'hong@test.com', '1', '홍길동', '010-1234-5678', '2000-01-01', '서울시 강남구', '개발자', '영화');
#
# insert into users(user_id, user_email, password, user_name, phone, birth, address, job, user_interests)
# values (UNHEX(REPLACE(UUID(),'-','')),'park@test.com', '1', '박재범', '010-3344-5678', '2000-07-01', '서울시 강북구', '개발자', '여행');
#
# insert into articles(title, content)
# values ('number1', 'test1');
#
# insert into articles(title, content)
# values ('number2', 'test2');
#
# select * from users;
#
# select * from articles;