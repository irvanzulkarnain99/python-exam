install pip
pip install mysql-connector

create database webhook_integration
create table webhookconfiguration
-- webhook_integration.webhookconfiguration definition

CREATE TABLE `webhookconfiguration` (
  `webhook_configuration_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_id` varchar(100) NOT NULL,
  `is_active` int(11) NOT NULL,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `cerated_by` varchar(100) NOT NULL,
  `modified_by` varchar(100) NOT NULL,
  PRIMARY KEY (`webhook_configuration_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

for run file -> 
--python config.py
--python select-data.py
--python create-data.py
--python update-data.py

![python-image-select](https://github.com/user-attachments/assets/9ff2dded-98e8-43a4-b0f1-4aee7336144f)
![python-image-update](https://github.com/user-attachments/assets/75b23586-1bfb-44f1-977e-eb4e9bb57a34)
