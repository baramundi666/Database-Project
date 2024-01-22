from datetime import datetime, date, timedelta

table = [(1,1,8,3,'2020-04-12 03:14:32','2023-11-30 10:39:37','http://instagram.com/group/9'),
  (2,5,3,2,'2025-01-13 17:08:38','2024-01-27 01:02:08','http://facebook.com/one'),
  (3,9,7,1,'2020-01-20 21:55:11','2023-01-22 09:24:07','https://bbc.co.uk/settings'),
  (4,13,6,3,'2022-10-29 03:26:40','2024-04-15 19:46:35','http://whatsapp.com/settings'),
  (5,17,5,3,'2019-09-22 03:07:43','2024-01-22 09:16:51','http://wikipedia.org/en-us'),
  (6,21,1,2,'2020-06-19 23:26:29','2024-01-25 11:18:43','https://baidu.com/user/110'),
  (7,25,6,2,'2020-09-25 01:37:12','2023-07-31 15:15:09','https://whatsapp.com/group/9'),
  (8,29,1,1,'2020-08-09 20:08:56','2024-07-24 00:40:03','http://netflix.com/en-us'),
  (9,33,7,3,'2024-09-07 10:36:55','2023-04-06 13:53:24','http://guardian.co.uk/group/9'),
  (10,37,3,1,'2020-01-03 17:52:08','2024-11-25 02:11:54','http://yahoo.com/sub'),
  (11,41,6,2,'2023-05-23 03:24:13','2023-06-05 21:18:51','https://youtube.com/one'),
  (12,1,9,2,'2024-07-29 12:48:56','2023-04-12 23:36:05','http://google.com/fr'),
  (13,5,10,2,'2022-02-08 19:56:25','2024-10-14 12:52:49','https://instagram.com/site'),
  (14,9,6,3,'2019-07-31 06:04:31','2023-02-24 11:13:01','http://reddit.com/fr'),
  (15,13,3,2,'2020-11-12 01:18:17','2024-02-25 00:08:52','https://nytimes.com/sub'),
  (16,17,7,1,'2024-07-06 02:08:49','2023-07-28 17:12:46','http://bbc.co.uk/settings'),
  (17,21,8,2,'2020-01-05 05:36:06','2024-07-22 02:59:44','http://instagram.com/en-ca'),
  (18,25,6,3,'2024-11-21 02:05:45','2023-03-27 21:04:21','https://instagram.com/site'),
  (19,29,10,1,'2019-08-24 22:25:43','2024-02-17 20:26:33','https://facebook.com/sub/cars'),
  (20,33,5,1,'2022-06-11 12:08:16','2023-11-03 19:16:51','https://youtube.com/en-ca'),
  (21,37,7,2,'2019-07-24 01:57:42','2024-08-02 10:18:49','http://facebook.com/one'),
  (22,41,8,3,'2020-10-31 22:15:57','2023-11-23 23:45:30','http://facebook.com/sub'),
  (23,1,8,2,'2022-06-11 17:35:09','2023-03-06 17:10:38','http://walmart.com/en-ca'),
  (24,5,7,1,'2022-03-13 00:01:27','2024-03-25 02:39:43','https://twitter.com/sub'),
  (25,9,1,2,'2019-08-09 03:24:24','2024-04-07 20:16:57','https://nytimes.com/settings'),
  (26,13,2,3,'2023-09-14 11:03:16','2023-02-12 11:27:56','http://guardian.co.uk/group/9'),
  (27,17,3,3,'2022-06-30 08:55:34','2023-04-15 00:30:38','http://wikipedia.org/group/9'),
  (28,21,8,3,'2022-11-27 16:41:34','2024-11-17 05:25:36','http://yahoo.com/site'),
  (29,25,2,2,'2020-05-25 01:34:48','2023-08-19 19:42:42','https://guardian.co.uk/en-ca'),
  (30,29,2,1,'2019-12-20 00:50:20','2024-09-22 05:23:58','http://nytimes.com/sub'),
  (31,33,3,1,'2022-06-27 12:52:56','2023-10-15 02:45:29','http://yahoo.com/one'),
  (32,37,6,3,'2024-07-04 04:40:23','2023-05-22 06:48:55','https://ebay.com/sub/cars'),
  (33,41,2,1,'2022-03-18 07:17:12','2023-06-16 10:17:21','http://youtube.com/one'),
  (34,1,4,3,'2021-03-04 02:23:37','2024-06-01 07:25:58','http://facebook.com/user/110'),
  (35,5,4,2,'2021-12-17 03:04:55','2024-03-26 11:43:16','http://google.com/en-ca'),
  (36,9,1,2,'2023-12-01 00:31:44','2023-12-24 02:23:26','http://whatsapp.com/sub/cars'),
  (37,13,10,3,'2024-02-29 22:08:35','2024-06-11 15:46:47','http://youtube.com/site'),
  (38,17,8,1,'2022-03-14 16:11:06','2023-09-26 08:57:04','https://yahoo.com/en-ca'),
  (39,21,6,3,'2021-11-01 21:14:46','2023-12-16 09:58:29','http://google.com/en-ca'),
  (40,25,10,3,'2021-12-15 12:29:38','2024-07-14 01:07:33','https://guardian.co.uk/group/9'),
  (41,29,2,3,'2022-04-10 12:51:18','2023-06-24 19:59:22','http://ebay.com/site'),
  (42,33,2,2,'2019-10-08 03:23:49','2023-10-05 11:13:16','https://yahoo.com/one'),
  (43,37,8,2,'2020-01-28 18:55:36','2023-11-10 22:15:24','http://whatsapp.com/group/9'),
  (44,41,5,2,'2023-02-03 03:52:30','2023-11-07 19:25:39','https://cnn.com/en-ca'),
  (45,1,1,2,'2021-04-19 20:51:19','2024-02-04 17:10:48','https://wikipedia.org/en-ca'),
  (46,5,3,2,'2019-02-06 00:01:49','2024-12-31 16:42:59','https://baidu.com/one'),
  (47,9,7,2,'2020-09-25 07:34:12','2024-10-27 08:55:10','https://nytimes.com/sub/cars'),
  (48,13,4,3,'2020-12-17 04:21:43','2023-12-08 23:33:42','http://nytimes.com/site'),
  (49,17,4,1,'2022-04-16 19:37:37','2023-08-16 21:13:08','https://youtube.com/fr'),
  (50,21,8,2,'2023-02-21 07:47:18','2023-11-01 02:33:29','http://twitter.com/one'),
  (51,25,5,1,'2021-08-13 14:37:25','2023-03-07 00:21:19','https://baidu.com/fr'),
  (52,29,7,2,'2024-10-13 12:32:04','2024-08-17 23:25:41','http://naver.com/user/110'),
  (53,33,2,2,'2021-01-15 23:45:28','2023-02-07 21:49:34','https://facebook.com/sub'),
  (54,37,6,1,'2020-08-18 00:51:19','2023-02-26 06:46:48','https://nytimes.com/one'),
  (55,41,6,2,'2021-03-21 21:02:07','2024-03-14 19:55:31','http://google.com/sub/cars'),
  (56,1,8,3,'2020-08-18 21:18:33','2024-11-28 20:50:57','http://reddit.com/en-ca'),
  (57,5,9,2,'2022-01-15 23:15:38','2023-10-27 19:00:42','https://yahoo.com/en-ca'),
  (58,9,9,3,'2023-09-21 10:25:18','2024-03-15 12:22:00','http://facebook.com/settings'),
  (59,13,2,3,'2022-01-17 17:27:46','2024-12-21 15:28:18','http://netflix.com/one'),
  (60,17,3,1,'2024-11-17 08:51:16','2024-07-03 09:23:11','https://guardian.co.uk/one'),
  (61,21,7,2,'2023-05-27 15:20:12','2023-08-27 23:17:21','http://google.com/group/9'),
  (62,25,8,2,'2021-09-22 16:52:55','2025-01-02 16:27:27','https://facebook.com/en-ca'),
  (63,29,3,1,'2019-02-14 12:03:16','2023-07-14 01:00:08','https://ebay.com/one'),
  (64,33,5,3,'2019-11-02 17:18:48','2024-10-26 06:33:55','http://wikipedia.org/sub'),
  (65,37,4,3,'2019-12-20 04:55:49','2024-05-05 01:32:06','http://google.com/sub'),
  (66,41,9,1,'2022-07-23 06:10:36','2025-01-02 03:54:40','https://netflix.com/group/9'),
  (67,1,3,2,'2021-04-16 12:38:09','2023-11-07 20:36:41','https://instagram.com/settings'),
  (68,5,6,1,'2022-03-20 16:45:50','2024-08-22 10:13:25','https://whatsapp.com/site'),
  (69,9,4,2,'2020-05-03 07:59:27','2023-04-26 01:28:55','https://instagram.com/fr'),
  (70,13,5,3,'2019-09-10 00:49:13','2024-10-27 05:08:14','http://zoom.us/user/110'),
  (71,17,4,2,'2022-07-12 00:53:11','2024-01-23 11:06:27','https://zoom.us/group/9'),
  (72,21,10,1,'2021-08-26 07:51:23','2024-09-21 16:19:37','https://yahoo.com/en-ca'),
  (73,25,3,1,'2021-08-29 20:53:53','2023-03-01 07:35:51','http://netflix.com/group/9'),
  (74,29,2,2,'2020-04-09 20:01:53','2023-11-18 03:06:06','https://facebook.com/en-ca'),
  (75,33,9,2,'2024-12-24 11:42:33','2024-05-22 16:17:14','https://walmart.com/one'),
  (76,37,2,3,'2021-12-20 20:51:37','2023-06-10 08:06:38','http://netflix.com/en-ca'),
  (77,41,5,3,'2020-02-14 09:32:03','2024-11-18 22:27:26','https://zoom.us/site'),
  (78,1,4,1,'2023-09-14 18:08:44','2023-06-01 05:11:49','http://netflix.com/sub/cars'),
  (79,5,4,2,'2024-05-23 05:38:54','2023-10-03 10:38:32','https://walmart.com/one'),
  (80,9,8,3,'2022-04-21 17:44:20','2023-07-11 05:51:05','http://wikipedia.org/en-us'),
  (81,13,7,2,'2020-02-11 21:34:53','2023-12-08 10:27:22','http://twitter.com/en-us'),
  (82,17,8,3,'2024-10-19 01:16:06','2023-05-13 23:55:51','http://pinterest.com/en-ca'),
  (83,21,6,1,'2022-01-23 12:52:11','2023-07-03 10:24:45','http://bbc.co.uk/one'),
  (84,25,2,2,'2024-02-19 22:57:11','2024-09-14 03:27:43','https://pinterest.com/settings'),
  (85,29,4,1,'2022-01-11 18:19:37','2024-03-17 15:48:33','http://ebay.com/sub/cars'),
  (86,33,8,2,'2019-09-01 01:40:05','2023-06-20 14:41:37','http://cnn.com/sub'),
  (87,37,6,2,'2022-09-07 01:35:17','2024-05-15 10:52:17','https://guardian.co.uk/en-ca'),
  (88,41,4,3,'2024-07-14 02:42:47','2023-12-22 00:22:51','http://ebay.com/site'),
  (89,1,8,2,'2020-03-05 09:13:13','2023-02-07 21:53:56','https://walmart.com/site'),
  (90,5,4,2,'2022-11-14 03:10:25','2024-10-16 15:40:44','http://twitter.com/one'),
  (91,9,7,3,'2024-04-01 19:32:31','2024-07-09 23:22:02','https://walmart.com/user/110'),
  (92,13,7,2,'2023-12-14 07:22:52','2023-04-15 10:20:46','https://cnn.com/one'),
  (93,17,4,1,'2024-06-21 06:29:52','2023-04-07 10:58:14','https://wikipedia.org/sub/cars'),
  (94,21,2,2,'2021-12-13 00:12:49','2024-11-18 17:35:08','http://netflix.com/settings'),
  (95,25,2,1,'2023-10-05 23:11:39','2024-05-21 23:16:27','https://twitter.com/site'),
  (96,29,7,3,'2020-02-17 11:26:08','2023-03-15 03:54:03','http://nytimes.com/fr'),
  (97,33,7,2,'2021-11-14 08:34:47','2023-07-21 08:21:22','http://bbc.co.uk/sub'),
  (98,37,4,3,'2020-07-13 04:24:29','2023-06-10 17:07:01','http://cnn.com/sub/cars'),
  (99,41,8,2,'2021-04-18 09:17:42','2024-05-14 03:51:49','http://wikipedia.org/one'),
  (100,1,2,3,'2021-10-15 00:01:26','2023-10-10 16:08:05','https://guardian.co.uk/en-ca')]
newdata = []
import random
val = 2
for i in range(1,300):
    #data = table[i]
    #startdate = data[4]
    # enddate = datetime.strftime(datetime.strptime(startdate, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1.5), '%Y-%m-%d %H:%M:%S')
    # data = (data[0],data[1],data[2], data[3],data[4],enddate,data[6])
    # val+=4
    # if val>1000:
    #     val = 2
    
    #x = (data[1],data[2],enddate, round(float(data[4])/3,2), float(data[4]))
    #w = data[3].replace(',','')
    #x = "EXEC AddLecture {}, {}, {}, '{}', '{}', '{}', '{}', {}, '{}'".format(*data)
    data = (i, (i*190)%97 + 1)
    if i<100:
        x= "EXEC UpdateWebinarsAttendance {}, {}, 'Present'".format(*data)
    else:
        x= "EXEC UpdateWebinarsAttendance {}, {}, 'Absent'".format(*data)
    newdata.append(x)


for data in newdata:
    print(data,end='')
    print('; ')