'house_title','house_href', 'house_name', 'house_num', 'house_price', 'house_style', 'house_room', 'house_size', 'house_toward', 'house_imgdir'

house_title,house_href,house_name,house_num,house_price,house_style,house_room,house_size,house_toward,house_imgdir


CREATE TABLE 'lianjia'(
  'id' int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  'house_title' varchar(50) DEFAULT NULL COMMENT '房屋信息title',
  'house_href' varchar(50) DEFAULT NULL COMMENT '房屋信息title',
  'house_name' varchar(30) DEFAULT NULL COMMENT '小区名称',
  'house_num' varchar(30) DEFAULT NULL COMMENT '小区厅室',
  'house_price' varchar(30) DEFAULT NULL COMMENT '小区房屋大小',
  'house_style' varchar(30) DEFAULT NULL COMMENT '小区房屋朝向',
  'house_room' varchar(30) DEFAULT NULL COMMENT '哪个地方租',
  'house_size' varchar(30) DEFAULT NULL COMMENT '楼层',
  'house_toward' varchar(30) DEFAULT NULL COMMENT '建筑类型',
  'house_imgdir' varchar(15) DEFAULT NULL COMMENT '看房时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;




CREATE TABLE lianjia(
  id int(10) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  house_title varchar(50) DEFAULT NULL COMMENT '房屋信息title',
  house_href varchar(50) DEFAULT NULL COMMENT '房屋信息title',
  house_name varchar(30) DEFAULT NULL COMMENT '小区名称',
  house_num varchar(30) DEFAULT NULL COMMENT '小区厅室',
  house_price varchar(30) DEFAULT NULL COMMENT '小区房屋大小',
  house_style varchar(30) DEFAULT NULL COMMENT '小区房屋朝向',
  house_room varchar(30) DEFAULT NULL COMMENT '哪个地方租',
  house_size varchar(30) DEFAULT NULL COMMENT '楼层',
  house_toward varchar(30) DEFAULT NULL COMMENT '建筑类型',
  house_imgdir varchar(15) DEFAULT NULL COMMENT '看房时间',
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;


CREATE TABLE lianjia
(
Id_P int,
house_title varchar(255),
house_href varchar(255),
house_name varchar(255),
house_num varchar(255),
house_price varchar(255),
house_style varchar(255),
house_room varchar(255),
house_size varchar(255),
house_toward varchar(255),
house_imgdir varchar(255)
)


CREATE TABLE `lianjia` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `house_title` varchar(50) DEFAULT NULL COMMENT '房屋详细信息链接',
  `house_href` varchar(100) DEFAULT NULL COMMENT '房屋信息title',
  `house_name` varchar(30) DEFAULT NULL COMMENT '小区名称',
  `house_num` varchar(30) DEFAULT NULL COMMENT '小区厅室',
  `house_price` varchar(30) DEFAULT NULL COMMENT '小区房屋大小',
  `house_style` varchar(30) DEFAULT NULL COMMENT '小区房屋朝向',
  `house_room` varchar(30) DEFAULT NULL COMMENT '哪个地方租',
  `house_size` varchar(30) DEFAULT NULL COMMENT '楼层',
  `house_toward` varchar(30) DEFAULT NULL COMMENT '建筑类型',
  `house_imgdir` varchar(100) DEFAULT NULL COMMENT '看房时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;