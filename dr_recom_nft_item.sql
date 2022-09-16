CREATE TABLE IF NOT EXISTS `grmds054_druptest`.`dr_recom_nft_item` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `nft_id` BIGINT(20) NOT NULL DEFAULT 0,
  `name` VARCHAR(512) NOT NULL DEFAULT '',
  `description` TEXT NOT NULL DEFAULT '',
  `img_url` TEXT NOT NULL DEFAULT '',
  `price` VARCHAR(64) NOT NULL DEFAULT '0.00',
  `quantity` INT(10) NOT NULL DEFAULT 0,
  `item_owner` VARCHAR(128) NOT NULL DEFAULT '',
  `category_name` VARCHAR(128) NOT NULL DEFAULT '',
  `token_id` VARCHAR(256) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`));
