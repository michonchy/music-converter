import ffmpeg
 
# 入力
stream = ffmpeg.input("dummy_movie/ヴァンパイア.3gpp")
# 出力
stream = ffmpeg.output(stream, "dummy_movie/test.mp3") 
# 実行
ffmpeg.run(stream)
