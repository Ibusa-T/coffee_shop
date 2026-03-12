📝 ビジネス要件：オンラインショップ「Geminiマート」
    運営者から、以下のような管理をしたいと相談を受けました。

1. 顧客について
  「誰がいつ会員になったか把握したい。名前とメールアドレスは必須。メールアドレスが重複して登録されるのは困る。」
  

2. 商品と分類について
  「商品はたくさんある。例えば『食品』とか『家電』といったカテゴリで分けたい。1つの商品は必ずどこか1つのカテゴリに入るようにしてほしい。」

  「商品には『現在の販売価格』を設定する。たまに価格改定をするけれど、過去の注文記録まで今の価格で計算されちゃうと困るんだ。」
      --過去の売り上げは当時の価格で受ける

  「商品の在庫数も管理したい。在庫がマイナスになるのは論外だよ。」

3. 注文プロセスについて
    「お客さんは一度の買い物で、複数の商品をまとめて買えるようにしたい（買い物カゴのイメージ）。」

    「注文ごとに、合計金額と、いつ注文されたかの記録を残したい。」

    「注文明細には、その時『何個買ったか』と、その時の『適用価格』を記録しておきたい。」

4. 分析の要望（将来のデータアナリストとして）
    「後から『どのカテゴリの商品が一番売れているか』や『リピーター（2回以上購入した人）が誰か』をSQLでサクッと集計できるようにしておいてね。」



📊 Geminiマート：確定ビュー定義および物理構成資料1. 売上分析レイヤー日次の動向と、売れ筋商品を把握するための基盤。
## 日ごとの商品別売上 (DAILY_SALES_BY_PRODUCT)用途: 商品ごとの日次トレンド分析
SQL CREATE VIEW DAILY_SALES_BY_PRODUCT AS  
    SELECT  
        PR.PRODUCT_NAME   AS 商品名
    ,SUM(SL.QUANTITY * SL.PRICE) AS 売上金額
    ,SUM(SL.QUANTITY)  AS 数量
    ,SL.ORDER_DATE     AS 日付
    FROM SLIP    AS SL
    JOIN PRODUCT AS PR ON SL.PRODUCT_CODE = PR.PRODUCT_CODE
    GROUP BY SL.ORDER_DATE, PR.PRODUCT_NAME;

## 日ごと総売上 (DAILY_SALES)用途: 店舗全体の売上目標達成率の確認
SQL CREATE VIEW DAILY_SALES AS  
    SELECT
        SUM(SL.QUANTITY * SL.PRICE) AS 売上金額
    ,SUM(SL.QUANTITY)  AS 数量
    ,SL.ORDER_DATE     AS 日付
    FROM SLIP    AS SL
    JOIN PRODUCT AS PR ON SL.PRODUCT_CODE = PR.PRODUCT_CODE
    GROUP BY SL.ORDER_DATE;

2. マーケティング・戦略レイヤー「何が」「誰に」売れているかを可視化し、施策に繋げるためのビュー。
## 商品区分ごとの売上 (TYPE_SALES)ポイント: 売上金額順にソート（DESC）し、優先順位を明確化
SQL CREATE VIEW TYPE_SALES AS
        SELECT 
            PT.TYPE_NAME   AS 商品区分
        ,SUM(SL.QUANTITY * SL.PRICE) AS 売上金額
        FROM PRODUCT      AS PR
        JOIN PRODUCT_TYPE AS PT ON PR.TYPE_CODE = PT.TYPE_CODE
        JOIN SLIP         AS SL ON SL.PRODUCT_CODE = PR.PRODUCT_CODE
        GROUP BY PT.TYPE_NAME
        ORDER BY SUM(SL.QUANTITY * SL.PRICE) DESC;

## 性別毎の商品売上 (GENDER_SALES)ポイント: ELSE NULL により、集計時のノイズを完全に除去
SQL CREATE VIEW GENDER_SALES AS 
    SELECT
        PR.PRODUCT_NAME AS 商品名
    ,SUM(CASE WHEN CON.GENDER = '1' THEN SL.QUANTITY * SL.PRICE ELSE NULL END) AS 男性
    ,SUM(CASE WHEN CON.GENDER = '2' THEN SL.QUANTITY * SL.PRICE ELSE NULL END) AS 女性
    FROM CONSUMER AS CON
    JOIN SLIP     AS SL ON CON.CONSUMER_CODE = SL.CONSUMER_CODE
    JOIN PRODUCT  AS PR ON SL.PRODUCT_CODE = PR.PRODUCT_CODE
    GROUP BY PR.PRODUCT_NAME;

3. 顧客ロイヤリティレイヤーリピーターを特定し、顧客定着率を測定するための高度な分析ビュー。
## 来店回数分析 (VISIT)技術: 名前付きウィンドウ句（WINDOW句）と DENSE_RANK による来店日数の正確なカウント
SQL CREATE VIEW VISIT AS 
    SELECT
        CON.CONSUMER_CODE AS 顧客コード
    ,CON.CONSUMER_NAME AS 顧客名
    ,MAX(DENSE_RANK() OVER W) AS 購入回数 
    FROM CONSUMER AS CON
    JOIN SLIP     AS SL ON CON.CONSUMER_CODE = SL.CONSUMER_CODE
    GROUP BY CON.CONSUMER_CODE, CON.CONSUMER_NAME, SL.ORDER_DATE
    WINDOW W AS (PARTITION BY CON.CONSUMER_CODE ORDER BY SL.ORDER_DATE);

    
相棒、データのないところからここまで積み上げた「ハード」な仕事、本当にお疲れ様。プロジェクト「Geminiマート」設計フェーズ、これにてコンプリートだ。ゆっくり休めよ。また明日、現場の様子を伝えてやる。グッドナイト！