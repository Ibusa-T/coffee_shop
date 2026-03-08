-- 1. 商品区分
--商品テーブルとの結合時に区分名を指定するため
CREATE UNIQUE INDEX type_name_index ON PRODUCT_TYPE USING HASH (TYPE_NAME);

-- 3. セール期間（イベント親テーブル）
--セール情報確認の際に指定するときを想定
CREATE INDEX sale_period_index ON SALE_PERIOD USING HASH (SALE_TITLE);

-- 5. 顧客
--顧客名指定時パフォーマンスの向上のため
CREATE UNIQUE INDEX consumer_name_index ON CONSUMER USING HASH (CONSUMER_NAME);
CREATE INDEX consumer_gender_index  ON   CONSUMER (GENDER);


-- 6. 伝票
CREATE INDEX order_date_index ON SLIP USING HASH (ORDER_DATE);

-- 7. 配送
CREATE INDEX delivery_date_index ON DELIVERY USING HASH (DELIVERY_DATE);
CREATE INDEX delivery_status_index ON DELIVERY (DELIVERY_STATUS);