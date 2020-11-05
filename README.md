# Tello-Flight
Drone "Tello" control by Python

## Python Code
### rotate_cw.py
***
Telloを定常円旋回させるPythonコードです。
引数に何周するか、周回数を与えて実行します。
離陸後、与えた周回数分だけ時計回りに円を描くように旋回します。

```
$python3 rotate_cw.py 2
```
Telloを前進させるコマンド、「forward()」とその場旋回(時計回り)させるコマンド「clockwise()」との組み合わせで円を描くように飛行します。
※床面の状態や風の有無で離陸ポイントと着陸ポイントはズレます...

### forward_and_reverse.py
***
Telloを前進させてから後退させるPythonコードです。
```
$python3 forward_and_reverse.py
```

### video_effect.py
***
Telloのカメラ機能を使って、ストリーミング画像を取得するサンプルコード。

### takeoff_with_cam.py
***
Telloを離陸させ、ホバリング状態でカメラ撮影を行ってから着陸するコードです。
