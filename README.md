# Tello-Flight
Drone "Tello" control by Python

## forward_and_reverse.py

自動で離陸->上昇->前進->後退->着陸をするサンプルコード
```
$python3 forward_and_reverse.py
```
## rotate_cw.py

離陸して，与えられた周回数分，円を描くように時計回りに飛行して着陸するPythoコード

#### 実行方法
Pythonコードに引数として周回数を与える。
（２周回りたいときは"2"とする）
```
$python3 rotate_cw.py 2
```

## key.py

キーボードによるドローン操作
```
$python3 key.py
```

## video_effect.py

Telloについているカメラを起動させて画像を取得するPythonコード．
離陸の制御は入っていないので，ローターは回転しない．
そのため，実行時にはTello本体の発熱注意！

```
$python3 video_effect.py
```

## land.py
**Tellomの緊急着陸！**
万一システムが暴走してTelloが制御不能になった場合に，緊急着陸させるPythonコード

```
$python3 land.py
```

## takeoff_with_cam.py

**（未完成につき，使用注意）**
離陸->ホバリング->カメラを起動->画像を15sec撮影->着陸

WindowsのAnaconda環境下でのみ実行テスト済み．
画像がリアルタイムで取得できず，１フレームしか撮影できない状態．

