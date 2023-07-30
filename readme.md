sudo -u postgres psql
create user mehrnooch with password 'miloo123456';
create database urlhasher with owner mehrnooch encoding='UTF8';

